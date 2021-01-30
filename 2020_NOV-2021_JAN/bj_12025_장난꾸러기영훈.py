# 1 -> 6, 6 -> 1, 2 -> 7, 7 -> 2
    # 몇 개를 바꾸었다.
# 단서
    # 1, 6 -> 1 / 2, 7 -> 2로 한 숫자와
    # 1, 6 -> 6 / 2, 7 -> 7로 한 숫자 사이의 가능한 경우 중
    # 사전순으로 나열했을 때 k번째가 비밀번호.

# 출력: 원래 비밀번호
    # k번째 비번 없으면 -1 출력

# 체크할 조건
# 첫 숫자 0 가능
# 비번 길이 60자까지
# k <= 2 ** 63 - 1

# 사전순이므로 1 -> 6, 2 -> 7, 낮은 자리 숫자부터.
# 비번 길이가 60자까지, k는 63자리까지 가능
    # k > 2 ** 60 - 1 이면 -1 출력
# 1111122222222와 같이 초기화한 후
# 2진법으로 1이 있는 자리에만 6 또는 7로 바꿔주기.
    # 1,2,6,7이 있는 인덱스만 따로 저장
    # 1,2,6,7만 따져서 자리수 계산.

def solution(lst, k):
    indices = []
    for i in range(len(lst)):
        if lst[i] in ('1', '2', '6', '7'):
            indices.append(i)
            if lst[i] == '6': lst[i] = '1'
            elif lst[i] == '7': lst[i] = '2'
    compare = bin(k-1)[2:]
    if len(indices) < len(compare): 
        print(-1)
        return
    else:
        for j in range(-1, -len(compare) - 1, -1):
            if compare[j] == '1':
                lst[indices[j]] = '6' if lst[indices[j]] == '1' else '7'
    print(''.join(lst))

if __name__ == '__main__':
    solution(list(input()), int(input()))