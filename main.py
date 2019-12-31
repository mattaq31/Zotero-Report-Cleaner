# !/usr/bin/python3

import click
from report_manipulator.html_manipulator import HtmlManipulator


@click.command()
@click.option('--report', prompt='Zotero report location', help='Unedited Zotero report to convert')
@click.option('--output', prompt='Edited Report output location', help='Output location')
def convert(report, output):
    editor = HtmlManipulator(output)
    editor.read_html(report)
    editor.convert_html()
    editor.save_html()


