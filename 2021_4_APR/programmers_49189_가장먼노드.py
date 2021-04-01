# 가장 멀리 떨어진 노드: 
    # 최단 경로로 이동했을 때 간선의 개수가 가장 많은 노드

# 출력: 1번 노드에서 가장 멀리 떨어진 노드 개수

# 체크할 조건
    # 양방향 그래프
    # 2 <= n <= 20000 (노드의 개수)

# 가중치가 없으므로 BFS한 가장 마지막 노드들의 개수를 출력

from collections import deque

def BFS(graph, n):
    q = deque([1])
    visited = [0] * (n+1)
    visited[1] = 1
    while q:
        cnt = len(q)
        for _ in range(len(q)):
            node = q.popleft()
            if node in graph:
                for v in graph.get(node):
                    if not visited[v]:
                        visited[v] = 1
                        q.append(v)
    return cnt

def solution(n, edge):
    graph = dict()
    for s, e in edge:
        if s in graph:
            graph[s].append(e)
        else:
            graph[s] = [e]
        if e in graph:
            graph[e].append(s)
        else:
            graph[e] = [s]
    
    answer = BFS(graph, n)
    return answer