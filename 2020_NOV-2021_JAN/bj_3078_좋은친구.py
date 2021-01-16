# 좋은 친구 
    # 1. 등수의 차이가 K보다 작거나 같다.
    # 2. 이름의 길이가 같다.

# 출력: 좋은 친구 쌍의 수

# 체크할 조건
# 3 <= N <= 300000 (학생 수), 1 <= K <= N (등수 차이)
# 성적순으로 주어진다
# '쌍'의 개수를 출력한다.
# 글자는 2~20글자

# 슬라이딩 윈도우 알고리즘을 사용한다. (크기 K로 고정)
# 크기 3~21글자인 경우를 모두 탐색한다. (readline이라서)
    # 크기 22의 배열을 만든다. (num)
        # 현재 큐 안에 길이 i의 글자인 것의 개수 저장용
    # 돌면서 큐의 크기가 K가 넘어가면 popleft, 
        # 길이 i의 글자라면 num[i] -= 1
    # 입력받을 때 num[i] > 0이면 num[i] - 1 만큼 더해준다
        # num[i] += 1도 해주기

import sys
input = sys.stdin.readline
from collections import deque

def solution(N, K):
    inp = [len(input()) - 1 for i in range(N)]
    num = [0 for i in range(21)]

    cnt = 0
    for i in range(2, 21):
        q = deque()
        for leng in inp:
            q.append(leng)
            if len(q) > K + 1:
                if q.popleft() == i: num[i] -= 1
            if leng == i:
                if num[i] > 0: cnt += num[i]
                num[i] += 1
    
    print(cnt)    

if __name__ == '__main__':
    solution(*map(int, input().split()))


# 문자 길이를 저장하는 배열 lst
# 각 길이의 문자가 몇 개 있는지 저장하는 딕셔너리 nums
# 문자열 들어올 때마다 K범위 안에서 세어 더해준다.

import sys
input = sys.stdin.readline

def solution(N, K):
    lst = []
    nums = dict()
    cnt = 0
    for i in range(N):
        lst.append(len(input()))
        if not lst[i] in nums: nums[lst[i]] = 0
        if i > K: nums[lst[i-K-1]] -= 1
        cnt += nums[lst[i]]
        nums[lst[i]] += 1
    print(cnt)

if __name__ == '__main__':
    solution(*map(int, input().split()))