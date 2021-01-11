# k라는 예산 안에서 친구에게 돈을 주어 모든 학생을 친구로 만든다.

# 출력: 모든 학생을 친구로 만들 수 있는 최소비용
    # 불가능하면 Oh no 출력

# 모든 학생과 친구가 되어야 한다.
    # = 연결된 누군가와는 친구가 되어야 한다.
    # 그 연결된 누군가는 최소비용을 가지고 있어야 한다.
# 1. 친구비를 낮은 순으로 정렬한다.
# 2. 그 친구를 매수하고 연결된 모든 친구는 친구라고 한다.
    # xx 이때 연결된 친구는 모두 매수한 친구를 가리키도록 갱신한다.

# 친구비, 인덱스 배열 people
# 친구관계 나타내는 배열 rel
# 꼭대기 매수친구 가리키는 배열 head

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def update(idx):
    global left

    for p in rel[idx]:
        if not head[p]:
            head[p] = 1
            left -= 1
            update(p)

N, M, k = map(int, input().split())
people = [[0, i] for i in range(N+1)]
rel = [[] for i in range(N+1)]
head = [0 for i in range(N+1)]
left = N
init_k = k

inp = list(map(int, input().split()))
for i in range(len(inp)):
    people[i+1][0] = inp[i]

for i in range(M):
    a, b = map(int, input().split())
    rel[a].append(b)
    rel[b].append(a)

people.sort()

for i in range(1, N+1):
    price, idx = people[i]
    if not left or k < price: break

    if not head[idx]:
        head[idx] = 1
        left -= 1
        k -= price
        update(idx)

if left: print('Oh no')
else: print(init_k - k)



# while k > 0 and left:

# print(left)
# print(people)
# print(rel)
# print(head)