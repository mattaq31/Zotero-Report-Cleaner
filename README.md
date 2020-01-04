Zotero Report Editor
==============================
CI here

What Is This?
-------------

This repository contains a simple Python app which allows one to easily clean up Zotero [reports](https://www.zotero.org/support/reports#%20sort_order).  The main two features of this cleanup are the ability to cut off needless meta-information from each record and the arrangement of authors on one line (as opposed to the standard one author per line).  The resulting reports are leaner and much more practical for comparing notes and sharing research ideas.  App inspired by Jason Priem's [Zotero Report Customizer](http://jasonpriem.org/projects/report_cleaner.php).

The repository provides both a command-line interface and instructions on how to deploy the app to [Google Cloud Run](https://cloud.google.com/run/).  Ready-to-go web interface (coded using [JSSoup](https://www.npmjs.com/package/jssoup) and [Browserify](http://browserify.org)) also available [here](https://matthewaquilina.net/zotero_report_editor).

Command-Line Interface Installation And Usage
---------------------------------------------

### Installation

Activate your preferred Python (3.x) environment and run the following commands from the repo home directory:

1. `pip install -r requirements.txt`
2. `pip install --editable .`

Once installed, the interface can be used from any location on your computer.
### Usage

First, generate your Zotero report directly from the Zotero app by following [this](https://www.zotero.org/support/reports#%20sort_order) guide.  Then, command-line interface can be used by running the command:

`zotero_convert REPORT OUTPUT [Options]`

Where:

* `REPORT` - Location of unedited Zotero report (in one-page HTML format).
* `OUTPUT` - Location to save final edited report (also in HTML format).
* Adding the tag `--enforce_one_line_authors` will deactivate placing all authors on one line.

Alternatively, the `report_manipulator` package can be imported and used directly in Python.

Tested using Python 3.6+.

Deploying To Google Cloud Run
-----------------------------

The app can also be deployed to Google Cloud Run, where the API can be exposed for use within a web app.  This can be done for free, as long as you keep within the free tier [limits](https://cloud.google.com/run/pricing).

To deploy, simply create a project, enable the Cloud Build/Cloud Run APIs and install the Google Cloud SDK as described [here](https://cloud.google.com/run/docs/quickstarts/build-and-deploy) and [here](https://cloud.google.com/sdk/docs/#install_the_latest_cloud_tools_version_cloudsdk_current_version) respectively.  Then, build and deploy the app by executing the following two commands at the root directory of this repo:

`gcloud builds submit --tag gcr.io/**your project name**/zotero_report_editor`

`gcloud run deploy --image gcr.io/**your project name**/zotero_report_editor --platform managed`

Once deployed, the app exposes the following URLs: 

`*cloud_run_url*/defaults` - Accepts GET requests, and sends back the default meta-tags (and their values) stored within the app as a JSON string.

`*cloud_run_url*/reporteditor` -   Accepts POST requests with a JSON payload containing the below keys.  The request will return the edited report directly.

* `data` - HTML source of a Zotero report.
* `commands` - JSON string containing all meta-tags and their value (Boolean).
* `one_line_authors` - Boolean specifying whether authors should be placed on one line or left as-is.

Local Testing
-------------
The file `tests/main_tests.py` contains a Python file which can be used for directly testing out both the Python function and the Cloud Run API.

Further Development
-------------------
Open to suggestions/improvements.
