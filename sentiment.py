url = "https://www.amazon.in/Test-Exclusive-746/product-reviews/B07DJHXTLJ/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

import requests   ### load the url
from bs4 import BeautifulSoup  ### web scraping

page = requests.get(url)
page

page.content

soup = BeautifulSoup(page.content,'html.parser')
print(soup.prettify())

names = soup.find_all('span',class_='a-profile-name')[2:]
names

len(names)

cust_name = []
for i in range(0,len(names)):
  cust_name.append(names[i].get_text())

cust_name

stars = soup.find_all('span',class_='a-icon-alt')[3:]
stars

len(stars)

cust_rating = []
for i in range(0,len(stars)):
  cust_rating.append(stars[i].get_text())
cust_rating

title = soup.select('a.review-title span')
title

len(title)

rev_title = []
for i in range(0,len(title)):
  rev_title.append(title[i].get_text())
rev_title

dates = soup.select('span.review-date')[2:]
dates

len(dates)

rev_date = []
for i in range(0,len(dates)):
  rev_date.append(dates[i].get_text())
rev_date

details = soup.select('span.review-text-content span')
details

len(details)

rev_body = []
for i in range(0,len(details)):
  rev_body.append(details[i].get_text())
rev_body

import pandas as pd
df = pd.DataFrame()
df["Date"] = rev_date
df["Customer Name"] = cust_name
df['Ratings'] = cust_rating
df["Review Title"] = rev_title
df['Reviews'] = rev_body

df

df.to_csv("reviews.csv")
##### Sentiment Analysis
import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

sia.polarity_scores("This moview was really the best movie of my life")

rev_body

polarity_scores = []
for i in range(0,len(rev_body)):
  s = sia.polarity_scores(rev_body[i])
  polarity_scores.append(s) 

polarity_scores

polarity_scores[0]['compound']

score = []
for i in range(0,len(polarity_scores)):
  c = polarity_scores[i]['compound']
  if c > 0:
    score.append("Positive")
  elif c == 0:
    score.append("Neutral")
  else:
    score.append("Negative")

score

df['Score'] = score
df

