import os

from flask import Flask, request, redirect, url_for, jsonify
from report_manipulator.html_manipulator import HtmlManipulator

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('reporteditor')


@app.route('/reporteditor', methods=['GET', 'POST'])
def html_trigger_convert():
    if request.method == 'GET':
        return 'Zotero Report Editor Interface.', 200
    elif request.method == 'POST':
        request_json = request.get_json(silent=True)
        editor = HtmlManipulator()
        if 'commands' in request_json:
            editor.field_commands = request_json['commands']
        if 'one_line_authors' in request_json:
            editor.one_line_authors = request_json['one_line_authors']
        editor.convert_html(request_json['data'])
        return str(editor.report_html), 200


@app.route('/defaults', methods=['GET'])
def return_defaults():
    if request.method == 'GET':
        return jsonify(HtmlManipulator().field_commands), 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
