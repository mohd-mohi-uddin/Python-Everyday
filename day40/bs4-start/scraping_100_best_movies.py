from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0"
}


response = requests.get(url ="https://www.empireonline.com/movies/features/best-movies-2/",headers=headers)
response.raise_for_status()
contents = response.text

soup = BeautifulSoup(contents,"html.parser")
movie_name = [movie.getText() for movie in soup.select(".content_content__i0P3p > h2 > strong")]
movie_name.remove(movie_name[0])
movies_name = movie_name[::-1]
for movie in movies_name:
    with open("best_movies.txt", mode="a") as file:
        file.write(f"{movie}\n")
