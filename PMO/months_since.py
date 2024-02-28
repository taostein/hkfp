
import sys
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# function to add value labels
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center', va = 'bottom')

months = np.array(["2020-Jan", "2020-Feb", "2020-Mar", "2020-Apr", 
                   "2020-May", "2020-Jun", "2020-Jul", "2020-Aug",
                   "2020-Sep", "2020-Oct", "2020-Nov", "2020-Dec",
                   "2021-Jan", "2021-Feb", "2021-Mar", "2021-Apr", 
                   "2021-May", "2021-Jun", "2021-Jul", "2021-Aug",
                   "2021-Sep", "2021-Oct", "2021-Nov", "2021-Dec",
                   "2022-Jan", "2022-Feb", "2022-Mar", "2022-Apr", 
                   "2022-May", "2022-Jun", "2022-Jul", "2022-Aug",
                   "2022-Sep", "2022-Oct", "2022-Nov", "2022-Dec",
                   "2023-Jan", "2023-Feb", "2023-Mar", "2023-Apr", 
                   "2023-May", "2023-Jun", "2023-Jul", "2023-Aug",
                   "2023-Sep", "2023-Oct", "2023-Nov", "2023-Dec",
                   "2024-Jan", "2024-Feb"])
count = np.array([
                  0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0])

data = pd.read_csv(sys.argv[1],header=None)
column_name = ['Event Name', 'Date', 'Years', 'Time of Day', 'Gender']
data.columns = column_name

# loop through the case date for the months
dates = data.loc[:, 'Years']

n = len(dates)

i = 0
while i < n:
    if (type(dates[i]) == float and math.isnan(dates[i])):
        i = i + 1
        continue
    x = dates[i].split("-")
    if (len(x) < 2):
        i = i + 1
        continue
    year = x[0]
    month = x[1]
    if (int(year) < 2020):
        i = i + 1
        continue
    print(dates[i] + " has year of " + year + " and " + " month of " + month)
    index = ((int(year) - 2020) * 12) + (int(month)-1)
    print("index = " + str(index))
    count[index] = count[index] + 1
    i = i + 1

plt.title(sys.argv[2])
plt.xticks(rotation=90)

plt.bar(months, count)
addlabels(months, count)

plt.show()

