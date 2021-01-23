# 출력: 테케마다 목적지 후보 중 가능한 것만 오름차순으로.

# 체크할 조건
# 2 <= n <= 2000, 1 <= m <= 50000, 1 <= t <= 100
    # 교차로, 도로, 목적지 후보

# 목적지 후보로 가는 것 중 최단거리로 가는 것만 출력한다.
    # 최단거리로 가는 길에 gh를 반드시 거쳐야 한다.
    # g든 h든 거친 경우 & 그 경우가 최소인 경우만 가능하다고 표시.
        # == s -> g -> h -> t or s -> h -> g -> t

# def djikstra(graph, s, n):
#     dist = [float('inf')] * (n+1)
#     visited = [0] * (n+1)
#     dist[s] = 0

#     for i in range(1, n+1):
#         mi, mn = 0, float('inf')
#         for j in range(1, n+1):
#             if not visited[j] and mn > dist[j]:
#                 mi, mn = j, dist[j]
#         visited[mi] = 1
#         if mi in graph:
#             for v, val in graph.get(mi):
#                 if not visited[v] and dist[v] > dist[mi] + val:
#                     dist[v] = dist[mi] + val
#     return dist

# def solution(n, m, t):
#     s, g, h = map(int, input().split())
#     graph = dict()
#     gh = 0
#     for i in range(m):
#         a, b, d = map(int, input().split())
#         if (a == g and b == h) or (a == h and b == g): gh = d
#         if a in graph: graph[a].append((b, d))
#         else: graph[a] = [(b, d)]
#         if b in graph: graph[b].append((a, d))
#         else: graph[b] = [(a, d)]
    
#     lst = djikstra(graph, s, n)
#     stog, stoh = lst[g], lst[h]
#     gtot_lst = djikstra(graph, g, n)
#     htot_lst = djikstra(graph, h, n)
#     candis = []
#     for i in range(t):
#         inp = int(input())
#         if (stog + gh + htot_lst[inp] == lst[inp]) or (stoh + gh + gtot_lst[inp] == lst[inp]): 
#             candis.append(inp)
#     candis.sort()
#     print(*candis)

# if __name__ == '__main__':
#     for t in range(int(input())):
#         solution(*map(int, input().split()))


# gh를 반드시 들러야 한다.
    # 간선의 길이를 모두 두 배로 하고 
    # 최단거리가 홀수인 경우만 출력

# import sys
# input = sys.stdin.readline
# INF = 10 ** 10

# def djikstra(graph, s, n):
#     dist = [INF] * (n+1)
#     visited = [0] * (n+1)
#     dist[s] = 0

#     for i in range(1, n+1):
#         mi, mn = 0, INF
#         for j in range(1, n+1):
#             if not visited[j] and mn > dist[j]:
#                 mi, mn = j, dist[j]
#         visited[mi] = 1
#         if mi in graph:
#             for v, val in graph.get(mi):
#                 if not visited[v] and dist[v] > dist[mi] + val:
#                     dist[v] = dist[mi] + val
    
#     return dist

# def solution(n, m, t):
#     s, g, h = map(int, input().split())
#     graph = dict()
#     for i in range(m):
#         a, b, d = map(int, input().split())
#         if (a == g and b == h) or (a == h and b == g): d = d * 2 - 1
#         else: d *= 2
#         if a in graph: graph[a].append((b, d))
#         else: graph[a] = [(b, d)]
#         if b in graph: graph[b].append((a, d))
#         else: graph[b] = [(a, d)]
    
#     dist = djikstra(graph, s, n)
#     result = []
#     for i in range(t):
#         inp = int(input())
#         if dist[inp] & 1: result.append(inp)
#     print(*sorted(result))

# if __name__ == '__main__':
#     for i in range(int(input())):
#         solution(*map(int, input().split()))

# >> 836 ms

import sys
input = sys.stdin.readline
from heapq import heappush, heappop
INF = 10 ** 10

def djikstra(graph, s, n):
    dist = [INF] * (n+1)
    dist[s] = 0
    pq = [(0, s)]

    while pq:
        mn, mi = heappop(pq)
        if dist[mi] < mn: continue # 정확히 왜??
        if mi in graph:
            for v, val in graph.get(mi):
                if dist[v] > dist[mi] + val:
                    dist[v] = dist[mi] + val
                    heappush(pq, (dist[v], v))
    return dist

def solution(n, m, t):
    s, g, h = map(int, input().split())
    graph = dict()
    for i in range(m):
        a, b, d = map(int, input().split())
        if (a == g and b == h) or (a == h and b == g): d = d * 2 - 1
        else: d *= 2
        if a in graph: graph[a].append((b, d))
        else: graph[a] = [(b, d)]
        if b in graph: graph[b].append((a, d))
        else: graph[b] = [(a, d)]
    
    dist = djikstra(graph, s, n)
    result = []
    for i in range(t):
        inp = int(input())
        if dist[inp] & 1: result.append(inp)
    print(*sorted(result))

if __name__ == '__main__':
    for i in range(int(input())):
        solution(*map(int, input().split()))