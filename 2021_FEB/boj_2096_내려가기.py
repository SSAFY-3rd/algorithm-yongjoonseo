# 출력: 최대 점수, 최소 점수

# 체크할 조건
# 1 <= N <= 100000
# 세 줄

# 최대인 경우, 최소인 경우 각각 3번씩 dp

# import sys
# input = sys.stdin.readline

# def solution(N):
#     raw = [list(map(int, input().split())) for i in range(N)]
#     dp_max = [[0] * 3 for i in range(N)]
#     dp_min = [[0] * 3 for i in range(N)]
#     dp_max[0] = raw[0].copy()
#     dp_min[0] = raw[0].copy()
#     for i in range(1, N):
#         dp_max[i][0] = max(dp_max[i-1][0], dp_max[i-1][1]) + raw[i][0]
#         dp_max[i][1] = max(dp_max[i-1]) + raw[i][1]
#         dp_max[i][2] = max(dp_max[i-1][1], dp_max[i-1][2]) + raw[i][2]
#         dp_min[i][0] = min(dp_min[i-1][0], dp_min[i-1][1]) + raw[i][0]
#         dp_min[i][1] = min(dp_min[i-1]) + raw[i][1]
#         dp_min[i][2] = min(dp_min[i-1][1], dp_min[i-1][2]) + raw[i][2]
#     print(max(dp_max[-1]), min(dp_min[-1]))

# if __name__ == '__main__':
#     solution(int(input()))

# >> 메모리 초과

import sys
input = sys.stdin.readline

def solution(N):
    line = list(map(int, input().split()))
    mx_line = line.copy()
    mn_line = line.copy()
    for _ in range(N-1):
        new_line = list(map(int, input().split()))
        mx_line = [
            max(mx_line[0], mx_line[1]) + new_line[0],
            max(mx_line) + new_line[1],
            max(mx_line[1], mx_line[2]) + new_line[2]
        ]
        mn_line = [
            min(mn_line[0], mn_line[1]) + new_line[0],
            min(mn_line) + new_line[1],
            min(mn_line[1], mn_line[2]) + new_line[2]
        ]
    print(max(mx_line), min(mn_line))

if __name__ == '__main__':
    solution(int(input()))