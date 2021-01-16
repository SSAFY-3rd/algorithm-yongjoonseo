# 미로의 열쇠를 모두 찾아야 한다.
# 로봇이 열쇠를 찾으면 그 위치에서 복제된다.
# 복제된 로봇도 열쇠를 찾을 수 있다.
# 열쇠를 모두 찾은 후 같은 위치로 안 돌아와도 된다.

# 출력: 모든 로봇이 움직인 횟수의 총 합의 최솟값
    # 불가능한 경우 -1

# 시작점과 각 열쇠를 정점으로 한 밀집 그래프로 생각한다.
# 그 밀집 그래프의 최소 신장 트리를 구한다.
    # 어느 점에서 시작해도 상관 없다.


# 프림 알고리즘

from collections import deque


def is_found(y, x, graph, start, key):
    visited = [[0 for i in range(N)] for j in range(N)]
    q = deque([(y, x)])
    visited[y][x] = 1
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    
    reps = 1
    while q:
        for _ in range(len(q)):
            vy, vx = q.popleft()
            for i in range(4):
                ny = vy + dy[i]
                nx = vx + dx[i]
                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                    if field[ny][nx] >= 2:
                        e = field[ny][nx]
                        if graph.get(start):
                            graph.get(start).append((e, reps))
                        else:
                            graph[start] = [(e, reps)]
                        q.append((ny, nx))
                        key -= 1
                    elif field[ny][nx] == 0:
                        q.append((ny, nx))
                    visited[ny][nx] = 1
        reps += 1
    
    if key: return False
    else: return True

def prim(graph, start, M):
    minWeight = [float('inf') for i in range(M+3)]
    visited = [0 for i in range(M+3)]
    minWeight[0] = minWeight[1] = minWeight[start] = 0
    
    for i in range(2, M+3):
        minidx, minval = 0, float('inf')
        for j in range(2, M+3):
            if not visited[j] and minWeight[j] < minval:
                minval = minWeight[j]
                minidx = j
        visited[minidx] = 1

        for e, val in graph.get(minidx):
            if not visited[e] and minWeight[e] > val:
                minWeight[e] = val
    
    return sum(minWeight)

def solution(N, M, field):
    nodes = []
    idx = 2
    start = 0
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'S' or field[i][j] == 'K':
                if field[i][j] == 'S': start = idx
                field[i][j] = idx
                idx += 1
                nodes.append((i, j))
            else:
                field[i][j] = int(field[i][j])

    graph = dict()
    for i in range(N):
        for j in range(N):
            if field[i][j] >= 2:
                if not is_found(i, j, graph, field[i][j], M):
                    print(-1)
                    return
    
    print(prim(graph, start, M))

if __name__ == '__main__':
    N, M = map(int, input().split())
    field = [list(input()) for i in range(N)]
    solution(N, M, field)


# 크루스칼 알고리즘

from collections import deque


def is_found(y, x, edges, start, key):
    visited = [[0 for i in range(N)] for j in range(N)]
    q = deque([(y, x)])
    visited[y][x] = 1
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    
    reps = 1
    while q:
        for _ in range(len(q)):
            vy, vx = q.popleft()
            for i in range(4):
                ny = vy + dy[i]
                nx = vx + dx[i]
                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                    if field[ny][nx] >= 2:
                        edges.append((reps, start, field[ny][nx]))
                        q.append((ny, nx))
                        key -= 1
                    elif field[ny][nx] == 0:
                        q.append((ny, nx))
                    visited[ny][nx] = 1
        reps += 1
    
    if key: return False
    else: return True

def find(x, parents):
    if parents[x] == x:
        return x
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

def kruskal(edges):
    parents = [i for i in range(M+3)]
    ranks = [0 for i in range(M+3)]
    edges.sort()
    mst_val = 0
    
    for val, s, e in edges:
        if find(s, parents) != find(e, parents):
            union(s, e, parents, ranks)
            mst_val += val
    
    return mst_val

def solution(N, M, field):
    nodes = []
    idx = 2
    start = 0
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'S' or field[i][j] == 'K':
                if field[i][j] == 'S': start = idx
                field[i][j] = idx
                idx += 1
                nodes.append((i, j))
            else:
                field[i][j] = int(field[i][j])

    edges = []
    for i in range(N):
        for j in range(N):
            if field[i][j] >= 2:
                if not is_found(i, j, edges, field[i][j], M):
                    print(-1)
                    return
    
    print(kruskal(edges))

if __name__ == '__main__':
    N, M = map(int, input().split())
    field = [list(input()) for i in range(N)]
    solution(N, M, field)