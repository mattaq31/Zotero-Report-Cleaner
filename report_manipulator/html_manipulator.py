from bs4 import BeautifulSoup
import os
import csv


class HtmlManipulator:
    """
    Class containing methods for manipulating Zotero HTML report
    """
    def __init__(self, output: str = None):
        """
        Upon initialization, defaults are loaded for which fields to remove/keep
        :param output: output location to save data
        """
        self.report_html = None
        self.output_dir = output
        self.one_line_authors = True
        self.commands_dir = os.path.dirname(os.path.abspath(__file__)) + "/commands_config.tsv"
        self.field_commands = self.read_commands_config(self.commands_dir)

    def add_field_command(self, field: str, value: bool):
        """
        Add another field command to current list
        :param field: Label for field to keep/remove
        :param value: boolean indicating whether the given field should be
        :return: None
        """
        self.field_commands[field] = value

    def read_html(self, input_loc: str):
        """
        :param input_loc: location of Zotero HTML report to read
        :return: None
        """
        self.parse_html(open(input_loc, "r"))

    def parse_html(self, data):
        """
        Parses given HTML report using BeautifulSoup.
        :param data: HTML report to parse
        :return: None
        """
        self.report_html = BeautifulSoup(data, 'lxml')

    def save_html(self):
        """
        Saves current HTML report to file.
        :return: None
        """
        with open(self.output_dir, "w") as file:
            file.write(str(self.report_html.prettify()))

    def save_commands_config(self, data: dict):
        """
        Saves provided commands to default configuration file.
        :param data: Dict containing commands and their keep(1)/discard(0) value
        :return: None
        """
        with open(self.commands_dir, 'w+') as f:
            f.write('Command\tValue\n')
            for key, val in data.items():
                f.write('%s\t%d\n' % (key, val))

    @staticmethod
    def read_commands_config(commands_dir: str):
        """
        Reads commands from specified file.
        :param commands_dir: Commands file name
        :return: commands dict: each command is a key, with a binary value specifying whether to keep/discard said key
        """
        with open(commands_dir) as f:
            reader = csv.reader(f, delimiter="\t")
            next(reader)
            field_commands = {rows[0]: bool(int(rows[1])) for rows in reader}
        return field_commands

    def convert_html(self, data=None):
        """
        Function which removes marked fields from a Zotero report, and reorganises the authors into one line.
        Final report saved as an attribute of this class.
        :param data: Zotero report for parsing (optional, can be defined earlier)
        :return: True/False on success/failure
        """
        if data is not None:  # Parse data if provided
            self.parse_html(data)

        if self.report_html is None:  # No report provided
            return False

        for main_item in self.report_html.find_all('tbody'):  # tbody division used to locate each report entry
            authors = ''
            for data_container in main_item.children:
                if data_container != '\n':
                    label = data_container.th.get_text()  # Th tag contains field type
                    if label in self.field_commands and not self.field_commands[label]:
                        # Remove field if label not in accepted list
                        data_container.extract()
                    elif label == 'Author' and self.one_line_authors:  # Collects authors and places them in one string
                        if authors == '':
                            authors += data_container.td.get_text()
                            data_container.th.string.replace_with('Authors')
                            data_container.td['id'] = 'author'
                        else:
                            authors += ', %s' % data_container.td.get_text()
                            data_container.extract()

            if authors != '':  # Injects collected authors into one Author tag
                main_item.find(id='author').string.replace_with(authors)

        return True
