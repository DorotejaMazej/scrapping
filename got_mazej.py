#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

# open or create CSV file
csv_file = open("got.csv", "w")

url = 'https://en.wikipedia.org/wiki/Game_of_Thrones'
response = urlopen(url).read()

soup = BeautifulSoup(response)
print soup.html.head.title.string

links = set()
for link in soup.findAll("a"):
    href = link.get('href')
    if href == None:
        continue
    elif '/wiki/Game_of_Thrones_(season_1)' in href:
        links.add(href)
for link in links:  #znotraj teh linkov
    s1 = link # je naš link

got_s1 = url + s1[-11:] # novi link = prejšnji url + naš link (samo zadnjih 11 simbolov)
new_response=urlopen(got_s1).read()

soup = BeautifulSoup(new_response)

table = soup.find("table", {"class" : "wikitable plainrowheaders wikiepisodetable"})

views = []

for row in table.findAll("tr"):
    cells = row.findAll("td")
    for cell in cells:
        c = cell.text
        print c
        if "[" and "]" in str(c):
            views.append(c[:4])

for view in views:
    print view




