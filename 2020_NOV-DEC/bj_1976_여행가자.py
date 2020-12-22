# 출력: 여행 경로가 가능한지 여부 YES / NO

# 다른 도시를 경유해서 여행할 수도 있고, 중복해서 갈 수도 있다
# 경로를 하나하나 찾기엔 경우의 수가 너무 많아진다
# 도시들이 연결 되는지 여부만 따져서 모두 연결되면 YES 출력
# union-find 자료구조를 사용한다.

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

def solution():
    N = int(input())
    M = int(input())
    parents = [i for i in range(N)]
    ranks = [0 for i in range(N)]
    
    idx = 1
    for i in range(N):
        inp = list(map(int, input().split()))
        for j in range(idx, N):
            if inp[j]: union(i, j, parents, ranks)
    
    plan = list(map(int, input().split()))
    comp = find(plan[0] - 1, parents)
    for i in range(1, len(plan)):
        if find(plan[i]-1, parents) != comp:
            print('NO')
            return
    else:
        print('YES')

if __name__ == '__main__':
    solution()

# 76 ms


import sys
input = sys.stdin.readline


def find(x):
    if parents[x] == x: return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    xroot = find(x)
    yroot = find(y)
    if ranks[xroot] >= ranks[yroot]:
        parents[yroot] = xroot
    else:
        parents[xroot] = yroot
    if ranks[xroot] == ranks[yroot]:
        ranks[xroot] += 1

def solution():
    global parents, ranks
    N = int(input())
    M = int(input())
    parents = [i for i in range(N)]
    ranks = [0 for i in range(N)]
    
    idx = 1
    for i in range(N):
        inp = list(map(int, input().split()))
        for j in range(idx, N):
            if inp[j]: union(i, j)
    
    plan = list(map(int, input().split()))
    comp = find(plan[0] - 1)
    for i in range(1, len(plan)):
        if find(plan[i]-1) != comp:
            print('NO')
            return
    else:
        print('YES')

if __name__ == '__main__':
    solution()

# 84 ms (list global 선언)