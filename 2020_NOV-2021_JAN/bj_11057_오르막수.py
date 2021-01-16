# 출력: 길이가 N인 오르막 수의 개수 % 10007

# 체크할 조건
# 수는 0으로 시작할 수 있다.
# 인접한 수가 같아도 오름차순이다.
# 1 <= N <= 1000

# 00 01 02 03 04 05 06 07 08 09
# 11 12 13 14 15 16 17 18 19
# 22 23 24 25 26 27 28 29
# 33 34 35 36 37 38 39
# 44 45 46 47 48 49
# 55 56 57 58 59
# 66 67 68 69
# 77 78 79
# 88 89
# 99

# 55 + 45 + 36 + 28 + 21 + 15 + 10 + 6 + 3 + 1 = 220

# DP로 풀어보자.
# 0 ~ 9 배열에 길이가 1부터 N까지 오르막 수 개수를 저장한다.
    # 0은 sum(0~9), 1은 sum(1~9)와 같은 방식.
# (a + b) % c = ((a % c) + (b % c)) % c

def solution(N):
    dp = [1 for i in range(10)]
    for i in range(1, N):
        for j in range(10):
            dp[j] = sum(dp[j:]) % 10007
    print(sum(dp) % 10007)

if __name__ == '__main__':
    solution(int(input()))



# ?????????????
k=int(input())
result=1
for i in range(9+k,9,-1):
    result*=i
for i in range(1,k+1):
    result//=i
print(result%10007)