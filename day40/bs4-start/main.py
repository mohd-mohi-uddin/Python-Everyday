from bs4 import BeautifulSoup
import requests
# from pathlib import Path

# BASE_DIR = Path(__file__).parent

# with open(BASE_DIR/"website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents,"html.parser")


# heading = soup.find(name="h3",class_ ="heading")
# print(f'is this the {str(heading.get("class"))[2:9]}')

response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()
hn_web_page = response.text

soup = BeautifulSoup(hn_web_page,"html.parser")

article_tag = soup.select(".athing .title .titleline > a")
article_title = [title.getText() for title in article_tag]
article_link = [title.get("href") for title in article_tag]
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name ="span",class_ = "score")]
# print(article_title)
# print(article_link)
# print(article_upvote)

maximum_votes = max(article_upvote)
index_of_max_vote = article_upvote.index(maximum_votes)

title_with_max_votes = article_title[index_of_max_vote]
print(title_with_max_votes)

