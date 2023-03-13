import time
N, E, C = list(map(int, input().split()))
colors= list(map(int, input().split()))
edges =  [ [] for j in range(N) ]
unisolated = set()
for i in range(E):
    node1, node2 = list(map(int, input().split()))
    edges[node1].append(node2)
    edges[node2].append(node1)
    if colors[node1] == colors[node2]:
        unisolated.add(node1)
        unisolated.add(node2)
t1 = time.time()
isolated = set(range(N)) - unisolated

n = 0
visited = set()
for node in isolated:
    visited.add(node)
    children = edges[node]
    two_distance =set()
    for child in children:
        two_distance = set.union(two_distance, set(edges[child]))
    two_distance = two_distance - visited
    n += len(two_distance&isolated)
t2 = time.time()
print(n)
#print(t2-t1)
    