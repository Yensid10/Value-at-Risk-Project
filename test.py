import csv
import numpy as np

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
for i in range(2, len(closes)): 
    diffs = np.append(diffs, (closes[i]/closes[i-1] - 1))
# print(round(np.partition(diffs, 24)[24], 3))
print(round(np.partition(diffs, 24)[24]*100000000, 3))

