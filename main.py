from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.premierleague.com/results?co=1&se=418&cl=-1').text
soup = BeautifulSoup(html, 'lxml')

match_date = soup.find('time', class_='date long')
print(match_date)
