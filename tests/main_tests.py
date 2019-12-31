import requests
from report_manipulator.html_manipulator import HtmlManipulator


def test_api_convert(report, output, api_url):
    """
    Testing of converter with an API
    :param report: input report location
    :param output: output location for saving converted report
    :param api_url: API target URL
    :return: None, saves output to file
    """

    api_url = api_url + '/reporteditor'
    data = open(report, 'r').read()
    res = requests.post(api_url, json={'data': data})  # POST request to API
    with open(output, "w") as file:
        file.write(res.text)


def test_api_defaults(api_url):
    """
    Testing of API defaults
    :return: None
    :param api_url: API target URL
    """
    api_url = api_url + '/defaults'
    res = requests.get(api_url)  # GET request to API
    print(res.text)


def test_convert(report, output):
    """
    Local testing of main converter
    :param report: input report location
    :param output: output location for saving converted report
    :return: None, saves output to file
    """
    editor = HtmlManipulator(output)
    editor.read_html(report)
    editor.convert_html()
    editor.save_html()


if __name__ == '__main__':

    # Change inputs as required
    input = '*/input.html'
    output = '*/output.html'
    api_url = 'your API'

    test_api_convert(input, output, api_url)
    test_api_defaults(api_url)
