import requests
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
from twilio.rest import Client

apid="6HO7BOEE8R6MFHR0"
apid_news="efbf00a14e3a4ddb9f6372b2977d2db8"

Stock_Parameters={
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'apikey':apid,
    }

News_Parameters={
'q':STOCK,
'from':'2025-06-20',
'apikey':apid_news,
}

url_news = 'https://newsapi.org/v2/everything'
r_news = requests.get(url_news, params=News_Parameters)
articles = r_news.json()['articles']

three_articles = articles[:3]

formatted_articles = [f"Headlines: {article['title']}\nBrief: {article['description']}" for article in
                      three_articles]