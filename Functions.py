import yfinance as yf
import pandas as pd

def get_stocks():
    STI_watchlist = ['C52.SI', '9CI.SI', 'BUOU.SI', 'ME8U.SI', 'C38U.SI', 'M44U.SI', 'O39.SI', 'U14.SI', 'D05.SI',
                     'A17U.SI', 'Z74.SI', 'D01.SI', 'BN4.SI', 'S63.SI', 'U96.SI', 'S68.SI', 'V03.SI', 'S58.SI',
                     'Y92.SI', 'C07.SI', 'C09.SI', 'N2IU.SI', 'H78.SI', 'F34.SI', 'J36.SI', 'YF8.SI', 'G13.SI', 'AJBU.SI',
                     'BS6.SI']


def get_buy(filepath = 'buy.txt'):
    with open(filepath, 'r') as f:
        buy = f.readlines()
        return buy

def get_sell(filepath = 'sell.txt'):
    with open(filepath, 'r') as f:
        buy = f.readlines()
        return buy
#not sure if will have problems because adding to buy and sell list uses same function
def write_file(buy_arg, filepath):
    with open(filepath, 'a') as f:
        f.writelines(buy_arg + ', ')

