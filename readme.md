Movescount backup
=============

This repository contains collected tips on how to make a backup of your data in Suunto Movescount service.

Usage
-----

First log in to Movescount, go to Summary page and load one html page from each year. You can do it in various ways. I used iMacros browser plugin with the macro in file imacro.txt. But as there is most likely only 5-10 years, it is probably even faster to just do it manually.

When you have all downloaded, run load_ids.py. It will look for the files in "data/" folder and go through them for the excercise ids. It produces list in .txt format and links to .fit files in .csv format. Note also that the python script uses BeautifulSoup library which you have to have installed to your Python.

With the list of links, you can use your favorite broser download manager to files. Note that you have to be logged in to be able to load files.

The downloaded fit-tiles you can then save and/or import to other services.

Importing to Endomondo (example)
-----

Coming.