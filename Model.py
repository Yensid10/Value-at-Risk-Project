import datetime as dt
import numpy as np
from scipy.stats import norm
import yfinance as yf

# print(100000000 - 100000000*(norm.ppf(0.05, 0.00036, 0.0126) + 1))
#This appears to work for variance - covariance VAR

print("Model Building VaR\n")
def dailyVar(P, rl, mean, sD):
    return P - P*(norm.ppf(rl, mean, sD) + 1)

if __name__ == "__main__":
    startDate = dt.datetime(2021, 10, 26)
    endDate = dt.datetime(2023, 10, 24)

    #format              year, month, day
    
    stock = yf.download('NKE', startDate, endDate)
    # print(stock)
    closeDiffs = stock['Adj Close'].pct_change()
    
    portfolio = 100000000
    rlPercent = 0.05
    mean = np.mean(closeDiffs)
    sD = np.std(closeDiffs)
    
    VaR = dailyVar(portfolio, rlPercent, mean, sD)
    print("500 Day stock history, for 1 day time horizon, 95% certainty, Portfolio of 100,000,000, VaR for the 23/10/2023: £" + str(round(VaR, 3)))
    
    count = 0
    for i in range(1, len(stock) - 100):
        backtest = np.array([])
        backtest = stock['Adj Close'].pct_change()[i:i+100]
        VaR = dailyVar(portfolio, rlPercent, np.mean(backtest), np.std(backtest))
        day = stock['Adj Close'].pct_change()[i+100:i+101].values[0]
        if VaR*-1 > (day*portfolio): #Needs to be multiplied by -1 as VaR is a predicted loss
            count += 1
    print("Backtest for 100-day rolling window of 500 Day stock history, at 95% certainty: " + str(round(count/(len(stock)-100)*100, 1)) + "%")
    