from dotenv import load_dotenv
from os import getenv
import requests
from datetime import datetime, timedelta

load_dotenv()

URL_STOCK = "https://www.alphavantage.co/query"
FUNC = "TIME_SERIES_DAILY"
SYMBOL = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_STOCKS = getenv("API_KEY_STOCKS")

YESTERDAY = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
BEFORE_YESTERDAY = (datetime.now() - timedelta(2)).strftime('%Y-%m-%d')

URL_NEWS = "https://newsapi.org/v2/everything"
API_KEY_NEWS = getenv("API_KEY_NEWS")

def get_stock_change(ticker: str) -> float:
    r = requests.get(URL_STOCK, params={
        "function": FUNC,
        "symbol": ticker,
        "interval": "60min",
        "outputsize": "full",
        "apikey": API_KEY_STOCKS
    })

    r.raise_for_status()
    data = r.json()

    if data.get('Information') and "API rate limit" in data['Information']:
        return 10 #dummy

    yesterday_close = float(data['Time Series (Daily)'][YESTERDAY]['4. close'])
    before_yesterday_close = float(data['Time Series (Daily)'][BEFORE_YESTERDAY]['4. close'])
    return round((1 - (before_yesterday_close / yesterday_close)) * 100)

def get_news() -> str:
    r = requests.get(URL_NEWS, params={
        "q": COMPANY_NAME,
        "from": YESTERDAY,
        "sortBy": "popularity",
        "apiKey": API_KEY_NEWS
    })

    r.raise_for_status()
    data = r.json()

    return [{'title': x['title'], 'description': x['description']} for x in data['articles'][ : 3]]


diff = get_stock_change(SYMBOL)
up_or_down = '🔺' if diff > 0 else '🔻'
diff_visual = f"{up_or_down}{str(diff).strip('-')}%"

news_message = "###\n"
if (abs(diff) >= 5):
    news = get_news()
    for headline in news:
        news_message += f"Headline: {headline['title']}\nBrief: {headline['description']}\n###\n"

sms_template = f"""
{diff_visual}
{news_message}"""

print(sms_template)

from twilio.rest import Client

account_sid = getenv('ACCOUNT_SID')
auth_token = getenv('AUTH_TOKEN')
messaging_service_sid = getenv('MSG_SID')
phone_number = getenv('PHONE_NUMBER')

client = Client(account_sid, auth_token)
message = client.messages.create(
    messaging_service_sid=messaging_service_sid,
    body=sms_template,
    to=phone_number
)
print(message.sid)


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

