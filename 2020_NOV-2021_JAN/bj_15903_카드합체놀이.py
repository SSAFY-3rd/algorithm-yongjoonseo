# 자연수 n장

# 두 카드를 골라 그 수를 더하고 고른 두 카드에 덮어쓴다. 
# -> 덮어쓴다는 건 더한다는 게 아니다.
# x != y 라는 건 단순히 다른 카드를 고른다는 뜻이다.
# 결과 - 놀이가 끝난 후 n장의 카드 수를 모두 더한 값

# 출력: 만들 수 있는 가장 작은 점수

# 최대 1000개의 카드, 최대 카드합체 15000회
# 그냥 매번 가장 작은 두 카드 더하는 식으로 해도 될듯. => 안됨

# n, m = map(int, input().split())
# cards = list(map(int, input().split()))

# for i in range(m):
#     min1 = min(cards)
#     midx1 = cards.index(min1)
#     min2 = float('inf')
#     midx2 = 0
#     for j in range(len(cards)):
#         if j != midx1 and cards[j] < min2:
#             min2 = cards[j]
#             midx2 = j
    
#     temp_res = min1 + min2
#     cards[midx1] = temp_res
#     cards[midx2] = temp_res

# print(sum(cards))

# =>> 시간 초과

from heapq import heappop, heappush

n, m = map(int, input().split())
raw_cards = list(map(int, input().split()))

cards = []
for card in raw_cards:
    heappush(cards, card)

for i in range(m):
    min1 = heappop(cards)
    min2 = heappop(cards)
    res = min1 + min2
    for j in range(2):
        heappush(cards, res)

print(sum(cards))

# 통과