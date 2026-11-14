import requests as re
import pandas as pd

r = re.get("https://hacker-news.firebaseio.com/v0/topstories.json")

titles = []
scores = []




for i in range(5):
   article = re.get(f"https://hacker-news.firebaseio.com/v0/item/{r.json()[i]}.json")
   title = article.json()['title']
   score = article.json()['score']
   titles.append(title)
   scores.append(score)
   print(f"""Article number {i+1} with title "{title}" and a score of {score}""")



