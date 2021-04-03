# 한자리 숫자가 적힌 종이 조각
    # '013' == 0, 1, 3

# 출력: 종이 조각으로 만들 수 있는 소수 개수

# 체크할 조건
#     1 <= len(numbers) <= 7

# 소수 판별 함수를 만든 후 완전탐색

from itertools import permutations

def is_prime(number):
    if number <= 1: return False
    i = 2
    while i * i <= number:
        if not number % i:
            return False
        i += 1
    return True
    
def solution(numbers):
    nums = set()
    for i in range(1, len(numbers)+1):
        for item in permutations(numbers, i):
            num = int(''.join(item))
            nums.add(num)
    
    answer = 0
    for num in nums:
        if is_prime(num):
            answer += 1
        
    return answer