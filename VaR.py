import datetime as dt
import time
import numpy as np
from scipy.stats import norm
import yfinance as yf
import pandas as pd

ftse100 = pd.read_html('https://en.wikipedia.org/wiki/FTSE_100_Index')[4]


print("WELCOME TO THE VAR CALCULATOR\n-----------------------------\nWhich companies stock would you like to calculate the VaR for?")
for i in range(len(ftse100)):
    print(str(i+1) + " - " + ftse100['Company'][i])
    time.sleep(0.005)
while True:
    try:
        userInput = int(input("Enter the number of the company: "))-1
        if userInput > 0 and userInput < 100:
            break
        print("Please re-enter a valid input")
    except:
        print("Please re-enter a valid input")
                      
                      
    # userInput = input("What method would you like to use, Historical or Model Building?(H/M): ")
    # if (userInput == "H" or userInput == "h"):
        
    # elif (userInput == "M" or userInput == "m"):
        
    # else:
    #     print("Please enter a valid input")
    #     continue
