# 행렬을 곱하는 순서에 따라 곱셈 연산 수가 달라진다.
# (N x M 행렬) X (M x K 행렬)의 연산 수: N x M x K

# 출력: 모든 행렬을 곱하는데 필요한 연산 횟수의 최솟값

# 체크할 조건
# 행렬의 개수 N:  1 <= N <= 500
# 곱하는 순서가 달라지면 안 된다.

# 행렬의 개수가 1개면 곱셈 연산 0번
# 행렬의 개수가 2개면 곱셈 연산 경우의 수는 한 가지.
# 백트래킹을 하기엔 행렬의 개수가 너무 많다.
    # DP로 해결하자

# ABC -> AB + C / A + BC
# ABCD -> ABC + D / AB + CD / A + BCD
# ABCDE -> ABCD + E / ABC + DE / AB + CDE / A + BCDE
# dp[i][j] : 행렬 i ~ j까지 곱할 때 필요한 연산 횟수의 최솟값
# mat: 입력받은 행렬을 저장한 2차원 리스트
# dp[i][j] = min(dp[i][k] + dp[k+1][j] + mat[i][0] * mat[k+1][0] * mat[k+1][1]) (i <= k < j)

import sys
input = sys.stdin.readline

def solution(N):
    dp = [[0 for i in range(N)] for j in range(N)]
    mat = [list(map(int, input().split())) for i in range(N)]
    for length in range(1, N):
        for i in range(N - length):
            j = i + length
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][k] + dp[k+1][j] + mat[i][0] * mat[k+1][0] * mat[j][1], dp[i][j])
    print(dp[0][-1])

if __name__ == '__main__':
    solution(int(input()))
