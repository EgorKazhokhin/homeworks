import requests

response = requests.get("https://epam.com")
with open("response.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
divs = soup.find_all('div')
divs_count = len(divs)
print(divs_count)  # подсчёт количетсва тэгов div на сайте epam.com


import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''CREATE TABLE tablica
             (number, name)''')
c.execute("INSERT INTO tablica VALUES ('1','bob')")
c.execute("INSERT INTO tablica VALUES ('2','paul')")
c.execute("INSERT INTO tablica VALUES ('3','mary')")
conn.commit()
for row in c.execute('SELECT * FROM tablica'):
        print(row)  # создал таблицу с условиями из задания
