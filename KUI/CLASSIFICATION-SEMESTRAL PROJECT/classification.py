import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def func(a, b):
    a,b = np.array(a), np.array(b)
    c = a[np.equal(a,b)].tolist()
    fn= 0
    fp =0
    tp = 0
    p = 0
    n = 0
    for i in range(len(a)):
        if b[i] == 0:
            n+=1
        else:
            p += 1
        if a[i] == 1 and b[i] == 0:
            fp += 1
        if a[i] == 0 and b[i] == 1:
            fn += 1
        if a[i] == 1 and b[i] == 1:
            tp += 1
        
    return (len(c), fn/50, fp/(n), tp/(p))

def safety_first(classifier, corr_output, prev_acc, prev_tp, prev_fn, prev_fp):
    """
    Returns a boolean value which detemines if a classifier is better than the current best classifier
    within the secret agency.
    Parameters:
    classifier-path to the dsv file of the new classifier
    corr_output - path to the correct output data
    prev_acc - the current best classifier accuracy score
    prev_tp - the current best classifier true positive score
    prev_fn - the current best classifier false negative score
    prev_fp - the current best classifier false positive score
    """
    #   PROCESSING THE PARAMETERS IN ORDER TO GET IT WORKING
    c1 = pd.read_csv(classifier,header=None) 

    gt = pd.read_csv(corr_output,header=None)
    c1.columns = [x for x in range(50)]

    results = gt.to_numpy().transpose()
    C1 =c1.to_numpy().transpose()
    #   GETTING THE PARAMETERS WHICH WE WOULD USE TO COMPARE WITH THE PREVIOUS BEST CLASSIFIER
    result = [0]*50
    for i in range(50):
        result[i] = (func(C1[i], results[0]), i)

    best = []
    for j in range(20):
        best.append(sorted(result,key=lambda x: (x[0][0],-x[0][1],-x[0][2], x[0][3]), reverse=True)[:20][j])
    best_acc, best_fn, best_fp, best_tp = best[0][0]
    return best_acc > prev_acc and best_tp>prev_tp and best_fn < prev_fn and best_fp < prev_fp
##EXAMPLE TEST FORMAT
# print(safety_first("classif_result_tables/C1.dsv","classif_result_tables/GT.dsv",0.99, 0.96,0.05, 0.05))



