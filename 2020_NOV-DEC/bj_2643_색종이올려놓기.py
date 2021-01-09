# 되도록 많은 장수의 색종이를 쌓는다.
# 새로 올리는 색종이는 맨 위의 색종이 밖으로 나가면 안 된다.
    # 크지 않아야 한다 -> 같은 건 된다
# 새로 올리는 색종이와 맨 위의 색종이 변들은 모두 평행해야 한다.

# (3, 5) -> 두 변의 '길이'가 3, 5

# 출력: 쌓을 수 있는 최대 색종이 장 수

# 1. 모든 사각형을 x >= y가 되도록 만든다.
# 2. x가 큰 순서대로 정렬한다.
# 3. x가 같은 것끼리 묶어서 배열에 넣는다.
# 4. x 각각의 case당 가능한 모든 y의 경우를 다시 case로 넣는다.
# 5. 전체 경우 중 색종이 장 수가 가장 큰 값을 출력한다.

# 1. 색종이 장 수, 현재 색종이 크기 저장하는 배열 cases
# 2. 색종이 좌표 저장하는 배열 paper


# import sys
# input = sys.stdin.readline

# def solution(N):
#     cases = []

#     temp = []
#     for i in range(N):
#         x, y = map(int, input().split())
#         if x >= y: temp.append((x, y))
#         else: temp.append((y, x))
#     temp.sort(reverse=True)
    
#     cx = float('inf')
#     idx = -1
#     paper = []
#     for x, y in temp:
#         if cx != x:
#             cx = x
#             idx += 1
#             paper.append([(x, y)])
#         else:
#             paper[idx].append((x, y))
    
#     for i in range(len(paper)):
#         paper[i].sort(key=lambda x:x[1], reverse=True)

#     for i in range(len(paper)):
#         temp_cases = [[0, 0]]
#         for j in range(len(paper[i])):
#             if len(temp_cases) == 1:
#                 temp_cases.append([1, paper[i][j][1]])
#                 continue
#             x, y = paper[i][j]
#             for num, cy in temp_cases:
#                 if y < cy: temp_cases.append([num + 1, y])
        
#         if not cases: cases = temp_cases
#         else:
#             next_cases = []
#             for num, cy in cases:
#                 for num2, y in temp_cases:
#                     if y <= cy: next_cases.append([num + num2, y])
#             cases = next_cases
    
#     print(max(cases)[0])

# if __name__ == '__main__':
#     solution(int(input()))

# 반례
# 3
# 100 1
# 2 2
# 2 2



# import sys
# input = sys.stdin.readline

# def solution(N):
#     cases = []

#     temp = []
#     for i in range(N):
#         x, y = map(int, input().split())
#         if x >= y: temp.append((x, y))
#         else: temp.append((y, x))
#     temp.sort(reverse=True)
    
#     cx = float('inf')
#     idx = -1
#     paper = []
#     for x, y in temp:
#         if cx != x:
#             cx = x
#             idx += 1
#             paper.append([(x, y)])
#         else:
#             paper[idx].append((x, y))
    
#     for i in range(len(paper)):
#         paper[i].sort(key=lambda x:x[1], reverse=True)

#     for i in range(len(paper)):
#         temp_cases = [[0, 0]]
#         for j in range(len(paper[i])):
#             if len(temp_cases) == 1:
#                 temp_cases.append([1, paper[i][j][1]])
#                 continue
#             x, y = paper[i][j]
#             for k in range(len(temp_cases)):
#                 num, cy = temp_cases[k]
#                 temp_cases.append([num + 1, y])
        
#         if not cases: cases = temp_cases
#         else:
#             next_cases = []
#             for num, cy in cases:
#                 for num2, y in temp_cases:
#                     if y <= cy: next_cases.append([num + num2, y])
#             cases = next_cases
#             cases += temp_cases
    
#     print(cases)
#     print(max(cases)[0])

# if __name__ == '__main__':
#     solution(int(input()))



# import sys
# input = sys.stdin.readline

# def solution(N):
#     cases = []

#     temp = []
#     for i in range(N):
#         x, y = map(int, input().split())
#         if x >= y: temp.append((x, y))
#         else: temp.append((y, x))
#     temp.sort(reverse=True)
    
#     cx = float('inf')
#     idx = -1
#     paper = []
#     for x, y in temp:
#         if cx != x:
#             cx = x
#             idx += 1
#             paper.append([(x, y)])
#         else:
#             paper[idx].append((x, y))
    
#     for i in range(len(paper)):
#         paper[i].sort(key=lambda x:x[1], reverse=True)

#     for i in range(len(paper)):
#         for j in range(len(paper[i])):
#             x, y = paper[i][j]
#             if not cases: 
#                 cases.append([1, y])
#                 continue
#             for k in range(len(cases)):
#                 num, cy = cases[k]
#                 if y <= cy: cases.append([num + 1, y])
#                 else: cases.append([1, y])

#     print(max(cases)[0])

# if __name__ == '__main__':
#     solution(int(input()))

# > 메모리 초과

import sys
input = sys.stdin.readline

def solution(N):
    cases_n = []
    cases_y = []

    temp = []
    for i in range(N):
        x, y = map(int, input().split())
        if x >= y: temp.append((x, y))
        else: temp.append((y, x))
    temp.sort(reverse=True)
    
    cx = float('inf')
    idx = -1
    paper = []
    for x, y in temp:
        if cx != x:
            cx = x
            idx += 1
            paper.append([(x, y)])
        else:
            paper[idx].append((x, y))
    
    for i in range(len(paper)):
        paper[i].sort(key=lambda x:x[1], reverse=True)

    for i in range(len(paper)):
        for j in range(len(paper[i])):
            x, y = paper[i][j]
            if not cases_n:
                cases_n.append(1)
                cases_y.append(y)
                continue
            for k in range(len(cases_n)):
                num = cases_n[k]
                cy = cases_y[k]
                if y <= cy: 
                    cases_n.append(num + 1)
                    cases_y.append(y)
                else:
                    cases_n.append(1)
                    cases_y.append(y)
    
    print(max(cases_n))

if __name__ == '__main__':
    solution(int(input()))