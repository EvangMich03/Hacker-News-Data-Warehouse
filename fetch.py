import requests as re
import pandas as pd
import psycopg2 as psy
from dotenv import dotenv_values
import datetime
import json

r = re.get("https://hacker-news.firebaseio.com/v0/topstories.json")

titles = []
scores = []


conn = psy.connect(
    host="localhost",
    port="5432",
    dbname="postgres",
    user="postgres",
    password=dotenv_values()["dbpassword"],
)

cur = conn.cursor()


for i in range(100):
   article = re.get(f"https://hacker-news.firebaseio.com/v0/item/{r.json()[i]}.json")

   title = article.json().get('title')
   title = title.replace("'","''")
   score = article.json().get('score')
   json_dump = json.dumps(article.json())
   json_dump = str(json_dump.replace("'","''")) 

   titles.append(title)
   scores.append(score)

   sql_stories = """
    INSERT INTO stories (id, title, author, score, created_at, url)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON CONFLICT (id) DO UPDATE SET
        score = EXCLUDED.score,
        created_at = EXCLUDED.created_at,
        url = EXCLUDED.url;
"""

   values = (
    article.json().get("id"),
    article.json().get("title"),
    article.json().get("by"),
    article.json().get("score"),
    datetime.datetime.fromtimestamp(article.json()['time']),
    article.json().get("url"),
)




   sql_raw_times = """INSERT INTO raw_times (item_id,fetched_at,payload) 
   VALUES(%s,%s,%s) 
   ON CONFLICT(item_id) DO UPDATE SET payload = EXCLUDED.payload"""


   values_raw = (
      article.json().get("id"),
      datetime.datetime.fromtimestamp(article.json()['time']),
      json_dump
   )

   cur.execute(sql_stories, values)
   cur.execute(sql_raw_times, values_raw) 

conn.commit() 
conn.close()

