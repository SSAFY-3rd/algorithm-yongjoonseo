# 사과를 먹으면 뱀 길이가 늘어난다.
# 벽 or 자기자신의 몸과 부딪히면 게임이 끝
# N x N

# 움직임
#   머리를 다음 칸에 위치
#   이동한 칸에 사과가 있다면 사과 없어지고 꼬리는 움직이지 않는다.
#   이동한 칸에 사과가 없다면 몸 길이를 줄여 꼬리가 위치한 칸을 비워준다.

# 출력: 게임이 끝나는 시간 (초)

# 보드 위 사과 - 2 / 뱀 위치 - 1 / 빈칸 - 0
# 뱀을 하나의 큐로 생각하고 좌표를 저장한다.
    # 조건에 맞춰서 요소를 빼고 field(board)에 표시한다.

from collections import deque


def solution(N):
    field = [[0 for i in range(N)] for j in range(N)]
    K = int(input())
    for k in range(K):
        y, x = map(int, input().split())
        field[y-1][x-1] = 2
    
    snake = deque()
    direc = [0 for i in range(10001)]
    for i in range(int(input())):
        t, d = input().split()
        direc[int(t)] = d
    
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    idx = 0
    ny, nx = 0, 1
    snake.append((0, 0))
    field[0][0] = 1
    t = 1
    while 0 <= ny < N and 0 <= nx < N and field[ny][nx] != 1:
        snake.append((ny, nx))
        if field[ny][nx] == 2:
            field[ny][nx] = 1
        elif field[ny][nx] == 1:
            break
        else:
            field[ny][nx] = 1
            a, b = snake.popleft()
            field[a][b] = 0
        
        if direc[t] == 'L':
            idx = (idx - 1) % 4
        elif direc[t] == 'D':
            idx = (idx + 1) % 4
        t += 1
        ny += dy[idx]
        nx += dx[idx]
    
    print(t)

if __name__ == '__main__':
    solution(int(input()))