import yfinance as yf
from fastapi import FastAPI

app = FastAPI()

@app.get('/ns/{Stock}')
def get_info(Stock : str):
    stock = yf.Ticker(Stock + ".NS")
    data = stock.info

    return {"Name" : data['longName'] , "Total Revenue" : data['totalRevenue'] , "Revenue per Share" : data['revenuePerShare'] , "Revenue Growth" : data['revenueGrowth'] , "Gross Profits" : data['grossProfits'] , "TwoHundred Day Average Change" : data['twoHundredDayAverageChange'] , "Regular Market Price" : data['regularMarketPrice']}

@app.get('/ns/suggest/{Stock}')
def get_market(Stock : str):
    stock = yf.Ticker(Stock + ".NS")
    data = stock.analyst_price_targets

    if data['current'] < data['median']:
        return {"Current Price" : data['current'] , "Suggestion" : "Buy..I will buy the Stock if I were in your Situation" , "note" : "suggestions are made based on comparing median price of the stock"}
     
    return {"Current Price" : data['current'] , "Suggestion" : "Wait..I will Wait until the Stock price moves down if I were in your Situation" , "note" : "suggestions are made based on comparing median price of the stock"}
