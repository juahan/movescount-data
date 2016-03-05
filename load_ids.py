#!/usr/bin/python
# -*- coding: utf-8 -*-

#   Movescount-id loader
#    05.03.2016
#    ver 0.1
#
#   Juhana Heino

from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join

data_path = "data/"

path_file_list = [f for f in listdir(data_path) if isfile(join(data_path, f))]

id_array = []
link_array = []

for item in path_file_list:
    with open(data_path + item, "r") as f:
        html_source = f.read()
    soup = BeautifulSoup(html_source, 'html.parser')
    link_array.append(soup.find_all("a", attrs={"data-action": "clickYear"})[0]["href"])

print "files read"

for item in link_array:
    item = item.split("=")
    ids = item[2].split("+")
    print len(ids)
    for a in ids:
        id_array.append(a)

print "ids: {}".format(len(id_array))

# Write plain list
with open("id_results.txt", "w") as f:
    for item in id_array:
        f.write(item + "\n")
print "txt written"

# Write link list of csv
with open("id_results.csv", "w") as f:
    for item in id_array:
        f.write("http://www.movescount.com/move/export?id=" + item + "&format=fit" + "\n")
print "csv written"

