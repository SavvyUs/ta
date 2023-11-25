
from email.utils import decode_rfc2231
import pandas as pd 
import numpy 
import matplotlib.pyplot as plt 
import cufflinks as cf 
import yfinance as yf 
import pandas_datareader
import plotly.graph_objects as go
import plotly

def generate_simple_linear_chart(start, end, symbols) :

    colors = ['b','g','r','c','m','y','k']

    df = yf.download(tickers=symbols, start=start, end=end)

    df.to_csv("stocks.csv")

    df = pd.read_csv("stocks.csv", header=[0,1], index_col = 0, parse_dates = [0])
    index = 0 

    fig, axs = plt.subplots(1, len(symbols), figsize=(30,5))

    for ticker in symbols :
        # print(f"{ticker}, {len(symbols)}, {index}, {df["Close"]}")
        if len(symbols) == 1 : 
            df["Close"].plot(ax=axs, color=colors[index%len(symbols)])
        else : 
            df["Close"][ticker].plot(ax=axs[index], color=colors[index%len(symbols)])
        
        index += 1
    # gcf(): get the current figure    
    return plt.gcf() 
    
def generate_interactive_linear_chart(start, end, symbols) : 

    setattr(plotly.offline, "__PLOTLY_OFFLINE_INITIALIZED", True)    

    df = yf.download(tickers=symbols, start=start, end=end)

    df.to_csv("stocks.csv")

    df = pd.read_csv("stocks.csv", header=[0,1], index_col = 0, parse_dates = [0])
    index = 0 

    cf.set_config_file(offline = True)

    # figure = go.Figure(data=df.loc["2020-06":, ("Close", symbols)])

    #  df1 = df.loc["2020-06":, ("Close", symbols)]         

    # df1.iplot()
    df.Close.iplot(fill = True, colorscale = "rdylbu", theme = "solar")
    # return plt.gcf()


def delete_figure(figure) : 
    figure.get_tk_widget().forget()
    plt.close('all')    


# Unit test  
if __name__ == "__main__" : 
    start='2020-06-01'
    end='2022-12-31'
    symbols=["PLTR","ACAD","GE"]
    generate_interactive_linear_chart(start, end, symbols)
    
    # start='2010-01-01'
    # end='2022-12-31'
    # symbols=["MSFT"]
    # generate_simple_linear_chart(start, end, symbols)