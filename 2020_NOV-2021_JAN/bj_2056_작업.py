# N개 작업, 각 작업마다 정수의 시간이 걸린다.
# 1~K-1번 작업 중에 K번 작업의 선행 관계에 있는 작업이 있다.
# 모든 작업을 완료하기 위한 최소 시간을 구하라
# 선행 관계가 없는 작업은 동시 수행 가능.

# 출력: 모든 작업을 완료하기 위한 최소 시간

# 체크할 조건
# 3 <= N <= 10000, 1 <= t <= 100
# 선행 관계가 없는 작업은 동시 수행 가능
# 선행 관계에 있는 건 먼저 완료되어야 한다.
    # k번 작업 - 1~k-1 작업 중 x개
# 입력이 1번 작업부터 순차적으로 주어진다.

# dp[n] - n번 작업까지 모두 하는데 소요되는 시간.
# 선행 작업 중 가장 오래 걸리는 시간 + 현재 시간으로 갱신.
# max(dp) 출력

import sys
input = sys.stdin.readline

def solution(N):
    dp = [0]
    for i in range(N):
        inp = list(map(int, input().split()))
        val, num, lst = inp[0], inp[1], inp[2:]
        dp.append(val + dp[max(lst, key=lambda x: dp[x], default=0)])
    print(max(dp))

if __name__ == '__main__':
    solution(int(input()))