# 출력: 1 -> N 역으로 가는데 방문하는 역 개수의 최솟값
    # 갈 수 없으면 -1 출력

# 체크할 조건
# 1 <= N <= 100000
# 1 <= K, M <= 1000
# 모든 역을 들르는 게 아니다

# 하이퍼튜브도 모두 정점으로 둔다.
    # 정점 -> 튜브 -> 정점 -> 튜브와 같이 움직인다
# BFS사이클 횟수 // 2 + 1을 출력한다.

import sys
input = sys.stdin.readline
from collections import deque

def BFS(graph, visited, N):
    if N == 1: return 1
    q = deque([1])
    visited[1] = 1
    cnt = 0
    while q:
        cnt += 1
        for i in range(len(q)):
            idx = q.popleft()
            if idx in graph:
                for num in graph.get(idx):
                    if not visited[num]:
                        if num == N: return cnt // 2 + 1
                        visited[num] = 1
                        q.append(num)
    return -1

def solution(N, K, M):
    graph, idx = dict(), N + 1
    visited = [0] * (N + M + 1)
    for _ in range(M):
        lst = list(map(int, input().split()))
        for i in lst:
            if i in graph: graph[i].append(idx)
            else: graph[i] = [idx]
        graph[idx] = lst
        idx += 1
    print(BFS(graph, visited, N))

if __name__ == '__main__':
    solution(*map(int, input().split()))