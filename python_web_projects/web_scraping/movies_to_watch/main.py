from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.encoding = "utf-8"
movie_ranking_webpage = response.text
soup = BeautifulSoup(movie_ranking_webpage, "html.parser")

movie_titles = soup.find_all(name="h3", class_="title")

with open ("movies.txt", "w", encoding="utf-8") as file:
    for titles in movie_titles[::-1]:
        file.write(f"{titles.getText()}\n")