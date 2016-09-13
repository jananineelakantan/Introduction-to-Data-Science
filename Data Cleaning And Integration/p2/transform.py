from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

wikiSource = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"
sourcePage = urlopen(wikiSource)
sourceHTML = BeautifulSoup(sourcePage)

all_tables = sourceHTML.find_all("table", { "class" : "wikitable sortable" })
target_table = all_tables[1]

result_file = csv.writer(open("result.csv","w"))
result_file.writerow(["Game number","year","winning team","score","losing team","venue"])
for row in target_table.find_all("tr")[1:]:
        cells = row.findAll("td")
        game_number = cells[0].find("a").get_text()    
        year = cells[1].find_all("span")[1].get_text()[-4:]    
        winning_team = cells[2].find("span").get_text().strip('!')    
        score = cells[3].find_all("span")[1].get_text()    
        losing_team = cells[4].find("span", { "class" : "sortkey"}).get_text().strip('!')    
        venue = cells[5].find("span", { "class" : "sortkey"}).get_text().strip('!')
        result_file.writerow([game_number,year,winning_team,score,losing_team,venue])
