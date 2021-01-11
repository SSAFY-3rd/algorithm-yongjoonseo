# 2차원
# 모든 우주신을 연결해야한다
# 이미 연결된 통로 외에 새로 만들어야 할 통로 길이 합이 최소가 되어야 한다.
# 거리: 2차원 좌표상의 거리

# 출력: 만들어야할 최소 통로 길이

# 이미 있는 통로를 포함하는 최소 스패닝 트리의 크기를 구한다.
    # 새로 만들어지는 통로의 길이만 고려한다.
# 크루스칼 알고리즘을 사용한다.

import sys
input = sys.stdin.readline

def find(x, parents):
    if parents[x] == x: return x
    parents[x] = find(parents[x], parents)
    return parents[x]

def union(x, y, parents, ranks):
    xroot = find(x, parents)
    yroot = find(y, parents)
    if ranks[xroot] >= ranks[yroot]:
        parents[yroot] = xroot
    else:
        parents[xroot] = yroot
    if ranks[xroot] == ranks[yroot]:
        ranks[xroot] += 1

def kruskal(edges, parents, ranks):
    cost = 0
    for val, s, e in edges:
        if find(s, parents) != find(e, parents):
            cost += val
            union(s, e, parents, ranks)
    return cost

def solution(N, M):
    edges = []
    x, y = map(int, input().split())
    parents = [i for i in range(N+1)]
    ranks = [0 for i in range(N+1)]
    coors = [None, (x, y)]
    head = 2
    for i in range(N-1):
        x1, y1 = map(int, input().split())
        for j in range(1, len(coors)):
            x2, y2 = coors[j]
            d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)
            edges.append((d, j, head))
        coors.append((x1, y1))
        head += 1

    for i in range(M):
        a, b = map(int, input().split())
        if find(a, parents) != find(b, parents):
            union(a, b, parents, ranks)
    
    edges.sort()
    print('{0:0.2f}'.format(kruskal(edges, parents, ranks)))

if __name__ == '__main__':
    solution(*map(int, input().split()))

# 1400 ms


# 참고 코드 (828 ms)
    # 무슨 차이일까?

import sys
from heapq import heappush, heappop
from math import sqrt

input = sys.stdin
sys.setrecursionlimit(5000)


def find(u):
    if u == parent[u]: return u
    parent[u] = find(parent[u])
    return parent[u]


def merge(u, v):
    u, v = find(u), find(v)
    if u == v: return
    parent[u] = v


if __name__ == '__main__':
    n, m = map(int, input.readline().split())
    v = []
    parent = [0] * n
    cnt, ans = 0, 0
    for i in range(n):
        parent[i] = i
    for _ in range(n):
        x, y = map(int, input.readline().split())
        v.append((x, y))

    for _ in range(m):
        a, b = map(int, input.readline().split())
        a -= 1
        b -= 1
        if find(a) != find(b):
            merge(a, b)
            cnt += 1

    pq = []
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            dist = sqrt((v[i][0] - v[j][0]) * (v[i][0] - v[j][0]) + (v[i][1] - v[j][1]) * (v[i][1] - v[j][1]))
            heappush(pq, (dist, i, j))

    while cnt != n - 1:
        dist, here, next = heappop(pq)
        if find(here) != find(next):
            merge(here, next)
            cnt += 1
            ans += dist

    print("%.2f" % ans)