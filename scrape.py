from bs4 import BeautifulSoup
import requests

HEADERS = ({'User-Agent':
              'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
              'Accept-Language': 'en-US'})

URL = "https://play.google.com/store/search?q=subway+surfers&c=apps"

webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "lxml")
titles = soup.find_all("span", attrs={"class": 'DdYX5'})
ratings = soup.find_all("span", attrs={"class": 'w2kbF'})

name_list = []
rating_list = []
print("All of the games in this search are:\n")
for title in titles:
    try:
        name_list.append(title.string.strip())
        print(f"- {title.string.strip()}")
    except:
        print()

for rating in ratings:
    try:
        rating_list.append(rating.string.strip())
    except:
        print()

highest_rating = [rating_list[0], 0]
for i in range(len(rating_list)):
    if (rating_list[i] > highest_rating[0]):
        highest_rating = [rating_list[i], i]

print(f"\nThe highest rated game is {name_list[highest_rating[1]]} with a rating of {highest_rating[0]}\n")