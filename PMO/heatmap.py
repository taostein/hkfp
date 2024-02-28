
import sys
import numpy as np; np.random.seed(1)
import pandas as pd

xx = pd.read_csv(sys.argv[1], header=None)
days = pd.DatetimeIndex(data=xx.loc[:,0])
counts = np.array(xx.loc[:,1])

values = pd.Series(counts, index=days)

import calplot
import matplotlib.pyplot as plt
calplot.calplot(values,
                suptitle = sys.argv[2],
                suptitle_kws = {'x': 0.5, 'y': 1.0})

plt.show()

