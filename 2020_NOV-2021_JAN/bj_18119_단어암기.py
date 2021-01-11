# 모두 소문자
# N개의 단어, M개의 쿼리
# 1 x - 알파벳 x를 잊는다
# 2 x - 알파벳 x를 기억해 낸다.
# 단어 안의 모든 알파벳을 알 때 그 단어를 완전히 안다.
# 모음은 절대 잊지 않는다.

# 출력: 각 쿼리마다 완전히 알고있는 단어의 개수를 출력

# 각 단어마다 검사하는 방식은 시간이 너무 오래 걸릴 것 같다.
# 단어에 모르는 글자가 하나라도 있으면 모르는 단어가 된다.
# 처음에 모든 단어에 숫자를 매겨서 a-z key에 해당 숫자를 저장한다.

# 1. a-z를 0-25로 변환하는 dict char2num
# 2. 0-25에 어떤 단어들이 속하는지 각각의 집합을 저장하는 list store
    # 0번째 요소: 초기에 저장한 집합 / 1번째 요소: 갱신하는 집합
# 3. 알고있는 단어의 집합 known 
    # 쿼리로 1이 들어오면 intersection을 구해서 차집합을 구하고 갱신
    # 2가 들어오면 갱신한 집합으로 합집합 연산

# 이렇게하면 빈 곳이 생긴다..

# import sys
# input = sys.stdin.readline

# def solution(N, M):
#     char2num = dict()
#     store = [[set(), set()] for i in range(26)]
#     known = set()

#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     for i in range(26):
#         char2num[alphabet[i]] = i

#     num = 1
#     for i in range(N):
#         temp_set = set()
#         for char in input().rstrip('\n'):
#             temp_set.add(char)
#         for char in temp_set:
#             idx = char2num.get(char)
#             store[idx][0].add(num)
#         known.add(num)
#         num += 1
    
#     for j in range(M):
#         o, x = input().split()
#         idx = char2num.get(x)
#         if o == '1':
#             temp = known & store[idx][0]
#             known -= temp
#             store[idx][1] = temp
#         else:
#             known.update(store[idx][1])
#         print(len(known))

# if __name__ == '__main__':
#     solution(*map(int, input().split()))



# 26차원 array를 만든다면?
    # 빈 array 크기가 너무 크고 시간도 오래 걸린다.

# def make_store(n, lst):
#     if n == 1: return
#     lst[0] = [[], []]
#     lst[1] = [[], []]
#     make_store(n-1, lst[0])
#     make_store(n-1, lst[1])    

# def solution(N, M):
#     char2num = dict()
#     store = [[], []]
#     make_store(25, store)
#     # store = [[set(), set()] for i in range(26)]
#     print(store)

#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     for i in range(26):
#         char2num[alphabet[i]] = i

# if __name__ == '__main__':
#     solution(*map(int, input().split()))


# 각 알파벳이 존재하면 1, 존재하지 않으면 0으로 하자.
# 고유 알파벳만 구해서 딕셔너리에 저장해보자.
    # 최대  크기의 딕셔너리가 나올것.


# def solution(N, M):


# if __name__ == '__main__':
#     solution(*map(int, input().split()))





# 혹시 그냥 비트마스크 연산이 빨라서 전부 탐색해도 되는 건 아닐까?
    # 모음은 빼고 해보자

# def solution(N, M):
#     known = []
#     unknown = []

#     vowels = 'aeiou'
#     cons = 'bcdfghjklmnpqrstvwxyz'
    
#     weight = dict()
#     for i in range(len(cons)):
#         weight[cons[i]] = i
    
#     # print(weight)

#     for i in range(N):
#         temp = set()
#         for char in input():
#             temp.add(char)
                
#         num = 0
#         for char in temp:
#             if char in vowels: continue
#             num += 1 << weight.get(char)
        
#         known.append(num)
    
#     current = (1 << 21) -1
#     for i in range(M):
#         o, x = input().split()
#         if o == '1':
#             current -= 1 << weight.get(x)
#             for j in range(len(known) - 1, -1, -1):
#                 # print('current & known', current, known[j], current & known[j])
#                 if current & known[j] != known[j]:
#                     unknown.append(known.pop(j))
#         else:
#             current += 1 << weight.get(x)
#             for j in range(len(unknown) - 1, -1, -1):
#                 if current & unknown[j] == unknown[j]:
#                     known.append(unknown.pop(j))
        
#         print(len(known))

# if __name__ == '__main__':
#     solution(*map(int, input().split()))

# >> 시간 초과

# 리스트 넣고 빼는 거 없이하면?

# def solution(N, M):
#     strings = []

#     vowels = 'aeiou'
#     cons = 'bcdfghjklmnpqrstvwxyz'
    
#     weight = dict()
#     for i in range(len(cons)):
#         weight[cons[i]] = i
    
#     # print(weight)

#     for i in range(N):
#         temp = set()
#         for char in input():
#             temp.add(char)
                
#         num = 0
#         for char in temp:
#             if char in vowels: continue
#             num += 1 << weight.get(char)
        
#         strings.append(num)
    
#     current = (1 << 21) -1
#     for i in range(M):
#         o, x = input().split()
#         if o == '1':
#             current -= 1 << weight.get(x)
#         else:
#             current += 1 << weight.get(x)
        
#         num = 0
#         for string in strings:
#             if current & string == string: num += 1
        
#         print(num)

# if __name__ == '__main__':
#     solution(*map(int, input().split()))

# >> 시간 초과


# 각 알파벳마다 넣어둔 후 해당 알파벳에 있는 것만 비교하면?
    # 최악의 경우엔 a-z가 모두 있는 입력만 들어와서 다시 시간 초과일듯 하지만
    # 일단 해보자

import sys
input = sys.stdin.readline

def solution(N, M):
    vowels = 'aeiou'
    cons = 'bcdfghjklmnpqrstvwxyz'
    
    weight = dict()
    strings = dict()
    for i in range(len(cons)):
        weight[cons[i]] = i
        strings[cons[i]] = []
    

    for i in range(N):
        temp = set()
        for char in input().strip():
            temp.add(char)
                
        num = 0
        for char in temp:
            if char in vowels: continue
            num += 1 << weight.get(char)
        
        for char in temp:
            if char in vowels: continue
            strings.get(char).append(num)
    
    current = (1 << 21) -1
    for i in range(M):
        o, x = input().split()
        if o == '1':
            for string in strings.get(x):
                if current & string == string: N -= 1
            current -= 1 << weight.get(x)
        else:
            current += 1 << weight.get(x)
            for string in strings.get(x):
                if current & string == string: N += 1
        
        print(N)

if __name__ == '__main__':
    solution(*map(int, input().split()))

# ------------------------------------

import sys
input = sys.stdin.readline

def solution(N, M):
    strings = []

    vowels = 'aeiou'
    cons = 'bcdfghjklmnpqrstvwxyz'
    
    weight = dict()
    for i in range(len(cons)):
        weight[cons[i]] = i

    for i in range(N):
        temp = set()
        for char in input().strip():
            temp.add(char)
                
        num = 0
        for char in temp:
            if char in vowels: continue
            num += 1 << weight.get(char)
        
        strings.append(num)
    
    current = (1 << 21) -1
    for i in range(M):
        o, x = input().split()
        if o == '1':
            current -= 1 << weight.get(x)
        else:
            current += 1 << weight.get(x)
        
        num = 0
        for string in strings:
            if current & string == string: num += 1
        
        print(num)

if __name__ == '__main__':
    solution(*map(int, input().split()))

# >> 통과
# 리스트 넣고 빼는 거 없이 해야 통과됨