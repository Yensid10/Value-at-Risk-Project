import csv
import numpy as np

print("Historical Simulation VaR\n")
closes = np.array([])
with open('NKE.csv', 'r') as file:
    reader = csv.reader(file)
    flag = True
    for row in reader:
        if flag:
            flag = False
            continue
        closes = np.append(closes, float(row[5]))
        
# print(closes)
diffs = np.array([])
for i in range(1, len(closes)): 
    diffs = np.append(diffs, (closes[i]/closes[i-1] - 1))
# print(round(np.partition(diffs, 24)[24], 3))
print("500 Day stock history, for 1 day time horizon, 95% certainty, Portfolio of 100,000,000, VaR for the 23/10/2023: £" + str(round(np.partition(diffs, 24)[24]*100000000*-1, 3)))

count = 0
for i in range(1, len(closes) - 100):
    backtest = np.array([])
    for x in range(i, i + 100):
        backtest = np.append(backtest, (closes[x]/closes[x-1] - 1))
    VaR = np.partition(backtest, 4)[4]
    if VaR > ((closes[x+1]/closes[x] - 1)):
        # print(str(VaR) + " " + str((closes[x+1]/closes[x] - 1)*100000000))
        count += 1
print("Backtest for 100-day rolling window of 500 Day stock history, at 95% certainty: " + str(round(count/(len(closes)-100)*100, 1)) + "%")