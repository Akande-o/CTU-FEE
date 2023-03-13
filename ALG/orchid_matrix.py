import time
from itertools import product
t0 = time.time()
N = int(input())
M = []
for i in range(N):
    arr = list(map(int, input().split()))
    M.append(arr)
t1 = time.time()
Q = M
for i, j in list(product(range(N), range(1, N))):
        Q[i][j]  += Q[i][j-1]
for i, j in list(product(range(N), range(1, N))):
        Q[j][i] += Q[j-1][i]
min_sum_diff0 = 10**12
min_sum_diff1 = 10**12
min_sum_diff2 = 10**12
t2 = time.time()
#indices = list(product(range(1, N), range(1,N), range(1, N)))
#for num in indices
for a in range(N-1):
    if abs(Q[a][N-1] - (Q[N-1][N-1]- Q[a][N-1])) > min_sum_diff0:
        continue
    else:
        min_sum_diff0 = abs(Q[a][N-1] - (Q[N-1][N-1]- Q[a][N-1]))
        index0 = a

for b in range(N-1):
    if abs(Q[index0][b] - (Q[index0][N-1]- Q[index0][b])) > min_sum_diff1:
        continue
    else:
        min_sum_diff1 = abs(Q[index0][b] - (Q[index0][N-1]- Q[index0][b]))
        index1 = b
for c in range(N-1):
    num3 = Q[N-1][c] - Q[index0][c]
    num4 = Q[N-1][N-1] - Q[index0][N-1] - num3
    if abs(num4-num3) > min_sum_diff2:
        continue
    else:
        min_sum_diff2 = abs(num4-num3)
        index2 = c
num1 = Q[index0][index1]
num2 = Q[index0][N-1]- Q[index0][index1]
num3 = Q[N-1][index2] - Q[index0][index2]
num4 = Q[N-1][N-1] - Q[index0][N-1] - num3
min_sum_diff = (max(num1, num2, num3, num4) - min(num1, num2, num3, num4))
t3 = time.time()
print(min_sum_diff)            
t4 = time.time()
#print("The time for loading the data is: ",t1-t0)
#print('The time for the processing of the sum is:',t2-t1)
#print('The time for the processing of the minimum sum difference is: ',t3-t2)
#print('The time of printing',t4-t3)
#print('The time of total input to output: ',t3-t1)
#print('The time from input to output with print: ',t4-t1)