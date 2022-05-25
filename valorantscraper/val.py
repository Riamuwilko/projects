import requests
from bs4 import BeautifulSoup as bs

val_username = input('Input Valorant IGN without the tag (ex. Kise): ')
if ' ' in val_username:
    val_username.replace(" ","%20")
val_tag = input('Input the tag without the hastag (ex. Aznl): ').lower()
url = 'https://tracker.gg/valorant/profile/riot/' + val_username + '%23'+ val_tag + '/overview'
r = requests.get(url)
soup = bs(r.content, 'html.parser')
stats = soup.findAll('span', class_='stat__value')
rank = stats[0].text
kda = stats[1].text
statement = f"{val_username}#{val_tag}'s rank is {rank} and their kda is {kda}."
print(statement)



