# !/usr/bin/python3

import click
from report_manipulator.html_manipulator import HtmlManipulator


@click.command()
@click.option("--enforce_one_line_authors", default=False, is_flag=True,
              help='Specify whether authors should be left as is.'
                   '  By default, program will arrange all authors on one line.')
@click.argument('report', type=click.Path(exists=True))
@click.argument('output', type=click.Path())
def convert(report, output, enforce_one_line_authors):
    """Streamlines a Zotero Report by removing unnecessary tags and placing authors on one line.

    REPORT is the path to the html file to convert.
    OUTPUT is the path to which the converted report should be saved.
    """
    editor = HtmlManipulator(output)
    editor.read_html(report)
    editor.one_line_authors = not enforce_one_line_authors
    editor.convert_html()
    editor.save_html()


