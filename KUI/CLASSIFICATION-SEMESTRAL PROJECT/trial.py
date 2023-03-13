import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

c1 = pd.read_csv("classif_result_tables/C1.dsv",header=None) 
C1 = c1.to_numpy().transpose().flatten()
gt = pd.read_csv("classif_result_tables/GT.dsv",header=None)
results = gt.to_numpy().transpose()[0]

tpr = []
fpr = []
tp = 0
fp = 0
for i in range(len(C1)):
    if C1[i] == 1 and results[i%(len(results))] == 1:
        if i == 0:
            tp += 1
            tpr.append(min(1/2500, 1))
            fpr.append(0)
        else:
            tp += 1
            tpr.append(min(tp/2500, 1))
            fpr.append(fpr[-1])
    elif C1[i] == 0 and results[i%(len(results))] == 1:
        if i == 0:
            fp += 1
            fpr.append(min(1/2500, 1))
            tpr.append(0)
        else:
            fp += 1
            tpr.append(tpr[-1])
            fpr.append(min(fp/2500, 1))
plt.plot(fpr, tpr)
plt.plot(fpr[2200], tpr[2200], "x")
plt.show()
    

