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


url = 'https://www.alphavantage.co/query'
r = requests.get(url,params=Stock_Parameters)
data = r.json()
data_list=[value for (key,value) in data['Time Series (Daily)'].items()]
print(data_list)

yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data['4. close']

day_before_yesterday=data_list[1]
day_before_yesterday_closing_price=day_before_yesterday['4. close']

difference=abs(float(yesterday_closing_price)-float(day_before_yesterday_closing_price))
print(difference)

difference_percent=(difference/float(yesterday_closing_price))*100
print(difference_percent)

def Get_news():
    if difference_percent>4:
        url_news = 'https://newsapi.org/v2/everything'
        r_news = requests.get(url_news, params=News_Parameters)
        articles = r_news.json()['articles']

        three_articles = articles[:3]

        formatted_articles = [f"Headlines: {article['title']}\nBrief: {article['description']}" for article in
                              three_articles]

        account_sid = "ACa3305e5e0e5d40f8a36f2758788cf4b8"
        auth_token = "885b105c913ab2bffa189164409b64ad"

        client = Client(account_sid, auth_token)
        for article in formatted_articles:
            message = client.messages.create(
                body=article,
                from_='+15076045786',
                to='+919501929416'
            )
    else:
        pass


Get_news()


