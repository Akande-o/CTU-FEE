N, T = list(map(int, input().split()))
Tnodes = list(map(int, input().split()))
edges =  [ []for j in range(N) ]
for i in range(N-1):
    node1, node2, cost = list(map(int, input().split()))
    edges[node1].append([node2, cost])
    edges[node2].append([node1, cost])
import time
t1 = time.time()
def find_all_paths(graph, start, end, dist, path, paths):
    path = path + [start]
    if start in end and start != Tnodes[0]:
        paths.append([start, path])
    if len(graph[start]) != 1 or start in end:
        for node in graph[start]:
            if node[0] not in path:
                new_dist = dist + node[1]
                find_all_paths(graph, node[0], end, new_dist, path, paths)
    return paths
lst = find_all_paths(edges, Tnodes[0], Tnodes, 0, [], [])
t2 = time.time()
print(t2-t1)