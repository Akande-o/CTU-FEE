import time
N, T = list(map(int, input().split()))
Tnodes = list(map(int, input().split()))
edges =  [ [] for j in range(N) ]
for i in range(N-1):
    node1, node2, cost = list(map(int, input().split()))
    edges[node1].append([node2, cost])
    edges[node2].append([node1, cost])
    
t1 = time.time()
def remove_nodes(lst, num):
    if len(lst[num]) > 1 or num in Tnodes:
        return lst
    next_num = lst[num][0][0]
    dist = lst[num][0][1]
    lst[next_num].remove([num, dist])
    lst[num] = []
    return remove_nodes(lst, next_num)
t3 = time.time()
for i in range(len(edges)):
    if len(edges[i]) == 1 and i not in Tnodes:
        edges = remove_nodes(edges, i)
t4 =time.time()
total = 0
for edge in edges:
    if edge == []:
        continue
    else:
        for line in edge:
            total += line[1]
print(total)
t2 = time.time()
print(t2-t1)
print(t4-t3)