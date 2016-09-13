**********************************HOMEWORK 2******************************

NAME: JANANI NEELAKANTAN
UIN: 670805407

The p2 folder contains the following:
1)transform.py
2)result.csv
3)README

How to run
python3 transform.py

Installation
BeautifulSoup - pip3 install bs4

Solution:
The source HTML is parsed using BeautifulSoup

1)From the parsed file, first all tables with the class 'wikitable sortable' are extracted.
2)In the extracted list, the table with index 1 is considered which is the required table.
3)All tr tags are extracted.
4)For each tr tag, all the td tags are extracted. This is to extract details of each row.
5)Now for each row, based on properties of the html element required, extraction is done. 
6)Result is written to csv file.


