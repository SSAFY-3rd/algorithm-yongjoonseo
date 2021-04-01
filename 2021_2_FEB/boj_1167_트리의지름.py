# 출력: 임의의 두 점 사이의 거리 중 가장 긴 것

# 체크할 조건
# 2 <= V <= 100000 (정점)
# 정점 번호 1 ~ V
# 256 MB 메모리 제한

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)

# def update_max(val):
#     global result
#     if result < val:
#         result = val

# def DFS(graph, visited, node, total):
#     leaf = True
#     for e, val in graph.get(node):
#         if not visited[e]:
#             visited[e] = 1
#             DFS(graph, visited, e, total+val)
#             if leaf: leaf = False
#     if leaf:
#         update_max(total)

# def solution(V):
#     graph = dict()
#     visited = [0] * (V+1)
#     root = None
#     for _ in range(V):
#         line = list(map(int, input().split()))
#         s = line[0]
#         if not root and len(line) == 4:
#             root = s
#         graph[s] = []
#         for i in range(2, len(line), 2):
#             e, val = line[i-1], line[i]
#             graph[s].append((e, val))
    
#     visited[root] = 1
#     DFS(graph, visited, root, 0)
#     print(result)

# if __name__ == '__main__':
#     result = -1
#     solution(int(input()))

# 반례: 1 - 2 - 3 - 4 - 5
#               |
#               6
# 6
# 1 3 1 -1
# 2 6 1 3 1 -1
# 3 2 1 6 1 4 1 -1
# 4 3 1 5 1 -1
# 5 4 1 -1
# 6 2 1 -1


# root 노드 모두에서 계산해보기

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)

# def update_max(val):
#     global result
#     if result < val:
#         result = val

# def DFS(graph, visited, node, total):
#     leaf = True
#     for e, val in graph.get(node):
#         if not visited[e]:
#             visited[e] = 1
#             DFS(graph, visited, e, total+val)
#             visited[e] = 0
#             if leaf: leaf = False
#     if leaf:
#         update_max(total)

# def solution(V):
#     graph = dict()
#     visited = [0] * (V+1)
#     roots = []
#     for _ in range(V):
#         line = list(map(int, input().split()))
#         s = line[0]
#         if len(line) == 4:
#             roots.append(s)
#         graph[s] = []
#         for i in range(2, len(line), 2):
#             e, val = line[i-1], line[i]
#             graph[s].append((e, val))
    
#     for node in roots:
#         visited[node] = 1
#         DFS(graph, visited, node, 0)
#         visited[node] = 0
#     print(result)

# if __name__ == '__main__':
#     result = -1
#     solution(int(input()))

# >> 시간 초과



import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def update_max(val, node):
    global result, new_root
    if result < val:
        result = val
        new_root = node

def DFS(graph, visited, node, total):
    leaf = True
    for e, val in graph.get(node):
        if not visited[e]:
            visited[e] = 1
            DFS(graph, visited, e, total+val)
            visited[e] = 0
            if leaf: leaf = False
    if leaf:
        update_max(total, node)

def solution(V):
    graph = dict()
    visited = [0] * (V+1)
    root = None
    for _ in range(V):
        line = list(map(int, input().split()))
        s = line[0]
        if not root and len(line) == 4:
            root = s
        graph[s] = []
        for i in range(2, len(line), 2):
            e, val = line[i-1], line[i]
            graph[s].append((e, val))
    
    visited[root] = 1
    DFS(graph, visited, root, 0)
    visited[new_root] = 1
    DFS(graph, visited, new_root, 0)
    print(result)

if __name__ == '__main__':
    result, new_root = -1, None
    solution(int(input()))