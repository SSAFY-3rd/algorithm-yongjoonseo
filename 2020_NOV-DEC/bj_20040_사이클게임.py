# 평면상의 점 n개
# 어느 세 점도 일직선 위에 놓이지 않는다.
# 사이클: 한 끝점에서 모든 선분을 한 번씩만 지나 출발점으로 되돌아온다
# 사이클이 완성되었는지 판단하는 프로그램

# 출력: 
    # m번째 차례까지 하는 동안 이미 게임이 종료되었으면: 처음 번호
    # m번째 차례까지도 종료되지 않았으면 0출력

# 체크할 조건
# 0 <= n <= 500000 // 3 <= m <= 1000000
    # 입력이 많다 (m개)
# n개의 점은 0부터 n-1의 번호

# union-find 자료구조를 사용해본다.
# 새로 들어오는 a, b 둘다 이미 같은 집합에 있다면
    # find(a) == find(b)라면 사이클 완성

import sys
input = sys.stdin.readline

def find(x, parents):
    if parents[x] == x: return x
    parents[x] = find(parents[x], parents)
    return parents[x]

def union(x, y, parents, ranks):
    xroot = find(x, parents)
    yroot = find(y, parents)
    if ranks[xroot] >= ranks[yroot]:
        parents[yroot] = xroot
    else:
        parents[xroot] = yroot
    if ranks[xroot] == ranks[yroot]:
        ranks[xroot] += 1

def solution(n, m):
    parents = [i for i in range(n)]
    ranks = [0 for i in range(n)]
    result = 0
    found = False
    for i in range(1, m+1):
        a, b = map(int, input().split())
        if found: continue
        if find(a, parents) == find(b, parents):
            result = i
            found = True
        else:
            union(a, b, parents, ranks)
    print(result)

if __name__ == '__main__':
    solution(*map(int, input().split()))