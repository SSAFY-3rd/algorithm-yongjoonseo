# 카드 i개 카드백은 Pi원
# 카드 N개를 구매하려고 함

# 출력: N개의 카드를 구매하기 위해 지불할 금액의 최댓값

# n == 0 -> cards[0]
# n == i => 새로운 카드가 추가
    # -> dp[i-1] + cards[1] (1개짜리 카드팩)
    # -> dp[i-2] + cards[2] (2개짜리 카드팩)
    # -> dp(i-k) + cards[k] (k개짜리 카드팩) 

def solution(N):
    cards = [0] + list(map(int, input().split()))
    dp = [0 for i in range(N+1)]
    dp[1] = cards[1]
    for i in range(2, len(cards)):
        for k in range(1, i):
            dp[i] = max(dp[i], dp[i-k] + cards[k], cards[i])
    print(dp[-1])

if __name__ == '__main__':
    solution(int(input()))