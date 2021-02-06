# 정렬한 후 스위핑.
# 현재 위치 now
# e - now의 값을 더해간다.
# now가 s보다 작으면 now = s
# now가 s보다 크면 now 그대로 사용
# 매번 now를 e로 갱신

import sys
input = sys.stdin.readline

def solution(N):
    lst = [list(map(int, input().split())) for i in range(N)]
    lst.sort()
    now = -float('inf')
    result = 0
    for i in range(N):
        s, e = lst[i]
        if now < s: now = s
        if now < e:
            result += e - now
            now = e
    print(result)

if __name__ == '__main__':
    solution(int(input()))