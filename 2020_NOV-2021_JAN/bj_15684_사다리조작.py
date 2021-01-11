# index 1부터 시작
# 사다리는 연속하거나 접하면 안 된다.

# 출력: i번 세로선의 결과가 i가 나오는 최소 가로선 개수
#     정답이 3보다 크면 -1 출력, 불가능하면 -1 출력

# 세로선 최대 10개, 가로선 위치 최대 30
# 300 * (210 * 210C2 * 210C3)
# 좀 더 효율적인 방법을 찾아보자.
# 일단 조합으로 가능한 가로선마다 구해서 해보긴 해보자.

# 세로선 하나하나가 각각의 열이 되도록 행렬을 만든다.
#   H x (N + 2, 양 끝)
# 1. 가능한 가로선을 구하는 조합
# 2. 처음부터 끝까지 세로선이 해당 숫자로 가는지 체크하는 함수
# 가능한 때 곧바로 최솟값을 출력한다.

def combi(arr, start, r):
    for i in range(start, len(arr) - r + 1):
        if r == 1:
            yield [arr[i]]
        else:
            for j in combi(arr, i+1, r-1):
                is_possible = True
                for y, x in j:
                    if y == arr[i][0] and x-1 <= arr[i][1] <= x+1:
                        is_possible = False
                        break
                if not is_possible: continue
                yield [arr[i]] + j

def check(N, H):
    for i in range(1, N+1):
        y, x = 0, i
        while y < H:
            if field[y][x][0]: x -= 1
            elif field[y][x][1]: x += 1
            y += 1
        if x != i: return False
    return True

N, M, H = map(int, input().split())
field = [[[0,0] for i in range(N+2)] for j in range(H)]
candis = []
result = float('inf')

for _ in range(M):
    a, b = map(int, input().split())
    field[a-1][b][1] = 1
    field[a-1][b+1][0] = 1

for i in range(H):
    for j in range(1, N):
        if field[i][j][0] or field[i][j+1][0] or field[i][j+1][1]: continue
        else: candis.append((i,j))

if check(N, H):
    print(0)
else:
    found = False
    for i in range(1, 4):
        for case in combi(candis, 0, i):
            for y, x in case:
                field[y][x][1] = 1
                field[y][x+1][0] = 1
            if check(N, H):
                found = True
                print(i)
                break
            for y, x in case:
                field[y][x][1] = 0
                field[y][x+1][0] = 0
            if found: break
        if found: break
    else:
        print(-1)

# >> Python 시간 초과, PyPy 통과





# for _ in range(len(field)):
#     print(*field[_])
# print(candis)
# for candi in combi(candis, 0, 3):
#     print(candi)

# print(candis)
# a = [1,2,3,4]
# for _ in combi(a, 0, 3):
#     print(_)


# (가로선) 세로출발 -> 세로도착
# 1번: (1) 1 -> 2 / (3) 2 -> 3
# 2번: (1) 2 -> 1 / (5) 1 -> 2
# 3번: (2) 3 -> 4 / (5) 4 -> 5
# 4번: (2) 4 -> 3 / (3) 3 -> 2 / (5) 2 -> 1
# 5번: (5) 5 -> 4

# 1번: 1, 5
# 2번: 1, 3
# 3번: 2, 3
# 4번: 2, 5
# 5번: 5


