import time
N, E = list(map(int, input().split()))
edges =  [ [] for j in range(N) ]
for i in range(E):
    node1, node2 = list(map(int, input().split()))
    edges[node1].append(node2)
    edges[node2].append(node1)
t1 =time.time()
n = 0
for i in range(N):
    for j in edges[i]:
        if j < i: continue
        else:
            for first_node in edges[j]:
                if i in edges[first_node] or first_node == i:continue
                else:
                    for second_node in edges[i]:
                        if j in edges[second_node] or second_node == j or first_node in edges[second_node]: continue
                        else:
                            n += 1
print(n)
t2 = time.time()