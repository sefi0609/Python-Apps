import requests
from send_email import send_email
from datetime import datetime, timedelta

# get yesterday date
presentday = datetime.now()  # or presentday = datetime.today()
yesterday = presentday - timedelta(1)
date = yesterday.strftime('%Y-%m-%d')

# language=en - for news in english only
# get dynamic topics and news from yesterday
url = 'https://newsapi.org/v2/everything?' \
      f'domains=wsj.com&' \
      f'from={date}&' \
      'sortBy=publishedAt&' \
      'apiKey={ENTER YOUR API KEY}' \
      'language=en'

# make request
response = requests.get(url)
content = response.json()
message = 'Subject: Daily News\n'

# get the first 20 articles
for article in content['articles'][:20]:
    if article['title'] is not None:
        message += f"""
        Title: {article['title']}
        Description: {article['description']}
        Link: {article['url']}
        ----------------------------------------
        """

# need to encode the message before sending it
send_email(message.encode('utf-8'))
