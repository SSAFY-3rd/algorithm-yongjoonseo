# 모든 집하장에서 각각 다른 집하장으로 가는 최단 경로를 구해야 한다.

# 출력: 가장 먼저 가야하는 집하장 경로표 (자신에게 가는 건 - 로 표시)

# 모든 쌍에 대한 최단 경로를 구해야 하므로 플로이드 알고리즘을 사용한다.
# 1. 가중치 field
# 2. 초기 간선 연결 여부 edges
# 3. 경로표 table


# A. 2168 ms

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
field = [[float('inf') for i in range(n+1)] for j in range(n+1)]
edges = [[0 for i in range(n+1)] for j in range(n+1)]
table = [['-' for i in range(n+1)] for j in range(n+1)]

for i in range(1, n+1):
    for j in range(i, n+1):
        if i != j:
            table[i][j] = j
            table[j][i] = i

for _ in range(m):
    s, e, t = map(int, input().split())
    field[s][e] = t
    field[e][s] = t
    edges[s][e] = 1
    edges[e][s] = 1

for i in range(1, n+1):
    field[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        if field[i][k]:
            for j in range(1, n+1):
                if field[i][j] > field[i][k] + field[k][j]:
                    field[i][j] = field[i][k] + field[k][j]
                    table[i][j] = k

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j: continue
        arrive = table[i][j]
        while not table[i][arrive] == arrive:
            arrive = table[i][arrive]
        table[i][j] = arrive

for _ in range(1, n+1):
    print(*table[_][1:])

# 플로이드 알고리즘은 최단 '거리' 알고리즘이라,
# 경로를 찾을 땐 추가적인 작업이 많이 필요하다.
# 역으로 추적하는 연산이 필요해서 시간이 많이 걸린다.

# 역으로 추적하는 연산을 줄여본다면?

# B. 2312 ms

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
field = [[float('inf') for i in range(n+1)] for j in range(n+1)]
edges = [[0 for i in range(n+1)] for j in range(n+1)]
table = [['-' for i in range(n+1)] for j in range(n+1)]

for i in range(1, n+1):
    for j in range(i, n+1):
        if i != j:
            table[i][j] = j
            table[j][i] = i

for _ in range(m):
    s, e, t = map(int, input().split())
    field[s][e] = t
    field[e][s] = t
    edges[s][e] = 1
    edges[e][s] = 1

for i in range(1, n+1):
    field[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        if field[i][k]:
            for j in range(1, n+1):
                if field[i][j] > field[i][k] + field[k][j]:
                    field[i][j] = field[i][k] + field[k][j]
                    table[i][j] = k

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j: continue
        lst = [(i, j)]
        arrive = table[i][j]
        while not table[i][arrive] == arrive:
            lst.append((i, arrive))
            arrive = table[i][arrive]
        for y, x in lst:
            table[y][x] = arrive

for _ in range(1, n+1):
    print(*table[_][1:])

# 별로 최적화되지 않는다.
    # arrive를 할당시킬 때 이미 최소 깊이인 경우가 많은 것 같다.

# 다익스트라 알고리즘을 모든 집하장에 대해 실행하고, 
# 맨 처음 방문하는 집하장을 경로표에 모은다.

# C. 1016 ms

import sys
input = sys.stdin.readline


def Dijkstra(G, s, n):
    visited = [0 for i in range(n+1)]
    dist = [float('inf') for i in range(n+1)]
    parents = ['-' for i in range(n+1)]
    dist[s] = 0

    for i in range(1, n+1):
        minidx, minval = -1, float('inf')
        for j in range(1, n+1):
            if not visited[j] and dist[j] < minval:
                minidx = j
                minval = dist[j]
        visited[minidx] = 1

        if G.get(minidx):
            for v, val in G.get(minidx):
                if not visited[v] and dist[minidx] + val < dist[v]:
                    dist[v] = dist[minidx] + val
                    parents[v] = minidx
                    if minidx == s: parents[v] = v
    
    for i in range(1, n+1):
        if i == s: continue
        arrive = parents[i]
        while not parents[arrive] == arrive:
            arrive = parents[arrive]
        parents[i] = arrive

    return parents[1:]

n, m = map(int, input().split())
graph = dict()
result = []

for i in range(m):
    s, e, t = map(int, input().split())
    if graph.get(s):
        graph.get(s).append((e, t))
    else:
        graph[s] = [(e, t)]
    if graph.get(e):
        graph.get(e).append((s, t))
    else:
        graph[e] = [(s, t)]

for i in range(1, n+1):
    result.append(Dijkstra(graph, i, n))

for _ in range(n):
    print(*result[_])
