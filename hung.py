import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# load data
df = pd.read_csv("linearinput.csv")
# plot data
df.plot(x='x', y='y', legend=False, marker='o', style='o', mec='b', mfc='w')
# expected line
plt.plot(df.values[:,0], df.values[:,1], color='g')
plt.xlabel('x'); plt.ylabel('y'); plt.show()

# extract X, y
X = df.values[:,0]
y = df.values[:,2]
# number of training examples
m = y.size