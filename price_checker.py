import pandas as pd
import yfinance as yf
from datetime import date



def today_price(stock):
    thisday = date.today()
    data = yf.download(stock, start=thisday, end=thisday)
    return data

def price_checker(target_price,stock,higher = True):
    try:
        price = today_price(stock)['Close'][0]
    except KeyError:
        return [False,stock,'KeyError']
    except IndexError:
        return [False,stock,"Can't find the stock"]

    if higher:
        print(stock)
        if price > float(target_price):
            return True, stock, target_price, price
        else:
            return False, stock, target_price, price

    if not higher:
        if price < float(target_price):
            return True, stock, target_price, price
        else:
            return False, stock, target_price, price

def check_price(stocks,condition,target_price):
    if condition == '>':
        higher = True
    elif condition == '<':
        higher = False
    else:
        return 'Please enter the condition as > or <'
    result = []
    for stock in stocks:
        if price_checker(target_price,stock,higher)[0]:
            result.append(price_checker(target_price,stock,higher))
    if result[0][0]:
        return f'now reaching!  {result[0][1]} price {condition} {target_price}  '
    else:
        return