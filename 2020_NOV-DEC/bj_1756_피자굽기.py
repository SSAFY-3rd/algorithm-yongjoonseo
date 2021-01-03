# 제멋대로인 오븐에 피자 반죽을 넣는다

# 출력: 가장 마지막 피자 반죽의 깊이

# 이전에 들어간 피자보다 이번에 들어갈 피자가 작거나 같다면
    # 단순히 한 층 쌓는 격이다.
    # 1, 2, 3, 4 이런 식으로 쌓으면 불리함
# 어떤 피자보다 작은 오븐의 층을 구해서 쌓는다.
    # 300000, 299999, 299998 이런 식으로 쌓으면 불리함
# 두 방법을 혼용해본다.

# 1. 오븐 각각의 지름이 가장 먼저 나타나는 층을 저장한다.
# 2-1. 피자 반죽의 지름이 d라면 그보다 오븐 지름이 작은 층 중에
    # 가장 위에있는 층을 구해서 그 위에 쌓는다.
    # 구한 층이 현재 층보다 아래 있다면 단순히 한 층 쌓는다.
# 2-2. 피자 반죽이 이전 반죽보다 작거나 같으면 단순히 한 층 쌓는다.
# 3. 가장 마지막 피자 반죽의 깊이를 구한다.

# 1. 오븐 저장해두는 배열 oven
# 2. 오븐 지름마다 가장 먼저 나타나는 층 저장하는 딕셔너리 where
# 3. 현재 피자 쌓을 층 나타내는 정수 D
# 4. 피자 저장해두는 배열 pizza

# def solution(D, N):
#     oven = list(map(int, input().split()))
#     where = dict()

#     for i in range(len(oven)):
#         if not where.get(oven[i]):
#             where[oven[i]] = i+1
    
#     pizza = list(map(int, input().split()))
#     before = pizza[0]

#     if before == 1: D -= 1
#     else:
#         for j in range(1, before):
#             floor = where.get(j)
#             if floor: D = floor - 2
#             else: D -= 1
    
#     for i in range(1, len(pizza)):
#         if D <= 0: 
#             print(0)
#             break
#         if pizza[i] <= before:
#             D -= 1
#             continue
#         min_d = D
#         for j in range(1, pizza[i]):
#             floor = where.get(j)
#             if floor: min_d = min(min_d, floor)
#         if min_d <= D:
#             D = min_d - 2
#         else: D -= 1
#         before = pizza[i]
#     else:
#         print(D+1)

# if __name__ == '__main__':
#     solution(*map(int, input().split()))

# >> 시간 초과

# 큰 것 작은 것 큰 것 순으로 들어갔을 때도 연산이 많이 된다.

# before - 이전에 나온 피자 크기중 가장 큰 것
import sys
input = sys.stdin.readline

def solution(D, N):
    oven = list(map(int, input().split()))
    where = dict()

    for i in range(len(oven)):
        if not where.get(oven[i]):
            where[oven[i]] = i+1
    
    pizza = list(map(int, input().split()))
    before = pizza[0]

    if before == 1: D -= 1
    else:
        for j in range(1, pizza[0]):
            floor = where.get(j)
            if floor: D = floor - 2
            else: D -= 1
    
    for i in range(1, len(pizza)):
        if D <= 0: 
            print(0)
            break
        if pizza[i] <= before:
            D -= 1
            continue
        min_d = D
        for j in range(before, pizza[i]):
            floor = where.get(j)
            if floor: 
                if min_d > floor:
                    min_d = floor
                    if before < pizza[i]: before = pizza[i]
        if min_d <= D:
            D = min_d - 2
        else: D -= 1
    else:
        print(D+1)

if __name__ == '__main__':
    solution(*map(int, input().split()))