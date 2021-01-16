# N개의 행성
# 터널 연결비용 min(|xa - xb|, |ya - yb|, |za - zb|)
# 터널 N-1개

# 출력: 모든 행성을 터널로 연결하는데 필요한 최소 비용

# 체크할 조건
# N <= 100000
    # 간선을 있는 대로 다 만들면 시간초과

# 크루스칼 알고리즘
# 간선의 길이가 0에 가까운 것 N-1개를 뽑는다.
    # 간선의 길이가 0인 것들은 바로 union

# import sys
# input = sys.stdin.readline

# def find(x, parents):
#     if parents[x] == x: return x
#     parents[x] = find(parents[x], parents)
#     return parents[x]

# def union(x, y, parents, ranks):
#     xr = find(x, parents)
#     yr = find(y, parents)
#     if ranks[xr] >= ranks[yr]:
#         parents[yr] = xr
#     else:
#         parents[xr] = yr
#     if ranks[xr] == ranks[yr]:
#         ranks[xr] += 1

# def kruskal(edges, parents, ranks, cnt):
#     cost = 0
#     for val, x, y in edges:
#         if not cnt: return cost
#         if find(x, parents) != find(y, parents):
#             union(x, y, parents, ranks)
#             cnt -= 1
#             cost += val
#     return cost

# def solution(N):
#     parents = [i for i in range(N)]
#     ranks = [0 for i in range(N)]
#     ps = [list(map(int, input().split())) for i in range(N)]
#     edges = []
    
#     cnt = N-1
#     for i in range(N-1):
#         for j in range(i+1, N):
#             if find(i, parents) == find(j, parents): continue
#             diff = min(abs(ps[i][0] - ps[j][0]), abs(ps[i][1] - ps[j][1]), abs(ps[i][2] - ps[j][2]))
#             if not diff: 
#                 union(i, j, parents, ranks)
#                 cnt -= 1
#                 continue
#             edges.append([diff, i, j])
#             if not cnt: break
#         if not cnt: break

#     if cnt: 
#         edges.sort()
#         print(kruskal(edges, parents, ranks, cnt))
#     else: print(0)

# if __name__ == '__main__':
#     solution(int(input()))

# >> 메모리 초과

# x, y, z 모두 각각 정렬해서 저장해두고 
# 10만개의 좌표에 대해서 인접한 점만 검사해서 edge에 넣는다.

import sys
input = sys.stdin.readline

def find(x, parents):
    if parents[x] == x: return x
    parents[x] = find(parents[x], parents)
    return parents[x]

def union(x, y, parents, ranks):
    xr = find(x, parents)
    yr = find(y, parents)
    if ranks[xr] >= ranks[yr]:
        parents[yr] = xr
    else:
        parents[xr] = yr
    if ranks[xr] == ranks[yr]:
        ranks[xr] += 1

def kruskal(edges, parents, ranks, cnt):
    cost = 0
    for val, x, y in edges:
        if not cnt: return cost
        if find(x, parents) != find(y, parents):
            union(x, y, parents, ranks)
            cnt -= 1
            cost += val
    return cost

def solution(N):
    parents = [i for i in range(N)]
    ranks = [0 for i in range(N)]
    planets = []
    edges = []

    for i in range(N):
        x, y, z = map(int, input().split())
        planets.append([x, y, z, i])
    
    cnt = N-1
    for i in range(3):
        planets.sort(key=lambda x: x[i])
        for j in range(1, N):
            nowv, nowi = planets[j][i], planets[j][3]
            prevv, previ = planets[j-1][i], planets[j-1][3]
            edges.append([abs(nowv - prevv), nowi, previ])
    
    edges.sort()
    print(kruskal(edges, parents, ranks, cnt))

if __name__ == '__main__':
    solution(int(input()))