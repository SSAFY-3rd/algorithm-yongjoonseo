# 체크할 조건
# 최대 1000글자

# 두 문자열을 비교
# 문자열이 같은 경우: 대각선 왼쪽 + 1 (이전 부분까지의 문자열 비교 LCS + 1)
# 문자열이 다른 경우: max(왼쪽, 위쪽) (두 경우 중 LCS가 더 큰것)


def solution(str1, str2):
    n, m = len(str1), len(str2)
    dp = [[0] * m for i in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if str1[i] == str2[j]: dp[i][j] = dp[i-1][j-1] + 1
            else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp[-1][-1])

if __name__ == '__main__':
    solution(' '+input(), ' '+input())



a=input()
b=input()
T=[0]*300
row=0
X=0
al = len(a)
bl = len(b)
for i in range(al):
    T[ord(a[i])]+=(2**i)
for i in range(al):
    if(a[i]==b[0]):
        row+=(2**i)
        break
for i in range(1, bl):
    X = T[ord(b[i])]|row
    row=X&((X-(row*2+1))^X) # ??

cnt = 0
while(row):
    cnt+=(row%2)
    row//=2

print(cnt)