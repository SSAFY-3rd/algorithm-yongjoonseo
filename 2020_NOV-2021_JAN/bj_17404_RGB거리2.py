# 1번부터 N번 집
# 빨, 초, 파 중 하나의 색

# 출력: 모든 집을 칠하는 비용의 최솟값

# 체크할 조건
# 2 <= N <= 1000
# 1번 집 != 2, N번 집
# N번 집 != N-1, 1번 집
# i번 집 != i-1, i+1 (2 <= i <= N-1)
    # 양 옆의 집 색과 같으면 안 된다.

# 최솟값이니까 백트래킹으로 한번 짜보자.

# import sys
# input = sys.stdin.readline

# def BT(houses, visited, val, hi, ci):
#     global result
#     if val >= result: return
#     if hi == len(houses):
#         if result > val: result = val
#         return
#     for i in range(3):
#         if i == ci: continue
#         if hi == len(houses) - 1 and visited[i]: continue
#         BT(houses, visited, val + houses[hi][i], hi+1, i)

# def solution(N):
#     global result
#     houses = [list(map(int, input().split())) for i in range(N)]
#     visited = [0] * 3
#     for i in range(3):
#         visited[i] = 1
#         BT(houses, visited, houses[0][i], 1, i)
#         visited[i] = 0
#     print(result)

# if __name__ == '__main__':
#     result = float('inf')
#     solution(int(input()))

# >> 시간 초과

# 1번 집이 빨, 초, 파인 경우 3가지에 대해 dp
# dp[i][0~2]: i번째 집까지 최솟값
    # 빨, 초, 파 3가지 경우
    # dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + lst[i][0]
    # dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + lst[i][1]
    # dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + lst[i][2]
    # 0으로 시작할 땐 dp[n-1][1], dp[n-1][2] 중 최솟값.

import sys
input = sys.stdin.readline

def solution(N):
    lst = [list(map(int, input().split())) for i in range(N)]
    result = float('inf')
    for i in range(3):
        dp = [[float('inf')] * 3]
        dp[0][i] = lst[0][i]
        for j in range(1, N):
            dp.append([float('inf')] * 3)
            for k in range(3):
                dp[j][k] = min(dp[j-1][(k+1)%3], dp[j-1][(k+2)%3]) + lst[j][k]
        result = min(result, dp[N-1][(i+1)%3], dp[N-1][(i+2)%3])
    print(result)

if __name__ == '__main__':
    solution(int(input()))