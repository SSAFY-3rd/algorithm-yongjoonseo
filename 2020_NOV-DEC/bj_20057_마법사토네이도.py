# idx 1부터 시작 (==(0,0) 까지 이동한후 소멸)
# 항상 가운데부터 토네이도 출발. (가운데의 모래 양은 0)
# N은 홀수

# 출력: 격자 밖으로 나간 모래 양

# 1. 토네이도 이동 방향 (날아갈 위치 지정 & 방향)
# 2. 모래 날아가는 것
    # -> 격자 밖으로 나가는지 여부 boolean
    # -> 방향도 함께 체크

# 1 1 2 2 3 3 4 4 4 => N = 5
# 1 1 2 2 3 3 4 4 5 5 6 6 6 => N = 7

def idx(n):
    y = x = n // 2
    num = 1
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]
    num_cnt = 0 # num_cnt가 num이 되면 방향 바꾸기
    dir_cnt = 0 # dir_cnt가 2가 되면 num += 1
    direc = 0
    while num < n:
        if num == n: break
        y += dy[direc]
        x += dx[direc]
        yield y, x, direc
        num_cnt += 1
        if num_cnt == num:
            direc = (direc + 1) % 4
            dir_cnt += 1
            num_cnt = 0
        if dir_cnt == 2:
            num += 1
            dir_cnt = 0
    else:
        for _ in range(1, n):
            y += dy[direc]
            x += dx[direc]
            yield y, x, direc

def sand(y, x, direc, amount):
    global N, field
    field[y][x] = 0
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]
    idx = 1 if direc & 1 else 0
    out = 0
    # 1% = dy, dx - 1칸 // dy가 0이면 y로 +-1, dx가 0이면 x로 +-1
    # 7% = dy가 0이면 dy +- 1, dx 상동
    # 2% = dy가 0이면 dy +- 2
    # 10% = dy, dx + 1칸 // dy가 0이면 y로 +-1, dx 상동
    # 5% = dy, dx + 2칸
    # a = dy, dx + 1칸
    # direc & 1 => dx가 0
    p = [0.01, 0.01, 0.07, 0.07, 0.02, 0.02, 0.1, 0.1, 0.05, 0]
    # res = [0 for _ in range(len(p))]
    res = 0

    for i in range(len(p)):
        temp_amount = int(p[i] * amount)
        if i in (0, 1):
            d = (direc + 3) % 4 if i == 0 else (direc + 1) % 4
            ny = y - dy[direc] + dy[d]
            nx = x - dx[direc] + dx[d]
        elif i in (2, 3):
            d = (direc + 3) % 4 if i == 2 else (direc + 1) % 4
            ny = y + dy[d]
            nx = x + dx[d]
        elif i in (4, 5):
            d = (direc + 3) % 4 if i == 4 else (direc + 1) % 4
            ny = y + dy[d] * 2
            nx = x + dx[d] * 2
        elif i in (6, 7):
            d = (direc + 3) % 4 if i == 6 else (direc + 1) % 4
            ny = y + dy[direc] + dy[d]
            nx = x + dx[direc] + dx[d]
        elif i == 8:
            ny = y + dy[direc] * 2
            nx = x + dx[direc] * 2
        else:
            ny = y + dy[direc]
            nx = x + dx[direc]
            # temp_amount = amount - sum(res)
            temp_amount = amount - res
        
        # res[i] = temp_amount
        res += temp_amount
        if 0 <= ny < N and 0 <= nx < N:
            field[ny][nx] += temp_amount
        else:
            out += temp_amount

    return out


N = int(input())
field = [list(map(int, input().split())) for i in range(N)]
result = 0

for y, x, direc in idx(N):
    result += sand(y, x, direc, field[y][x])

print(result)