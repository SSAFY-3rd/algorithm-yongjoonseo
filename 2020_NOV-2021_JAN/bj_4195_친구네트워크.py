# 출력: 친구 관계가 생길 때마다 두 사람의 친구 네트워크에 몇 명이 있는지

# union-find 자료구조를 이용하여 판단한다.
# parents - dict, 노드: [루트노드, 친구수]
# ranks - 노드: 랭크(트리의 깊이)


def find(x, parents):
    if parents.get(x)[0] == x: return parents.get(x)
    parents[x] = find(parents[x][0], parents)
    return parents[x]

def union(x, y, parents, ranks):
    xroot, xnum = find(x, parents)
    yroot, ynum = find(y, parents)
    if xroot == yroot: return
    if ranks[xroot] >= ranks[yroot]:
        parents[yroot][0] = xroot
        parents[xroot][1] += ynum
    else:
        parents[xroot][0] = yroot
        parents[yroot][1] += xnum
    if ranks[xroot] == ranks[yroot]:
        ranks[xroot] += 1

def solution():
    parents = dict()
    ranks = dict()
    for i in range(int(input())):
        f1, f2 = input().split()

        if not parents.get(f1):
            parents[f1] = [f1, 1]
            ranks[f1] = 1
        if not parents.get(f2):
            parents[f2] = [f2, 1]
            ranks[f2] = 1
        
        union(f1, f2, parents, ranks)

        print(find(f1, parents)[1])

if __name__ == '__main__':
    for _ in range(int(input())):
        solution()


# -----------------------


import sys
input = sys.stdin.readline


def find(x, parents):
    if parents[x] == x: return x
    parents[x] = find(parents[x], parents)
    return parents[x]

def howmany(x, parents, nums):
    if parents[x] == x: return nums[x]
    nums[x] = howmany(parents[x], parents, nums)
    return nums[x]

def union(x, y, parents, ranks, nums):
    xroot = find(x, parents)
    yroot = find(y, parents)
    if xroot == yroot: return
    x_num = howmany(x, parents, nums)
    y_num = howmany(y, parents, nums)
    if ranks[xroot] >= ranks[yroot]:
        parents[yroot] = xroot
        nums[xroot] += y_num
    else:
        parents[xroot] = yroot
        nums[yroot] += x_num
    if ranks[xroot] == ranks[yroot]:
        ranks[xroot] += 1

def solution():
    F = int(input())
    friends = dict()
    parents = []
    ranks = []
    nums = []
    idx = 0
    for i in range(F):
        s, e = input().split()
        if friends.get(s) == None:
            friends[s] = idx
            parents.append(idx)
            ranks.append(0)
            nums.append(1)
            idx += 1
        if friends.get(e) == None:
            friends[e] = idx
            parents.append(idx)
            ranks.append(0)
            nums.append(1)
            idx += 1
        union(friends[s], friends[e], parents, ranks, nums)

        print(howmany(friends[s], parents, nums))

if __name__ == '__main__':
    for t in range(int(input())):
        solution()