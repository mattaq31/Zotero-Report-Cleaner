Zotero Report Editor
==============================
CI here

What Is This?
-------------

This is a simple Python app which allows one to easily clean up Zotero [reports](https://www.zotero.org/support/reports#%20sort_order).  The main two features of this cleanup are the ability to cut off needless meta-information from each record and the arrangement of authors on one line (as opposed to one author per line).  Resulting reports are cleaner and much more practical when used for comparing notes and sharing research ideas.  App inspired by Jason Priem's [Zotero Report Customizer](http://jasonpriem.org/projects/report_cleaner.php).

The app provides both a command-line interface and instructions on how to deploy the app to [Google Cloud Run](https://cloud.google.com/run/).  Web Interface also available at *link here*.

How To Use This
---------------

1.

Testing
-------

Deploying To Google Cloud Run
-----------------------------

The app can also be deployed to Google Cloud Run, where the API can be exposed for use within a web app.  This can be done for free, as long as you keep within the free tier [limits](https://cloud.google.com/run/pricing).

To deploy, simply create a project and enable the Cloud Build/Cloud Run APIs as described [here](https://cloud.google.com/run/docs/quickstarts/build-and-deploy).  Then, build and deploy the app by executing the following two commands at the root directory of this repo:

`gcloud builds submit --tag gcr.io/**your project name**/zotero_report_editor`

`gcloud run deploy --image gcr.io/**your project name**/zotero_report_editor --platform managed`

Once deployed, the app has two usable URLs: *cloud_run_url*/reporteditor and *cloud_run_url*/defaults

Further Development
-------------------
Open to suggestions/improvements.

Licensing
---------
*Add license here*
