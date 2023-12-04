from bs4 import BeautifulSoup
import requests
import pandas as pd

'''
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

soup = BeautifulSoup(html, 'html5lib')
# print(soup.prettify())

title_obj = soup.title
# print('title obj:', title_obj)
# print('title obj type:', type(title_obj))

h3_obj = soup.h3
print('h3 obj:', h3_obj)
# print('h3 obj type:', type(h3_obj))
h3_child_obj = h3_obj.b
# print('h3 child:', h3_child_obj)
# print('h3 child parent:', h3_child_obj.parent)
# print(h3_child_obj.attrs)
# print(h3_child_obj.get('id'))
string = h3_child_obj.string
print(string)
print(type(string))
unicode_string = str(string)
print('unicode_string:', unicode_string)



table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"

table_bs = BeautifulSoup(table, 'html5lib')

table_rows = table_bs.find_all('tr')
# print(table_rows)
first_row = table_rows[0]
# print('first row: ', first_row)
# print('type first row: ', type(first_row))


for i, row in enumerate(table_rows):
    print('row: ', i)
    cells = row.find_all('td')
    for j,cell in enumerate(cells):
        print('column', j, 'is', cell)


list_input = table_bs.find_all(name=['tr', 'td'])
print(list_input)



url = 'http://www.ibm.com'
data = requests.get(url).text
soup = BeautifulSoup(data, 'html5lib')

for link in soup.find_all('a', href = True):
    print(link.get('href'))
'''


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

tables = pd.read_html(url) # using pandas turn table to a list of dataframe from web page
print(tables)