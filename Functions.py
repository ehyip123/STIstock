import yfinance as yf
import pandas as pd
import streamlit as st
import time

STI_watchlist = ['C52.SI', '9CI.SI', 'BUOU.SI', 'ME8U.SI', 'C38U.SI', 'M44U.SI', 'O39.SI', 'U14.SI', 'D05.SI',
                     'A17U.SI', 'Z74.SI', 'D01.SI', 'BN4.SI', 'S63.SI', 'U96.SI', 'S68.SI', 'V03.SI', 'S58.SI',
                     'Y92.SI', 'C07.SI', 'C09.SI', 'N2IU.SI', 'H78.SI', 'F34.SI', 'J36.SI', 'YF8.SI', 'G13.SI', 'AJBU.SI',
                     'BS6.SI']

#not sure if will have problems because adding to buy and sell list uses same function
def write_file(buy_arg,filepath):
    with open(filepath,'a') as f:
        f.writelines(buy_arg + ' ')

#write records
def get_list(filepath):
    with open(filepath, 'r') as f:
        buy = f.readlines()
        return buy


def bollinger():
    # header text
    textcurrentbuy1 = write_file('Bollinger:', 'currentbuy.txt')
    textcurrentsell1 = write_file('Bollinger:', 'currentsell.txt')

    for stock in STI_watchlist:

        data = yf.download(stock, period='1year')
        Closing = (data['Close'].values)

        stock_info = yf.Ticker(stock)
        stock_data = stock_info.history
        twentyMA = (round(stock_info.history(period="20d", interval="1d").mean(), 2)['Close'])
        stddev = stock_info.history(period="20d", interval="1d")['Close'].std(ddof=0)
        topband = twentyMA + 2 * stddev
        lowerband = twentyMA - 2 * stddev

        if Closing > topband:
            sell2 = write_file(stock, filepath='currentsell.txt')

        if Closing < lowerband:
            buy2 = write_file(stock, filepath='currentbuy.txt')

        else:
            pass
    add_line = write_file('\n', 'currentbuy.txt')
    add_line = write_file('\n', 'currentsell.txt')


def rsical():
    # header text
    textcurrentbuy2 = write_file('RSI:', 'currentbuy.txt')
    textcurrentsell2 = write_file('RSI:', 'currentsell.txt')
    for stock in STI_watchlist:
        rsi_period = 14
        data_df = yf.download(stock, period='1y')
        data_df = pd.DataFrame(data_df['Close'])
        data_df.reset_index(inplace=True)
        # find out whats the difference in closing price
        change = data_df['Close'].diff(1)
        # hide those negative numbers
        gain = change.mask(change < 0, 0)
        data_df['gain'] = gain
        # hide positive numbers
        loss = change.mask(change > 0, 0)
        data_df['loss'] = loss

        avg_gain = gain.ewm(com=rsi_period - 1, min_periods=rsi_period).mean()
        data_df['avg_gain'] = avg_gain
        avg_loss = loss.ewm(com=rsi_period - 1, min_periods=rsi_period).mean()
        data_df['avg_loss'] = avg_loss

        relativestrength = abs(avg_gain) / abs(avg_loss)
        rsi = 100 - (100 / (1 + relativestrength))
        data_df['rsi'] = rsi

        latest_rsi = round(data_df.iloc[-1, -1], 2)
        #print(stock, latest_rsi)

        if latest_rsi > 70:
            sell2 = write_file(stock, filepath='currentsell.txt')

        elif latest_rsi < 30:
            buy2 = write_file(stock, filepath='currentbuy.txt')


        else:
            pass
    add_line = write_file('\n', 'currentbuy.txt')
    add_line = write_file('\n', 'currentsell.txt')
def MA():
    #header text
    textcurrentbuy3 = write_file('MA:', 'currentbuy.txt')
    textcurrentsell3 = write_file('MA:', 'currentsell.txt')

    for stock in STI_watchlist:
        stock_info = yf.Ticker(stock)
        stock_data = stock_info.history
        fiftyMA = round(stock_info.history(period="50d", interval="1d").mean(), 2)
        twentyMA = round(stock_info.history(period="20d", interval="1d").mean(), 2)

        if (twentyMA['Close'])> (fiftyMA['Close']):
            buy2 = write_file(stock, filepath='currentbuy.txt')

        elif (twentyMA['Close']) < (fiftyMA['Close']):
            sell = write_file(stock, filepath='currentsell.txt')
        else:
            pass

    add_line = write_file('\n', 'currentbuy.txt')
    add_line = write_file('\n', 'currentsell.txt')