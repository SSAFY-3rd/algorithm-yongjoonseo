# 출력: 가장 큰 음식물의 크기 출력

# BFS, DFS 등으로 갱신해가면서 가장 큰 음식물 크기 저장 후 출력

# from collections import deque


def BFS(r, c):
    global N, M, field
    q = deque([(r, c)])
    field[r][c] = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    size = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M and field[ny][nx]:
                q.append((ny, nx))
                field[ny][nx] = 0
                size += 1
    
    return size

N, M, K = map(int, input().split())
field = [[0 for i in range(M)] for j in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    field[r-1][c-1] = 1

size = -1
for i in range(N):
    for j in range(M):
        if field[i][j]:
            size = max(size, BFS(i, j))

print(size)




import sys
sys.setrecursionlimit(1000000)

def DFS(y, x):
    global field, dy, dx, N, M, comp
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < M and field[ny][nx]:
            field[ny][nx] = 0
            comp += 1
            DFS(ny, nx)

N, M, K = map(int, input().split())
field = [[0 for i in range(M)] for j in range(N)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for _ in range(K):
    r, c = map(int, input().split())
    field[r-1][c-1] = 1

size = -1
for i in range(N):
    for j in range(M):
        if field[i][j]:
            field[i][j] = 0
            comp = 1
            DFS(i, j)
            size = max(comp, size)

print(size)




def DFS(r, c):
    global dy, dx, field

    stack = [(r, c)]
    val = 1
    field[r][c] = 0

    while stack:
        y, x = stack[-1]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M and field[ny][nx]:
                stack.append((ny, nx))
                field[ny][nx] = 0
                val += 1
                break
        else:
            stack.pop()         
    
    return val

N, M, K = map(int, input().split())
field = [[0 for i in range(M)] for j in range(N)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for _ in range(K):
    r, c = map(int, input().split())
    field[r-1][c-1] = 1

size = -1
for i in range(N):
    for j in range(M):
        if field[i][j]:
            size = max(size, DFS(i, j))

print(size)