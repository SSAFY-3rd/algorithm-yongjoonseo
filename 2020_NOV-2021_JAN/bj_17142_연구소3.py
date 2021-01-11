# NxN 정사각형 연구소
# 빈칸, 벽, 바이러스로 이루어져있다
# 활성 바이러스가 비활성 바이러스로 가면 비활성이 활성으로 변한다

# 출력: 모든 빈 칸에 바이러스가 있게 되는 최소 시간
    # 모든 빈 칸에 바이러스를 놓을 수 없으면 -1 출력

# N이 최대 50이므로 맵 전체를 탐색한다면 2500번,
# 2의 개수는 10보다 작거나 같으므로 대략 10C5정도가 가장 큰 경우의 수
# 10C5 * 2500 * 5 = 315만
# 백트래킹으로 풀어보자

from collections import deque
from itertools import combinations

def BFS(candis, min_time, left):
    global time
    q = deque(candis)
    time_val = 0
    visited = [[0 for i in range(N)] for j in range(N)]
    for y, x in candis:
        visited[y][x] = 1

    while q:
        if not left: break
        time_val += 1
        if time_val >= min_time: return float('inf')
        for i in range(len(q)):
            y, x = q.popleft()

            for j in range(4):
                ny = y + dy[j]
                nx = x + dx[j]

                if 0 <= ny < N and 0 <= nx < N and field[ny][nx] != 1 and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    q.append((ny, nx))
                    if field[ny][nx] == 0: 
                        left -= 1
    
    if not left: return time_val   
    else: return float('inf')     

N, M = map(int, input().split())
field = [list(map(int, input().split())) for i in range(N)]
virus_candis = []
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
time = float('inf')
left = 0

for i in range(N):
    for j in range(N):
        if field[i][j] == 2:
            virus_candis.append((i, j))
        if field[i][j] == 0:
            left += 1

for candi in combinations(virus_candis, M):
    time = min(time, BFS(candi, time, left))

if time == float('inf'): time = -1

print(time)