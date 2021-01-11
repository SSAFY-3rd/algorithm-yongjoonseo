# 각 물고기는 번호 & 방향 가짐
# 4 X 4 공간, 1 <= 번호 <= 16, 자연수
# 두 물고기는 다른 번호
# 8방향
# 청소년 상어 - 0,0 물고기부터 시작, (0,0에 있던 물고기 방향)
# 물고기는 한 칸 이동, 그다음 상어 이동
# 상어 or 밖으로 나가면 못감, 이동할 수 있을 때까지 45도 반시계 회전
# 다른 물고기 칸으로 이동하면 서로 위치바꿈
# 상어 - 여러 개 칸 이동 가능, 물고기 있는 칸으로만 이동가능

# 출력: 상어가 먹을 수 있는 물고기 번호 합의 최댓값

# 상어가 먹은 물고기 번호 백트래킹 해야할듯..?
# field - 물고기 없음: 0, 물고기: 튜플, 상어: -1
# 1. 번호 작은 물고기부터 선택 & 이동
    # 좌표는 번호를 index로 해서 배열에 넣어두기
    # 방향도 함께 넣어두기 (0부터 시작)
# 2. 상어 이동 & 물고기 번호 합 (백트래킹)

from copy import deepcopy

def move_fish(field, coor):
    global d

    for i in range(1, 17):
        if coor[i]:
            fy, fx, direc = coor[i]
            for j in range(8):
                ny = fy + d[(direc + j) % 8][0]
                nx = fx + d[(direc + j) % 8][1]
                if 0 <= ny < 4 and 0 <= nx < 4 and field[ny][nx] != -1:
                    if field[ny][nx]:
                        tar_num, tar_dir = field[ny][nx]
                        field[fy][fx], field[ny][nx] = field[ny][nx], field[fy][fx]
                        field[ny][nx][1] = (direc + j) % 8 # field에서 방향
                        coor[i][0], coor[tar_num][0] = coor[tar_num][0], coor[i][0]
                        coor[i][1], coor[tar_num][1] = coor[tar_num][1], coor[i][1]
                        coor[i][-1] = (direc + j) % 8
                    else:
                        field[ny][nx] = field[fy][fx]
                        field[ny][nx][1] = (direc + j) % 8
                        field[fy][fx] = 0
                        coor[i] = [ny, nx, (direc + j) % 8]
                    break

def shark(y, x, inp, raw_field, raw_coor):
    global result
    field = deepcopy(raw_field)
    coor = deepcopy(raw_coor)
    n, direc = field[y][x]

    field[y][x] = -1
    coor[n] = 0
    val = inp + n
    move_fish(field, coor)

    ny = y + d[direc][0]
    nx = x + d[direc][1]

    while 0 <= ny < 4 and 0 <= nx < 4:
        if field[ny][nx]:
            field[y][x] = 0
            shark(ny, nx, val, field, coor)
        ny += d[direc][0]
        nx += d[direc][1]
    
    result = max(result, val)

raw_coor = [0 for i in range(17)]
d = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
raw_field = [[0 for i in range(4)] for j in range(4)]
result = -1

for i in range(4):
    lst = list(map(int, input().split()))
    for j in range(0, 8, 2):
        raw_coor[lst[j]] = [i, j//2, lst[j+1]-1]
        raw_field[i][j//2] = [lst[j], lst[j+1]-1]

shark(0, 0, 0, raw_field, raw_coor)
print(result)
