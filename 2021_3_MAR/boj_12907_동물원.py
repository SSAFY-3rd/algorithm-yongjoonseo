# 1번부터 N번 번호매겨진 동물
    # 토끼 or 고양이
    # 키는 모두 다르다
# 같은 동물 중 자신보다 키가 큰 동물의 수를 물을 때
# 각 대답을 어떤 동물이 했는지 알아내려 함

# 출력: 가능한 조합의 수

# 체크할 조건
# 1 <= N <= 40 (동물의 수)
# 0 <= 대답 <= 40
    # 각 대답은 동물의 수보다 많을 수도 있고 0일 수도 있다.

# 대답 숫자가 적을수록 키가 크다.
# 0은 2개까지만 가능하다.
    # 모든 수는 2개 초과해서 나올 수 없다. (토끼, 고양이 두 종류)
# 키가 모두 다르므로 0, 1, 2, 3... 순서로 와야한다.
# 0, 0, 1, 1 ... 짝 맞는 만큼 2의 n제곱 해서 개수를 구한다.
    # 짝이 딱 떨어지는 경우 n제곱, 이외엔 n+1제곱
        # (0, 0, 1, 1, 2, 2의 경우의 수 == 0, 0, 1, 1, 2)
    # 짝 맞은 후에는 가능한 경우여야 한다.
        # 0, 0, 1, 1, 2, 3, 4, 5 (O)
        # 0, 0, 1, 1, 2, 3, 4, 6 (X)

def impossible():
    print(0)
    exit()

def solution(N, answers):
    answers.sort()
    check = [0] * 41
    for answer in answers:
        check[answer] += 1
        if check[answer] > 2: impossible()

    power = 0
    for i in range(len(check)):
        if check[i] == 2:
            power += 1
        else:
            break
    if check[i]:
        while i < len(check):
            if check[i] == 1: i += 1
            elif check[i] == 2: impossible()
            else: break
    else:
        i += 1
        for j in range(i, len(check)):
            if check[j]: impossible()
        print(2**power)
        return
    
    for j in range(i, len(check)):
        if check[j]: impossible()
    print(2 ** (power + 1))

if __name__ == '__main__':
    solution(int(input()), list(map(int, input().split())))