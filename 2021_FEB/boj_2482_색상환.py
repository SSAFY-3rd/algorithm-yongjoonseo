# 출력: K개의 색을 고르는 경우의 수 % 1000000003

# 체크할 조건
# 인접한 두 색을 사용하지 않는다.
# 4 <= N <= 1000 (색의 개수)
# 1 <= K <= N (선택할 색의 개수)

# K >= (N+1) // 2 -> return 0
# dp[i][j] == i개의 색 중 j개를 인접하지 않게 고르는 경우의 수
# dp[i][j] = (dp[i-2][j-1]) + (dp[i-1][j])
    #        (이전 항 미포함)  (이전 항 포함)
# result: dp[N-1][K] (첫째항 미포함) + dp[N-3][K-1] (첫째항 포함)

DIV = 1000000003

def solution(N, K):
    if K > N // 2:
        print(0)
        return
    dp = [[0] * (K+1) for i in range(N+1)]
    for i in range(N+1):
        dp[i][0], dp[i][1] = 1, i
    for i in range(2, N+1):
        for j in range(1, K+1):
            dp[i][j] = (dp[i-2][j-1] + dp[i-1][j]) % DIV
    print((dp[N-1][K] + dp[N-3][K-1]) % DIV)

if __name__ == '__main__':
    solution(int(input()), int(input()))

# >> 정답 (212 ms)


# 서로 다른 n개에서 r개를 인접하지 않게 고르는 경우의 수 == n-r+1Cr
    # == 띄워줄 색상 개수 만큼 제외한 색 중에 r개 고르는 경우의 수
    # nCr == n! // (r! * (n-r)!)
    # (n-r+1)Cr == (n-r+1)! // (r! * (n-2*r+1)!)
# result: [N개에서 K개] - [첫 색깔과 마지막 색을 모두 택하는 경우]
    # (N-K+1)CK - (N-K-1)C(K-2)

DIV = 1000000003

def factorial(N, dp):
    if dp[N]: return dp[N]
    dp[N] = (N * factorial(N-1, dp))
    return dp[N]

def combination(n, r, dp):
    f = factorial
    return (f(n, dp) // (f(r, dp) * f(n-r, dp)))

def solution(N, K):
    if K > N // 2:
        print(0)
        return
    dp = [0] * (N+1)
    dp[0] = 1
    c = combination
    result = (c(N-K+1, K, dp) - c(N-K-1, K-2, dp)) % DIV
    print(result)

if __name__ == '__main__':
    solution(int(input()), int(input()))

# >> 정답 (72 ms)

# revised_combination == 서로 다른 n개에서 r개를 인접하지 않게 고르는 경우의 수
# revised_combination(n, r) == n-r+1Cr
# result: [N-1, K] + [N-3, K-1] (첫째항 미포함 & 첫째항 포함)

DIV = 1000000003

def factorial(N, dp):
    if dp[N]: return dp[N]
    dp[N] = (N * factorial(N-1, dp))
    return dp[N]

def revised_combination(n, r, dp):
    f = factorial
    return (f(n-r+1, dp) // (f(r, dp) * f(n-2*r+1, dp)))

def solution(N, K):
    if K > N // 2:
        print(0)
        return
    dp = [0] * (N+1)
    dp[0] = 1
    c = revised_combination
    result = (c(N-1, K, dp) + c(N-3, K-1, dp)) % DIV
    print(result)

if __name__ == '__main__':
    solution(int(input()), int(input()))

# >> 정답 (64 ms)