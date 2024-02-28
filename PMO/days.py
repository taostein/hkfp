
import sys
import math
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center', va = 'bottom')

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
count = [0, 0, 0, 0, 0, 0, 0]

data = pd.read_csv(sys.argv[1], header=None)
column_name = ['Event Name', 'Date', 'Years', 'Time of Day', 'Gender']
data.columns = column_name

dates = data.loc[:, 'Date']
n = len(dates)

i = 0
while i < n:
    if (type(dates[i]) == float and math.isnan(dates[i])):
        i = i + 1
        continue
    x = dates[i].split("-")
    if (len(x) == 3):
        yy = x[0]
        mm = x[1]
        dd = x[2]
        dt = date(int(yy), int(mm), int(dd))
        x = dt.weekday()
        count[x] = count[x] + 1
    i = i + 1

plt.title(sys.argv[2])
plt.bar(days, count)
addlabels(days, count)
plt.show()

