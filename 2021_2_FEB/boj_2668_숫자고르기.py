# 출력: 정수들의 개수 -> 뽑힌 정수들을 작은 수부터

# 체크할 조건
# 1 <= N <= 100

# 순서: 값 형식으로 딕셔너리에 저장.
# dict.get(값)을 해서 본인 순서 or None이 나올 때까지 순환
    # None이면 continue
    # 본인 순서가 나온다면 거쳐간 숫자 모두 dict에서 pop, 저장

import sys
input = sys.stdin.readline

def solution(N):
    check = dict()
    result = []
    for i in range(1, N+1):
        num = int(input())
        if num == i: 
            result.append(num)
            continue
        check[i] = num
        if num in check:
            target = num
            temp = [target]
            while not (target == i or target == None):
                target = check.get(target)
                temp.append(target)
            if target == None: continue
            else:
                for n in temp:
                    result.append(n)
                    check.pop(n)
    result.sort()
    print(len(result))
    for num in result:
        print(num)

if __name__ == '__main__':
    solution(int(input()))