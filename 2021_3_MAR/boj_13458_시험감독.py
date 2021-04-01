# N개 시험장, i번 시험장 응시자수 Ai
# 총감독관 부감독관 각각 B명, C명 감시 가능
# 총감독관은 1명, 부감독관은 여러명 가능
# 응시생 모두 감시할 때 필요한 최소 감독관 수

# 출력: 필요한 감독관의 최소 수

# 체크할 조건
# 1 <= N <= 1000000 (시험장 개수)
# 1 <= Ai <= 1000000 (응시자 수)
# 1 <= B,C <= 1000000
# 예제를 보니 부감독관이 없어도 되는듯.

# 시험장마다 총감독관 하나 배치하고 
# 남은 응시생 수를 커버할 수 있는 부감독관 수를 찾는다.

def solution(N, A, B, C):
    cnt = 0
    for num in A:
        num -= B
        cnt += 1
        if num > 0:
            if num % C: cnt += 1
            cnt += num // C
    print(cnt)

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())
    solution(N, A, B, C)