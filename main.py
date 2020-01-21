# !/usr/bin/python3

import click
from report_manipulator.html_manipulator import HtmlManipulator
from report_manipulator.index_maker import IndexMaker


@click.command()
@click.argument('root_directory', type=click.Path())
def index_reports(root_directory):
    """Creates index files for easy navigation between report folders.

    ROOT_DIRECTORY is the path to the root folder to create indexes within
    """
    index_maker = IndexMaker(root_directory)
    index_maker.generate_contents()


@click.command()
@click.option("--enforce_one_line_authors", default=False, is_flag=True,
              help='Enforce keeping each author individually separated line-by-line.'
                   '  By default, this app will arrange all authors to be placed together on one line.')
@click.option("--commands_file", default=None,
              help='Location of custom commands file to use when specifying which report tags to keep/discard.')
@click.option("--override_defaults", default=False, is_flag=True,
              help='Setting this flag will override the default commands with those specified in this call.')
@click.option("--just_remove", default=None,
              help='Specify the only tags to be removed from the report.  '
                   'Comma-separate each tag and replace spaces with underscores e.g. Name,Author,Date_Added,... '
                   'If both present, *just_remove* takes priority over *commands_file*.')
@click.option("--also_remove", default=None,
              help='Specify additional tags to remove, apart from the defaults.'
                   ' Comma-separate each tag and replace spaces with underscores e.g. Name,Author,Date_Added,...')
@click.argument('report', type=click.Path(exists=True))
@click.argument('output', type=click.Path())
def convert(report, output, enforce_one_line_authors, commands_file, override_defaults, just_remove, also_remove):
    """Streamlines a Zotero Report by removing unnecessary tags and placing authors on one line.

    REPORT is the path to the html file to convert.
    OUTPUT is the path to which the converted report should be saved.
    """

    # Read and setup editor
    editor = HtmlManipulator(output)
    editor.read_html(report)
    editor.one_line_authors = not enforce_one_line_authors

    # Specify changes to commands
    if just_remove is not None:
        editor.field_commands = {command: 0 for command in just_remove.replace('_', ' ').split(',')}
    elif commands_file is not None:
        editor.field_commands = editor.read_commands_config(commands_file)

    if also_remove is not None:
        for command in also_remove.replace('_', ' ').split(','):
            editor.add_field_command(command, False)

    # Perform conversion
    editor.convert_html()
    editor.save_html()

    # Override default commands if specified
    if override_defaults:
        editor.save_commands_config(editor.field_commands)
