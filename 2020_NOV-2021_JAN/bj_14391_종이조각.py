# 출력: 얻을 수 있는 점수의 최댓값

# 체크할 조건
# 직사각형 각 조각은 세로나 가로 크기가 1이다
# 가로 조각은 왼쪽부터 오른쪽, 세로는 위에서 아래
# 1 <= N, M <= 4

# 제일 큰 수의 가능성부터 본다 (0으로 시작하지 않는 경우)
# 가로 세로 가장 큰 수가 나오는 경우부터 모두 추린 후
# 남는 부분을 따로 떼어 다시 가장 큰 수를 찾아보자.
    # 0이라서 넘어갔던 부분은 한칸 당겨서 떼어준다.

# def BT(field, val):
#     h = v = 0
#     hidx, vidx = [], []
#     if (not field) or (not field[0]): return val
#     N, M = len(field), len(field[0])
#     for i in range(N):
#         if field[i][0] != '0':
#             temp = field[i][0]
#             hidx.append(i)
#             for j in range(1, M):
#                 temp += field[i][j]
#             h += int(temp)
#     for i in range(M):
#         if field[0][i] != '0':
#             temp = field[0][i]
#             vidx.append(i)
#             for j in range(1, N):
#                 temp += field[j][i]
#             v += int(temp)
    
#     if (not hidx) and (not vidx): return val
    
#     if h >= v:
#         new = [[0] * (M-1) for i in range(N - len(hidx))]
#         idx = 0
#         for i in range(N):
#             if i in hidx: continue
#             for j in range(1, M):
#                 new[idx][j-1] = field[i][j]
#             idx += 1
#         return BT(new, val + h)
#     else:
#         new = [[0] * (M - len(vidx)) for i in range(N-1)]
#         idx = 0
#         for i in range(M):
#             if i in vidx: continue
#             for j in range(1, N):
#                 new[j-1][idx] = field[j][i]
#             idx += 1
#         return BT(new, val + v)

# def solution(N, M):
#     field = [list(input()) for i in range(N)]
#     print(BT(field, 0))

# if __name__ == '__main__':
#     solution(*map(int, input().split()))

# 1 0 0 0
# 0 0 0 1
# 0 1 0 1
# 1 0 0 0

# 4 x 4이므로 완전 탐색 가능
# 가로 탐색이면 0, 세로 탐색이면 1으로 하여 
# 모든 경우에 대해 구한 후 값을 더해서 비교한다.

from itertools import combinations as combi

def calculate(field, vh, N, M, direc):
    visited = [[0] * M for i in range(N)]
    val = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                visited[i][j] = 1
                d = vh[M * i + j]
                dx, dy = direc[d]
                temp = field[i][j]
                nx, ny = j + dx, i + dy
                while ny < N and nx < M and not visited[ny][nx] and vh[M * ny + nx] == d:
                    visited[ny][nx] = 1
                    temp += field[ny][nx]
                    ny += dy
                    nx += dx
                val += int(temp)
    return val                

def solution(N, M):
    field = [list(input()) for i in range(N)]
    vh = [0] * (N*M)
    direc = [[1, 0], [0, 1]]
    result = -float('inf')
    for i in range(N*M+1):
        for indices in combi(range(N*M), i):
            for idx in indices:
                vh[idx] = 1
            result = max(result, calculate(field, vh, N, M, direc))
            for idx in indices:
                vh[idx] = 0
    print(result)

if __name__ == '__main__':
    solution(*map(int, input().split()))



# ????
N,M=map(int,input().split())
L=[]
for i in range(N):
    L+=list(input())
DP=[-1]*(1<<(N*M))
def f(x):
    if x==0: return 0
    if DP[x]!=-1: return DP[x]
    ans=0
    for i in range(N*M-1,-1,-1):
        if x&(1<<i):
            y=x
            d=[]
            for j in range(i,i-(i%M)-1,-1):
                if (x&(1<<j))==0: break
                y^=(1<<j)
                d.append(L[N*M-1-j])
                r=f(y)+int(''.join(d))
                if r>ans: ans=r
            y=x
            d=[]
            for j in range(i,-1,-M):
                if x&(1<<j)==0: break
                y^=(1<<j)
                d.append(L[N*M-1-j])
                r=f(y)+int(''.join(d))
                if r>ans: ans=r

            break
    DP[x]=ans
    return ans
print(f((1<<(N*M))-1))