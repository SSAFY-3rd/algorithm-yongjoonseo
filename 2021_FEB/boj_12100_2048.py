# 출력: 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록

# 체크할 조건
# NxN
# 1 <= N <= 20
# 0은 빈 칸

# 4방향 중복순열 - 4 ** 5 == 1024가지 경우.
    # 백트래킹.
# 1. 왼쪽 방향으로의 블록 이동 & 병합
    # (board, N) -> None
# 2. 방향 전환 (회전)
    # (board, direc) -> board
    # 왼쪽 방향으로 이동 -> 회전안함 (0)
    # 오른쪽 방향으로 이동 -> 좌우반전 (1)
    # 위쪽 방향으로 이동 -> 반시계 90도 (2)
    # 아래쪽 방향으로 이동 -> 시계 90도 (3)
    # 연산 후 되돌리기 (0 X, 1 - 1, 2 - 3, 3- 2)
# 3. 가장 큰 블록 값 갱신

def move(board, N):
    for i in range(N):
        j = merged = now = 0
        while j < N:
            while j < N and not board[i][j]:
                j += 1
            if j == N: break
            board[i][now] = board[i][j]
            if now < j: board[i][j] = 0
            if now == 0:
                now += 1
            else:
                if board[i][now-1] == board[i][now] and merged < now:
                    board[i][now-1] *= 2
                    board[i][now] = 0
                    merged = now
                else:
                    now += 1
            j += 1

def rotate(board, d, N):
    if d == 1:
        for i in range(N):
            board[i].reverse()
    elif d == 2:
        for i in range(N//2):
            for j in range((N+1)//2):
                board[i][j], board[N-1-j][i], board[N-1-i][N-1-j], board[j][N-1-i] = board[j][N-1-i], board[i][j], board[N-1-j][i], board[N-1-i][N-1-j]
    elif d == 3:
        for i in range(N//2):
            for j in range((N+1)//2):
                board[i][j], board[N-1-j][i], board[N-1-i][N-1-j], board[j][N-1-i] = board[N-1-j][i], board[N-1-i][N-1-j], board[j][N-1-i], board[i][j]
    return board

def maxblock(board, N):
    global result
    for i in range(N):
        for j in range(N):
            if board[i][j] > result:
                result = board[i][j]

def BT(board, N, depth):
    if depth == 5:
        maxblock(board, N)
        return
    for i in range(4):
        next_board = [lst[:] for lst in board]
        rotate(next_board, i, N)
        move(next_board, N)
        if i == 1:
            rotate(next_board, i, N)
        elif i == 2:
            rotate(next_board, 3, N)
        elif i == 3:
            rotate(next_board, 2, N)
        BT(next_board, N, depth+1)

def solution(N):
    field = [list(map(int, input().split())) for i in range(N)]
    BT(field, N, 0)
    print(result)

if __name__ == '__main__':
    result = -1
    solution(int(input()))

# 2차원 배열 deepcopy 이용 복사 vs 슬라이싱 이용한 복사 시간차이
    # 652ms vs 352ms