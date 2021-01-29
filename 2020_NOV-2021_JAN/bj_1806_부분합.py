# 체크할 조건
# 10 <= N < 100000

# 투 포인터 알고리즘을 사용한다.
# S이상이 될 때 포인터의 길이 중 짧은 것으로 갱신.
# 부분합이 S이상이 되는 순간 시작점을 늘린다.
    # S이상인 동안 계속 늘린다.
# 부분합이 S보다 모자라면 끝점을 늘린다.

def solution(N, S):
    lst = list(map(int, input().split()))
    s, e = 0, 0
    result, sumval = 100001, lst[s]
    while s < N:
        if sumval < S:
            e += 1
            if e == N: break
            sumval += lst[e]
        else:
            result = min(result, e - s + 1)
            sumval -= lst[s]
            s += 1
            if s > e: break
    print(0) if result == 100001 else print(result)

if __name__ == '__main__':
    solution(*map(int, input().split()))