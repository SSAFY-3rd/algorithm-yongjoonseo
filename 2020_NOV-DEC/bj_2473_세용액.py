# 산성 용액, 알칼리 용액
# 용액의 특성을 나타내는 정수
    # 산성 - 양 / 염기성 - 음
# 용액의 특성값 - 각 용액의 특성값의 합
# 특성값이 0에 가까운 용액을 만드려고 함.

# 출력: 특성값이 0에 가장 가까운 용액의 특성값을 오름차순으로 출력

# 체크할 조건
# 특성값을 '오름차순'으로 출력
# 산성 용액 or 염기성 용액으로만 이루어져있을 수 있음

# N <= 5000이라 백트래킹은 힘들듯.
# 하나의 값을 정하고 투포인터 알고리즘으로 
# 세 용액의 특성값의 합이 최소인 점을 구해보자.
# 양 끝을 각각 start, end라고 하면
    # start++ == 특성값 합이 커진다
    # end-- == 특성값 합이 작아진다
# 합이 0보다 작다 -> start++
# 합이 0보다 크다 -> end--

def solution(N):
    sol = sorted(list(map(int, input().split())))
    val = float('inf')
    result = []
    for i in range(len(sol)-2):
        s, e = i+1, len(sol)-1
        while s != e:
            sumval = sol[i] + sol[s] + sol[e]
            absval = abs(sumval)
            if absval < val:
                val = absval
                result = [sol[i], sol[s], sol[e]]
            if sumval < 0: s += 1
            elif sumval > 0: e -= 1
            else:
                print(sol[i], sol[s], sol[e])
                return
    print(*result)

if __name__ == '__main__':
    solution(int(input()))