#original

import yfinance as yf
import pandas as pd


STI_dict = {'C6L.SI': ['Singapore Airlines','https://sg.finance.yahoo.com/quote/C6L.SI?p=C6L.SI&.tsrc=fin-srch'],
                '9CI.SI': ['CapitaLand Investment Limited', 'https://sg.finance.yahoo.com/quote/9CI.SI?p=9CI.SI&.tsrc=fin-srch'],
                'BUOU.SI': ['Frasers Logistics & Commercial Trust','https://sg.finance.yahoo.com/quote/BUOU.SI?p=BUOU.SI&.tsrc=fin-srch'],
                'ME8U.SI': ['Mapletree Industrial Trust','https://finance.yahoo.com/quote/ME8U.SI?p=ME8U.SI&.tsrc=fin-srch'],
                'C38U.SI': ['CapitaLand Integrated Commercial Trust','https://finance.yahoo.com/quote/C38U.SI?p=C38U.SI&.tsrc=fin-srch'],
                'M44U.SI': ['Mapletree Logistics Trust', 'https://finance.yahoo.com/quote/M44U.SI?p=M44U.SI&.tsrc=fin-srch'],
                'O39.SI': ['OCBC', 'https://finance.yahoo.com/quote/O39.SI?p=O39.SI&.tsrc=fin-srch'],
                'U14.SI': ['UOL Group Limited', 'https://finance.yahoo.com/quote/U14.SI?p=U14.SI&.tsrc=fin-srch'],
                'D05.SI': ['DBS', 'https://finance.yahoo.com/quote/D05.SI?p=D05.SI&.tsrc=fin-srch'],
                'A17U.SI': ['CapitaLand Ascendas REIT', 'https://finance.yahoo.com/quote/A17U.SI?p=A17U.SI&.tsrc=fin-srch'],
                'Z74.SI' : ['Singtel', 'https://finance.yahoo.com/quote/Z74.SI?p=Z74.SI&.tsrc=fin-srch'],
                'D01.SI' : ['DFI Retail Group Holdings Limited','https://finance.yahoo.com/quote/D01.SI?p=D01.SI&.tsrc=fin-srch'],
                'BN4.SI' : ['Keppel Corporation', 'https://finance.yahoo.com/quote/BN4.SI?p=BN4.SI&.tsrc=fin-srch'],
                'S63.SI':  ['Singapore Technologies Engineering Ltd', 'https://finance.yahoo.com/quote/S63.SI?p=S63.SI&.tsrc=fin-srch'],
                'U96.SI':  ['Sembcorp', 'https://finance.yahoo.com/quote/U96.SI?p=U96.SI&.tsrc=fin-srch'],
                'S68.SI': ['SGX', 'https://finance.yahoo.com/quote/S68.SI?p=S68.SI&.tsrc=fin-srch'],
                'V03.SI': ['Venture Corp', 'https://finance.yahoo.com/quote/V03.SI?p=V03.SI&.tsrc=fin-srch'],
                'S58.SI': ['SATS', 'https://finance.yahoo.com/quote/S58.SI?p=S58.SI&.tsrc=fin-srch'],
                'Y92.SI': ['Thai Beverage', 'https://finance.yahoo.com/quote/Y92.SI?p=Y92.SI&.tsrc=fin-srch'],
                'C07.SI': ['Jardine Cycle & Carriage', 'https://finance.yahoo.com/quote/C07.SI?p=C07.SI&.tsrc=fin-srch'],
                'C09.SI': ['City Developments', 'https://finance.yahoo.com/quote/C09.SI?p=C09.SI&.tsrc=fin-srch'],
                'N2IU.SI': ['Mapletree Pan Asia Commercial Trust', 'https://finance.yahoo.com/quote/N2IU.SI?p=N2IU.SI&.tsrc=fin-srch'],
                'H78.SI': ['Hong Kong Land holdings', 'https://finance.yahoo.com/quote/H78.SI?p=H78.SI&.tsrc=fin-srch'],
                'F34.SI': ['Wilmar International', 'https://finance.yahoo.com/quote/F34.SI?p=F34.SI&.tsrc=fin-srch'],
                'J36.SI': ['Jardine Matheson Holdings Limited', 'https://finance.yahoo.com/quote/J36.SI?p=J36.SI&.tsrc=fin-srch'],
                'YF8.SI': ['Yangzijiang Financial Holding Ltd', 'https://finance.yahoo.com/quote/YF8.SI?p=YF8.SI&.tsrc=fin-srch'],
                'G13.SI': ['Genting', 'https://finance.yahoo.com/quote/G13.SI?p=G13.SI&.tsrc=fin-srch'],
                'AJBU.SI': ['Keppel DC REIT', 'https://finance.yahoo.com/quote/AJBU.SI?p=AJBU.SI&.tsrc=fin-srch'],
                'BS6.SI': ['Yangzijiang' 'https://finance.yahoo.com/quote/BS6.SI?p=BS6.SI&.tsrc=fin-srch']
                 }

