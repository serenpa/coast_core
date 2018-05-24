The extraction module
=================
**Currently under development**
Introduction
------------

Usage
-----

Table of function(s)
--------------------
+----------------------+-------------------------------------------------------------------+
| Function             | Description                                                       |
+----------------------+-------------------------------------------------------------------+
| get_html(url)        | Given a URL, will return the HTML using urllib3.                  |
|                      | :param url: The url to extract the HTML from                      |
|                      | :return: If extracted successfully, the HTML is returned.         |
|                      | If there is a failure, a message with HTTP status.                |
|                      | If an exception is thrown, -1 is returned with a                  |
|                      | description of the error                                          |
+----------------------+-------------------------------------------------------------------+
| full_extraction(url) | Runs a complete end-to-end extraction using all other functions.  |
|                      | Refer to the documentation for usage guidelines and descriptions  |
|                      | of how the config file should be structured.(<<link>>)            |
|                      | :param url: The url to extract the HTML from                      |
|                      | :return: The html extracted from the url                          |
+----------------------+-------------------------------------------------------------------+
