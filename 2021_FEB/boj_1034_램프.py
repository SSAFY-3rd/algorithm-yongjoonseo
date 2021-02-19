# 출력: 켜진 행의 최댓값

# 체크할 조건
# 1 <= N, M <= 50
# 0 <= K <= 1000

# 켜지는 행이 있다면 적어도 하나의 행은 켜진다.
    # 그때의 열의 on/off 배열은 고유하다.
    # 같이 켜지는 행은 이후에 체크할 필요 없다.
    # 켜지는 행을 만들고 K가 짝수 만큼 남으면 카운트 가능.
# 켜진 행 개수의 최댓값을 갱신하며 모든 행을 순회.

import sys
input = sys.stdin.readline

def solution(N, M):
    lst = [input().strip() for i in range(N)]
    K = int(input())
    result = 0
    lamps = []
    for column in zip(*lst):
        lamps.append('0b1' + ''.join(column))
    visited_row = [0] * N
    std = (1 << N) - 1
    for i in range(N):
        if visited_row[i]: continue
        cols = lamps[:]
        left = K
        is_possible = True
        for j in range(M):
            if cols[j][i+3] == '0':
                if not left: 
                    is_possible = False
                    break
                left -= 1
                cols[j] = bin(int(cols[j], base=2) ^ std)
        if left&1: is_possible = False
        if not is_possible: continue
        cnt = 1
        visited_row[i] = 1
        for k in range(i+1, N):
            for j in range(M):
                if cols[j][k+3] == '0':
                    break
            else:
                cnt += 1
                visited_row[k] = 1
        result = max(result, cnt)
    print(result)

if __name__ == '__main__':
    solution(*map(int, input().split()))