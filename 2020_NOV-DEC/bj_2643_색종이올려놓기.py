# 되도록 많은 장수의 색종이를 쌓는다.
# 새로 올리는 색종이는 맨 위의 색종이 밖으로 나가면 안 된다.
    # 크지 않아야 한다 -> 같은 건 된다
# 새로 올리는 색종이와 맨 위의 색종이 변들은 모두 평행해야 한다.
# (3, 5) -> 두 변의 길이가 3, 5

# 출력: 쌓을 수 있는 최대 색종이 장 수

# 90도 회전 가능하므로 x <= y가 되도록 x, y를 설정할 수 있다.
# dp[0] == 1
# dp[n] == dp[0] ~ dp[n-1] 중에서 가능한 것 + 1
    # y의 범위가 커버 가능한 것

import sys
input = sys.stdin.readline

def solution(N):
    p = sorted([sorted(map(int, input().split())) for i in range(N)])
    dp = [1 for i in range(N)]
    for i in range(1, N):
        for j in range(i):
            if p[i][1] >= p[j][1]: dp[i] = max(dp[i], dp[j]+1)
    print(max(dp))

if __name__ == '__main__':
    solution(int(input()))