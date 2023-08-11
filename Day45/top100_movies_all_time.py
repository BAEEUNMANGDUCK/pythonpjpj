import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)

website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

titles = soup.find_all(name="h3", class_="title")


movie_titles = [title.getText() for title in titles][::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for title in movie_titles:
        file.write(f"{title}\n")
