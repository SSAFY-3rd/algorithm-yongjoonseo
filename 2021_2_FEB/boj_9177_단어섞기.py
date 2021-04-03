# 출력: Data set n: yes / no

# 첫 번째 단어 먼저 필터링 or 두 번째 단어 먼저 필터링
    # 한번이라도 되면 yes 아니면 no

# import sys
# input = sys.stdin.readline

# def solution(n):
#     w1, w2, w3 = input().split()
#     words = [w1, w2]
#     for i in range(2):
#         w1, w2 = words[i], words[(i+1)&1]
#         visited = [0] * (len(w3))
#         a = b = 0
#         for j in range(len(w3)):
#             if a == len(w1): break
#             if not visited[j] and w1[a] == w3[j]:
#                 visited[j] = 1
#                 a += 1
#         for j in range(len(w3)):
#             if b == len(w2): break
#             if not visited[j] and w2[b] == w3[j]:
#                 visited[j] = 1
#                 b += 1
#         if a == len(w1) and b == len(w2):
#             print('Data set {0}: yes'.format(n))
#             return
#     print('Data set {0}: no'.format(n))

# if __name__ == '__main__':
#     for i in range(1, int(input())+1):
#         solution(i)

# 틀림 (반례: tcat tree tcatrtee)

# from collections import deque
# import sys
# input = sys.stdin.readline

# def solution(n):
#     w1, w2, w3 = input().split()
#     i = 0
#     q = deque([(0, 0)])
#     while q:
#         for _ in range(len(q)):
#             a, b = q.popleft()
#             if a < len(w1) and w1[a] == w3[i]:
#                 q.append((a+1, b))
#             if b < len(w2) and w2[b] == w3[i]:
#                 q.append((a, b+1))
#         i += 1
#     tf = 'yes' if i == len(w3)+1 else 'no'
#     print('Data set {0}: {1}'.format(n, tf))

# if __name__ == '__main__':
#     for i in range(1, int(input())+1):
#         solution(i)

# >> 메모리 초과


from collections import deque
import sys
input = sys.stdin.readline

def solution(n):
    w1, w2, w3 = input().split()
    i = 0
    q = deque([(0, 0)])
    visited = [[0] * (len(w2)+1) for i in range(len(w1)+1)]
    while q:
        for _ in range(len(q)):
            a, b = q.popleft()
            if a < len(w1) and not visited[a+1][b] and w1[a] == w3[i]:
                visited[a+1][b] = 1
                q.append((a+1, b))
            if b < len(w2) and not visited[a][b+1] and w2[b] == w3[i]:
                visited[a][b+1] = 1
                q.append((a, b+1))
        i += 1
    tf = 'yes' if i == len(w3)+1 else 'no'
    print('Data set {0}: {1}'.format(n, tf))

if __name__ == '__main__':
    for i in range(1, int(input())+1):
        solution(i)
