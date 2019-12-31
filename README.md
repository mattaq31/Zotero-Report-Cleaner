Zotero Report Editor
==============================
CI here

What Is This?
-------------

This repository contains a simple Python app which allows one to easily clean up Zotero [reports](https://www.zotero.org/support/reports#%20sort_order).  The main two features of this cleanup are the ability to cut off needless meta-information from each record and the arrangement of authors on one line (as opposed to the standard one author per line).  The resulting reports are cleaner and much more practical when used for comparing notes and sharing research ideas.  App inspired by Jason Priem's [Zotero Report Customizer](http://jasonpriem.org/projects/report_cleaner.php).

The repository provides both a command-line interface and instructions on how to deploy the app to [Google Cloud Run](https://cloud.google.com/run/).  Ready-to-go web interface also available at *link here*.

How To Use Command-Line/Python Interface
---------------

1.

Deploying To Google Cloud Run
-----------------------------

The app can also be deployed to Google Cloud Run, where the API can be exposed for use within a web app.  This can be done for free, as long as you keep within the free tier [limits](https://cloud.google.com/run/pricing).

To deploy, simply create a project and enable the Cloud Build/Cloud Run APIs as described [here](https://cloud.google.com/run/docs/quickstarts/build-and-deploy).  Then, build and deploy the app by executing the following two commands at the root directory of this repo:

`gcloud builds submit --tag gcr.io/**your project name**/zotero_report_editor`

`gcloud run deploy --image gcr.io/**your project name**/zotero_report_editor --platform managed`

Once deployed, the app exposes the following URLs: 

`*cloud_run_url*/defaults` - Accepts GET requests, and sends back the default meta-tags (and their values) stored within the app as a JSON string.

`*cloud_run_url*/reporteditor` -   Accepts POST requests with a JSON payload containing the following keys:

* `data` - HTML source of a Zotero report.
* `commands` - JSON string containing all meta-tags and their value (Boolean).
* `one_line_authors` - Boolean specifying whether authors should be placed on one line or left as-is.

Testing
-------

Further Development
-------------------
Open to suggestions/improvements.

Licensing
---------
*Add license here*
