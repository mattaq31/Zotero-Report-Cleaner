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
----------------
To Build:
gcloud builds submit --tag gcr.io/**project name**/zotero_report_editor

To Deploy:
gcloud run deploy --image gcr.io/**project name**/zotero_report_editor --platform managed

Further Development
-------------------
Open to suggestions/improvements.

Licensing
---------
*Add license here*
