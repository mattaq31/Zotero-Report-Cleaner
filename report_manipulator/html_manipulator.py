from bs4 import BeautifulSoup


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
        self.field_commands = {'Type': True,
                               'Author': True,
                               'URL': True,
                               'Volume': False,
                               'Pages': False,
                               'Publication': True,
                               'Publisher': False,
                               'DOI': False,
                               'Issue': False,
                               'Extra': False,
                               'Accessed': False,
                               'Abstract': False,
                               'ISSN': False,
                               'Date': True,
                               'Rights': False,
                               'ISBN': False,
                               'Short Title': False,
                               'Conference Name': False,
                               'Library Catalog': False,
                               'Editor': False,
                               'Language': False,
                               'Website Title': False,
                               'Loc. in Archive': False,
                               'Archive': False,
                               'Journal Abbr': False,
                               'Date Added': False,
                               'Inventor': False,
                               'Issue Date': False,
                               'Assignee': False,
                               'Issuing Authority': False,
                               'Patent Number': False,
                               'Filing Date': False,
                               'Application Number': False,
                               'Country': False,
                               'Modified': False}  # default values

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
            file.write(str(self.report_html))

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
                            authors += '%s' % data_container.td.get_text()
                            data_container.th.string.replace_with('Authors')
                            data_container.td['id'] = 'author'
                        else:
                            authors += ', %s' % data_container.td.get_text()
                            data_container.extract()

            if authors != '':  # Injects collected authors into one Author tag
                main_item.find(id='author').string.replace_with(authors)

        return True
