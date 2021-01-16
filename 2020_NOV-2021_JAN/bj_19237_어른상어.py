# 1 이상 M 이하의 자연수 상어
# 1이 가장 강력한 상어
# N x N 격자
# 상어에 따라, 바라보는 방향에 따라 이동 방향의 우선순위가 다르다
#     1. 아무 냄새가 없는 칸
#     2. 자신의 냄새가 있는 칸
#         - 가능한 칸이 여러 개면 특정 우선순위를 따른다

# 출력: 1번 상어만 격자에 남게 되는 시간
#     1000초가 넘어도 다른 상어가 격자에 남아있다면 -1 출력

# 1. 상어의 위치 저장 2차원 배열 loc
# 2. 상어의 이동 우선순위 저장 배열 directions
# 3. 상어 번호 & 냄새 남아있는 배열 trace (빈칸: [0, 0])
#     냄새가 있는 좌표를 따로 set에 저장해두며 갱신 (trace_left)
# 4. 상어번호: 좌표, 방향 저장하는 딕셔너리 shark {1: (2, 0, 4)}
# 모든 상어를 한번씩 이동시키며 1, 3, 4를 갱신한다.
#     4에서 쫒겨난 상어는 없애버린다.

def move(num, ny, nx, y, x, d): # loc, trace, shark 갱신
    global k
    loc[ny][nx] = num
    loc[y][x] = 0
    trace[ny][nx][0], trace[ny][nx][1] = num, k
    trace_left.add((ny, nx))
    shark[num] = (ny, nx, d)

def add_temp(num, ny, nx, y, x, d):
    if temp.get((ny, nx)):
        temp.get((ny, nx)).append((num, ny, nx, y, x, d))
    else:
        temp[(ny, nx)] = [(num, ny, nx, y, x, d)]

N, M, k = map(int, input().split())
loc = [[0 for i in range(N)] for j in range(N)]
directions = [0] + [[0] + [[] for j in range(4)] for k in range(M)]
trace = [[[0, 0] for i in range(N)] for j in range(N)]
trace_left = set()
shark = dict()
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j]:
            loc[i][j] = line[j]
            shark[line[j]] = (i, j, 0)
            trace[i][j][0], trace[i][j][1] = line[j], k
            trace_left.add((i, j))

dir_init = list(map(int, input().split()))
for i in range(1, len(dir_init) + 1):
    y, x, zero = shark.get(i)
    shark[i] = (y, x, dir_init[i-1])

for i in range(1, M+1):
    for j in range(1, 5):
        directions[i][j] = list(map(int, input().split()))

temp = dict()
for t in range(1, 1001):
    update = trace_left.copy()

    for num in shark.keys():
        y, x, d = shark.get(num)
        direc = directions[num][d]
        has_blank = False
        for i in range(4):
            ny = y + dy[direc[i]]
            nx = x + dx[direc[i]]
            if 0 <= ny < N and 0 <= nx < N and not trace[ny][nx][0]:
                has_blank = True
                add_temp(num, ny, nx, y, x, direc[i])
                break
        if not has_blank:
            for i in range(4):
                ny = y + dy[direc[i]]
                nx = x + dx[direc[i]]
                if 0 <= ny < N and 0 <= nx < N and trace[ny][nx][0] == num:
                    add_temp(num, ny, nx, y, x, direc[i])
                    break

    # trace 시간 갱신
    for y, x in update:
        trace[y][x][1] -= 1
        if not trace[y][x][1]:
            trace[y][x][0] = 0
            trace_left.remove((y, x))

    for coor in temp.keys():
        if len(temp.get(coor)) == 1: move(*temp.get(coor)[0])
        else:
            lst = sorted(temp.get(coor))
            move(*lst[0])
            for j in range(1, len(lst)):
                shark.pop(lst[j][0])

    if len(shark) == 1 and shark.get(1):
        break

    temp.clear()
    # print('time :', t)
    # print('shark :', shark)
    # print('trace')
    # for _ in range(len(trace)):
    #     print(*trace[_])
else:
    t = -1

print(t)


# print('loc')
# for _ in range(len(loc)):
#     print(*loc[_])
# print('directions :', directions)
# print('trace')
# for _ in range(len(trace)):
#     print(*trace[_])
# print('trace_left :', trace_left)
# print('shark :', shark)
