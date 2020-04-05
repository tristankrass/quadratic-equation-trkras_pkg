"""Get all quantine information to text file."""
import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://www.ttu.ee/students/university-facilities/canteen/'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
# article = soup()
article = soup.find("div", {"class": "article"}).table

tds = article.find_all("td")


headers = []
rows = []

for i in range(len(tds)-2):
    if i < 3:
        headers.append(tds[i].text)
    else:
        rows.append({headers[0]: tds[i].text, headers[1]: tds[i+1]., headers[2]: tds[i+2]})
        i+=2

with open('cuantines.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
