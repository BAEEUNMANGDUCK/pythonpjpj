from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text


soup = BeautifulSoup(yc_web_page, "html.parser")

article_tag = soup.select(selector=".titleline a")
# print(titles)

upvotes = soup.find_all(name="span", class_="score")
# print(upvotes)

article_subjects = [title.getText() for title in article_tag[::2]]
article_links = [title.get("href") for title in article_tag[::2]]
article_upvotes = [int(upvote.getText().split(" ")[0]) for upvote in upvotes]

# print(article_subjects)
# print(article_links)
# print(article_upvotes)

# 가장 추천수가 많은 기사의 제목, 링크, 점수 출력
all_about_article = sorted([[sub, links, score] for sub, links, score in zip(
    article_subjects, article_links, article_upvotes)], key=lambda x: x[2])
print(f"subject: {all_about_article[-1][0]}")
print(f"link: {all_about_article[-1][1]}")
print(f"score: {all_about_article[-1][2]}")
