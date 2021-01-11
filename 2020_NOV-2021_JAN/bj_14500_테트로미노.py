# 테트로미노 - 상하좌우로 붙어있음
# 정사각형 4개가 붙어있음

# 출력: 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값

# depth 4로 백트래킹, 모든 방향 순회 끝난 지점은 visited 해보기.
# 가장 큰 수 갱신해서 출력
# -> 안 된다. (가운데만 뾰족한 모양이 안 만들어진다.)
# 뾰족한 모양은 따로 체크

# from itertools import combinations

# def BT(y, x, depth, val):
#     global N, M, dy, dx, field, result
#     if depth == 4:
#         result = max(result, val)
#         return
#     visited[y][x] = 1
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]

#         if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
#             BT(ny, nx, depth+1, val + field[ny][nx])
#             visited[ny][nx] = 0
#     visited[y][x] = 0

# def mid_block(y, x):
#     global result
#     candis = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
#     temp_result = -1
#     for candi in combinations(candis, 3):
#         ((y1, x1), (y2, x2), (y3, x3)) = candi
#         if 0 <= y1 < N and 0 <= y2 < N and 0 <= y3 < N and 0 <= x1 < M and 0 <= x2 < M and 0 <= x3 < M:
#             temp_val = field[y][x] + field[y1][x1] + field[y2][x2] + field[y3][x3]
#             temp_result = max(temp_result, temp_val)
#     result = max(temp_result, result)

# N, M = map(int, input().split())
# field = [list(map(int, input().split())) for i in range(N)]
# dy = [0, 1, 0, -1]
# dx = [1, 0, -1, 0]
# visited = [[0 for i in range(M)] for j in range(N)]
# result = -1

# for i in range(N):
#     for j in range(M):
#         BT(i, j, 1, field[i][j])
#         mid_block(i, j)

# print(result)


# 백트래킹으로 나머지 네 개의 블럭에 대해서는 모두 탐색한다 생각했지만, 아닌 경우가 있다.
    # 현재 한 번 방문했던 지점은 visited 처리하기 때문에 발생하는 문제.

# >>> 시간 초과



# 백트래킹을 3개까지 적용하고 한 개의 블럭을 덧대보자.

from itertools import combinations

def BT(y, x, depth, val, ry, rx):
    global N, M, dy, dx, field, result
    if depth == 3:
        for i in range(4):
            ny = ry + dy[i]
            nx = rx + dx[i]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                result = max(result, val + field[ny][nx])
        return
    visited[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            BT(ny, nx, depth+1, val + field[ny][nx], ry, rx)
    visited[y][x] = 0

def mid_block(y, x):
    global result
    candis = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
    temp_result = -1
    for candi in combinations(candis, 3):
        ((y1, x1), (y2, x2), (y3, x3)) = candi
        if 0 <= y1 < N and 0 <= y2 < N and 0 <= y3 < N and 0 <= x1 < M and 0 <= x2 < M and 0 <= x3 < M:
            temp_val = field[y][x] + field[y1][x1] + field[y2][x2] + field[y3][x3]
            temp_result = max(temp_result, temp_val)
    result = max(temp_result, result)

N, M = map(int, input().split())
field = [list(map(int, input().split())) for i in range(N)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
visited = [[0 for i in range(M)] for j in range(N)]
result = -1

for i in range(N):
    for j in range(M):
        BT(i, j, 1, field[i][j], i, j)
        mid_block(i, j)

print(result)
