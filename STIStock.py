import streamlit as st
import yfinance as yf
import pandas as pd
import Functions
import time

st.title('STI Stock Analysis')

st.sidebar.header('Types of Analysis')

#bollinger
#if st button true
button1 = st.sidebar.button('Bollinger Analysis')

#if button is True:
if button1:
    with st.spinner('Fetching Data...'):
        result = Functions.bollinger()
        time.sleep(5)
    st.write('Bollinger Done!')



button2 = st.sidebar.button('RSI Analysis')
if button2:
    with st.spinner('Fetching Data...'):
        result = Functions.rsical()
        st.write('Status: RSI Analysis Done!')

#MA Analysis Button
button3 = st.sidebar.button('MA Analysis')
if button3:
   with st.spinner('Fetching Data...'):
       result = Functions.MA()
       st.write('Status: MA Analysis Done!git pull --allow-unrelated-histories  ')

#printing the currentbuylist
st.subheader('Current Buy/sell List')
st.write('Buy')

currentbuy = Functions.get_list('currentbuy.txt')
currentsell = Functions.get_list('currentsell.txt')

placeholder1 = st.empty()
with placeholder1.container():
    for items in currentbuy:
        st.write(items)

#printing the currentselllist
st.write('Sell')
placeholder2=st.empty()
with placeholder2.container():
    for items in currentsell:
        st.write(items)

#clearcurrentlist
if st.button('Clear current list'):
    f = open('currentbuy.txt',"w")
    f = open('currentsell.txt', "w")
    placeholder1.empty()
    placeholder2.empty()
    f.close()

#add to record
placeholder3 = st.empty()
with placeholder3.container():
    if st.button('Add to records'):
        #read current list and append to buy.txt
        currentbuyitems = Functions.get_list('currentbuy.txt')
        for item in currentbuyitems:
            newbuylist = Functions.write_file(item, filepath='buy.txt')

        currentsellitems = Functions.get_list('currentsell.txt')
        for item in currentsellitems:
            newselllist = Functions.write_file(item, filepath = 'sell.txt')

        #open updated buy/sell.txt and print
        st.subheader('Buy List:')
        buy = Functions.get_list('buy.txt')
        st.write(time.strftime('%d-%m-%Y'))
        for items in buy:
            st.write(items)

        st.subheader('Sell list:')
        sell = Functions.get_list('sell.txt')
        st.write(time.strftime('%d-%m-%Y'))
        for items in sell:
            st.write(items)



st.session_state