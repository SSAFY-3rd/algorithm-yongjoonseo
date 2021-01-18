# 1번 -> N번 정점
# 임의의 두 정점을 반드시 통과해야 한다.
# 한번 이동했던 정점, 간선 모두 다시 이동할 수 있다.

# 출력: 두 개의 정점을 지나는 최단 경로의 길이
    # 없으면 -1

# 체크할 조건
# 2 <= N <= 800 (정점), 0 <= E <= 200000 (간선)
# 두 개의 정점을 반드시 지나야 한다.

# 다익스트라 알고리즘 활용
# 1 -> v1 -> v2 -> N // 1 -> v2 -> v1 -> N

import sys
input = sys.stdin.readline

def djikstra(graph, N, s, targets):
    visited = [0 for i in range(N+1)]
    dist = [float('inf') for i in range(N+1)]
    dist[s] = 0
    ris = [0 for i in range(len(targets))]

    for i in range(1, N+1):
        mi, mv = 0, float('inf')
        for j in range(1, N+1):
            if not visited[j] and mv > dist[j]:
                mv, mi = dist[j], j
        visited[mi] = 1
        for k in range(len(targets)):
            if targets[k] == mi: ris[k] = mi
        
        if mi in graph:
            for v, val in graph.get(mi):
                if not visited[v]:
                    dist[v] = min(dist[v], dist[mi] + val)
        
        for t in targets:
            if not visited[t]: break
        else:
            break
    
    rs = [dist[ris[i]] for i in range(len(ris))]
    return rs

def solution(N, E):
    graph = dict()
    for i in range(E):
        a, b, c = map(int, input().split())
        if a in graph:
            graph[a].append((b, c))
        else:
            graph[a] = [(b, c)]
        if b in graph:
            graph[b].append((a, c))
        else:
            graph[b] = [(a, c)]
    
    v1, v2 = map(int, input().split())
    tov1, tov2 = djikstra(graph, N, 1, [v1, v2])
    v1toN, v1tov2 = djikstra(graph, N, v1, [N, v2])
    v2toN, v2tov1 = djikstra(graph, N, v2, [N, v1])

    minval = min(tov1 + v1tov2 + v2toN, tov2 + v2tov1 + v1toN)
    if minval == float('inf'): print(-1)
    else: print(minval)

if __name__ == '__main__':
    solution(*map(int, input().split()))