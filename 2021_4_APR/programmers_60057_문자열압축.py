# 1개 이상의 단위로 잘라서 압축

# 출력: 압축한 문자열 중 가장 짧은 것의 길이

# 체크할 조건
# 문자열은 제일 앞에서 정해진 길이 만큼 잘라야 함.
# 앞에서부터 잘라서 순서대로 리스트에 넣는다 [문자열, 개수]
# 모두 리스트에 넣은 후 압축된 문자열의 길이를 구하여 갱신한다. 

def solution(s):
    answer = len(s)
    for i in range(1, len(s)):
        cnt = 0
        temp = []
        temp.append([s[:i], 1])
        j = i
        while j < len(s):
            string = s[j:j+i]
            if temp[-1][0] == string:
                temp[-1][1] += 1
            else:
                temp.append([string, 1])
            j += i
        for word, num in temp:
            cnt += len(word)
            if num > 1:
                cnt += len(str(num))
        answer = min(answer, cnt)
    return answer