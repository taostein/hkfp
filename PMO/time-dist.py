
import numpy as np  
import matplotlib.pyplot as plt

def mktime(x):
    xs = (x.strip()).split(":")
    v = int(xs[0]) + (int(xs[1]) / 60)
    return v

# function to add value labels
def addlabels(x,y): 
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center', va = 'bottom')

bins = np.arange(0,25)

f = open("times.csv", "r")
zs = f.readlines()
hours = list(map(mktime, zs))

fig, ax = plt.subplots()

labels = []
for i in bins:
    if i<12:
        labels.append("{}:00AM".format(i))
    elif i == 12:
        labels.append("12:00PM")
    else:
        labels.append("{}:00PM".format(i-12))

ax.hist(hours, bins)
ax.set_xticks(bins + 0.5, bins) # 0.5 is half of the "1" auto width
ax.set_xticklabels(labels, rotation='vertical')
fig.subplots_adjust(bottom = 0.2) # makes space for the vertical 
                                  #labels.
plt.title('Distribution of Events by Time of Day')

ax.bar_label(ax.containers[0], label_type='edge')

plt.show()

