import streamlit as st
import yfinance as yf
import pandas as pd
import Functions
import time

STI_watchlist = ['C52.SI', '9CI.SI', 'BUOU.SI', 'ME8U.SI', 'C38U.SI', 'M44U.SI', 'O39.SI', 'U14.SI', 'D05.SI',
                     'A17U.SI', 'Z74.SI', 'D01.SI', 'BN4.SI', 'S63.SI', 'U96.SI', 'S68.SI', 'V03.SI', 'S58.SI',
                     'Y92.SI', 'C07.SI', 'C09.SI', 'N2IU.SI', 'H78.SI', 'F34.SI', 'J36.SI', 'YF8.SI', 'G13.SI', 'AJBU.SI',
                     'BS6.SI']

#codes for bollinger

def bollinger():
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
            sell = Functions.write_file('*' + stock,filepath = 'sell.txt')

        if Closing < lowerband:
            buy = Functions.write_file('*' + stock,filepath = 'buy.txt')

        else:
            pass

bollinger()


#codes for rsi
def rsical():
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

        if latest_rsi > 60:
            sell = Functions.write_file('/'+ stock, 'sell.txt')

        elif latest_rsi < 32:
            buy = Functions.write_file('/'+ stock, 'buy.txt')

        else:
            pass

rsical()

# buy if 20MA>50MA
def MA():
    for stock in STI_watchlist:
        stock_info = yf.Ticker(stock)
        stock_data = stock_info.history
        fiftyMA = round(stock_info.history(period="50d", interval="1d").mean(), 2)
        twentyMA = round(stock_info.history(period="20d", interval="1d").mean(), 2)

        if (twentyMA['Close'])> (fiftyMA['Close']):
            buy = Functions.write_file(stock, 'buy.txt')

        elif (twentyMA['Close']) < (fiftyMA['Close']):
            sell = Functions.write_file(stock, 'sell.txt')
        else:
            pass
MA()


st.write('MA buy list:')
buy = Functions.get_buy('buy.txt')
st.write(time.strftime('%d-%m-%Y'))
for items in buy:
    st.write(items)

st.write('MA sell list:')
sell = Functions.get_sell('sell.txt')
st.write(time.strftime('%d-%m-%Y'))
for items in sell:
    st.write(items)

st.session_state