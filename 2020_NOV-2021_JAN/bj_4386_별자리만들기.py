# 선을 하나 이을 때마다 두 별 사이의 거리만큼 비용이 든다.

# 출력: 별자리를 만드는 최소 비용

# 별들의 최소 신장 트리를 구한다.
# 각각의 별을 하나의 node라고 생각하고
# 모든 별들이 간선으로 이어져있다고 생각한다.

# 1. 모든 별의 좌표를 저장하는 stars
# 2. 별의 간선을 저장하는 2차원 배열 ds

# 1. 프림 알고리즘

def prim(s, n, ds):
    visited = [0 for i in range(n)]
    weight = [float('inf') for i in range(n)]
    weight[s] = 0

    for i in range(n):
        minidx, minval = 0, float('inf')
        for j in range(n):
            if not visited[j] and weight[j] < minval:
                minidx = j
                minval = weight[j]
        visited[minidx] = 1

        for j in range(n):
            if visited[j] or j == minidx: continue
            weight[j] = min(weight[j], ds[minidx][j])
    
    return sum(weight)


def solution(n):
    stars = []
    ds = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        x, y = map(float, input().split())
        stars.append((x, y))
    
    for i in range(n):
        for j in range(i+1, n):
            d = ((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2) ** (1/2)
            ds[i][j] = d
            ds[j][i] = d
    
    print(prim(0, n, ds))

if __name__ == '__main__':
    solution(int(input()))

# 2. 크루스칼 알고리즘

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

def kruskal(edges, n):
    parents = [i for i in range(n)]
    ranks = [0 for i in range(n)]
    mst_cost = 0

    for val, s, e in edges:
        if find(s, parents) != find(e, parents):
            mst_cost += val
            union(s, e, parents, ranks)
    
    return mst_cost

def solution(n):
    stars = []
    edges = []

    for i in range(n):
        stars.append(list(map(float, input().split())))
    
    for i in range(n):
        for j in range(i+1, n):
            d = ((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2) ** (1/2)
            edges.append((d, i, j))
            edges.append((d, j, i))
    
    edges.sort()
    print(kruskal(edges, n))

if __name__ == '__main__':
    solution(int(input()))