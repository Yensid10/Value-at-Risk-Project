import datetime as dt
import numpy as np
from scipy.stats import norm
import yfinance as yf

# print(100000000 - 100000000*(norm.ppf(0.05, 0.00036, 0.0126) + 1))
#This appears to work for variance - covariance VAR

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
    print(round(VaR, 3))
    