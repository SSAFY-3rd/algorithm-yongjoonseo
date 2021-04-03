# 체크할 조건
# K는 '한 자리' 정수
# Q는 '0자리' 이상의 문자열

# 출력: 압축되지 않은 문자열의 길이

# 1(9) == 9
# 71(9) == 79 => 7979
# 33(567979)
# 3 567979 567979 567979

# 스택을 사용해서 괄호 안에 있는 문자열을 더하여 반환한다.
# 함수 (문자열, 탐색할위치, 괄호 바로앞 숫자) -> 문자열 길이, 탐색한 길이

def cal(string, s, num):
    leng = 0
    while s < len(string):
        if string[s] == '(':
            leng -= 1
            calculated, s = cal(string, s+1, int(string[s-1]))
            leng += calculated
        elif string[s] == ')':
            return leng * num, s
        else:
            leng += 1
        s += 1
    return leng * num, s

def solution(string):
    print(cal(string, 0, 1)[0])

if __name__ == '__main__':
    solution(input())