def write_file(buy_arg,filepath):
    with open(filepath,'a') as f:
        f.writelines(buy_arg + ' ')

# write records
def get_list(filepath):
    with open(filepath, 'r') as f:
        buy = f.readlines()
        return buy


def bollinger():
    # header text
    textcurrentbuy1 = write_file('Bollinger:', 'currentbuy.txt')
    textcurrentsell1 = write_file('Bollinger:', 'currentsell.txt')

    for stockkey in STI_dict:

        data = yf.download(stockkey, period='1year')
        Closing = (data['Close'].values)

        stock_info = yf.Ticker(stockkey)
        stock_data = stock_info.history
        twentyma = (round(stock_info.history(period="20d", interval="1d").mean(), 2)['Close'])
        stddev = stock_info.history(period="20d", interval="1d")['Close'].std(ddof=0)
        topband = twentyma + 2 * stddev
        lowerband = twentyma - 2 * stddev

        if Closing > topband:
            selltext = f"\n {stockkey} - {STI_dict[stockkey][0]} [chart]({STI_dict[stockkey][1]})"
            sell2 = write_file(selltext,  filepath='currentsell.txt')


        if Closing < lowerband:
            buytext = f"\n {stockkey} - {STI_dict[stockkey][0]} [chart]({STI_dict[stockkey][1]})"
            buy2 = write_file(buytext,filepath='currentbuy.txt')

        else:
            pass
    add_line = write_file('\n', 'currentbuy.txt')
    add_line = write_file('\n', 'currentsell.txt')


def rsical():
    # header text
    textcurrentbuy2 = write_file('RSI:', 'currentbuy.txt')
    textcurrentsell2 = write_file('RSI:', 'currentsell.txt')
    for stockkey in STI_dict:
        rsi_period = 14
        data_df = yf.download(stockkey, period='1y')
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
            selltext = f"""\n {stockkey} - {STI_dict[stockkey][0]} [chart]({STI_dict[stockkey][1]})
            latest rsi = {latest_rsi}
            """
            sell2 = write_file(selltext, filepath='currentsell.txt')

        elif latest_rsi < 30:
            buytext = f"""\n {stockkey} - {STI_dict[stockkey][0]} [chart]({STI_dict[stockkey][1]})
            RSI = {latest_rsi}
            """
            buy2 = write_file(buytext, filepath='currentbuy.txt')


        else:
            pass
    add_line = write_file('\n', 'currentbuy.txt')
    add_line = write_file('\n', 'currentsell.txt')
def MA():
    #header text
    textcurrentbuy3 = write_file('MA:', 'currentbuy.txt')
    textcurrentsell3 = write_file('MA:', 'currentsell.txt')

    for stockkey in STI_dict:
        stock_info = yf.Ticker(stockkey)
        stock_data = stock_info.history
        fiftyMA = round(stock_info.history(period="50d", interval="1d").mean(), 2)
        twentyMA = round(stock_info.history(period="20d", interval="1d").mean(), 2)

        if (twentyMA['Close'])> (fiftyMA['Close']):
            buytext = (f"\n {stockkey} - {STI_dict[stockkey][0]} [chart]({STI_dict[stockkey][1]})")
            buy2 = write_file(buytext, filepath='currentbuy.txt')

        elif (twentyMA['Close']) < (fiftyMA['Close']):
            selltext = (f"\n {stockkey} - {STI_dict[stockkey][0]} [chart]({STI_dict[stockkey][1]})")
            sell2 = write_file(selltext, filepath='currentsell.txt')
        else:
            pass

    add_line = write_file('\n', 'currentbuy.txt')
    add_line = write_file('\n', 'currentsell.txt')




