import requests
from bs4 import BeautifulSoup

# url = "https://www.bbc.com/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# posts = soup.find_all('a', class_="media__link")
#
# print("Today's BBC Headlines:")
# for post in posts:
#     print(post.text)


url = "https://www.npr.org/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
posts = soup.find_all('h3', class_="title")

print("\nToday's NPR Headlines:")
for post in posts:
    print(post.text)

url = "https://huntnewsnu.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
posts = soup.find_all('a', class_="homeheadline")

print("\nTrending stories from Huntington News:")
counter = 0
for post in posts:
    counter += 1
    if counter != 21:
        print(post.text)
    else:
        break
