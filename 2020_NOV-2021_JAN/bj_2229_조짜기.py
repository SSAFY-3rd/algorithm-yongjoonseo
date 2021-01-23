# 실력 차이가 많이 나도록 조를 짠다
# 가장 점수가 높은 학생 - 가장 점수가 낮은 학생
# 나이 순으로 정렬해서 적당히 학생들을 나누는 방식
    # = 순차적으로 조를 짠다.

# 출력: 조가 잘 짜여진 정도의 최댓값

# 체크할 조건
# 1 <= N <= 1000

# dp[i] = k: 1~i+1, max(dp[i], dp[i-k] + abs(max(lst[i-k+1:i+1]) - min))

def solution(N):
    lst = list(map(int, input().split()))
    dp = [0] * N
    for i in range(1, N):
        for k in range(1, i+2):
            temp = lst[i-k+1:i+1]
            if k == i+1: k = i
            dp[i] = max(dp[i], dp[i-k] + abs(max(temp) - min(temp)))
    print(dp[-1])

if __name__ == '__main__':
    solution(int(input()))

# dp[i] : i번째까지 조가 잘 짜여진 최댓값
# i에서 1씩 빼면서 최댓값, 최솟값을 갱신하고 그때마다 dp[i+1] 갱신
    # 최댓값, 최솟값이 갱신되지 않으면 더 볼 필요 없음.

def solution(N):
    lst = list(map(int, input().split()))
    dp = [0] * (N+1)
    for i in range(N):
        dp[i+1] = dp[i]
        minval = maxval = lst[i]
        j = i-1
        while j >= 0 and (lst[j] < minval or lst[j] > maxval):
            minval, maxval = min(lst[j], minval), max(lst[j], maxval)
            dp[i+1] = max(dp[i+1], dp[j] + maxval - minval)
            j -= 1
    print(dp[-1])

if __name__ == '__main__':
    solution(int(input()))