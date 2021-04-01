# B//2 번 제곱한 결과를 제곱한다.
    # B%2라면 A를 한번 더 곱한다.

# aij bij -> a11*b11 + a12 * b21 + a13 * b31
    # a11 * b12 + a12 * b22 * a13 * b32

def multiply(mat1, mat2):
    n = len(mat1)
    mat = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            temp = 0
            for k in range(n):
                temp += mat1[i][k] * mat2[k][j]
            mat[i][j] = temp % 1000
    return mat

def pow(matrix, n, unit):
    if n == 1: return multiply(matrix, unit)
    if n & 1: return multiply(pow(multiply(matrix, matrix), n // 2, unit), matrix)
    else: return pow(multiply(matrix, matrix), n // 2, unit)

def solution(N, B):
    matrix = [list(map(int, input().split())) for i in range(N)]
    unit = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j: unit[i][j] = 1
    result = pow(matrix, B, unit)
    for _ in range(N):
        print(*result[_])

if __name__ == '__main__':
    solution(*map(int, input().split()))
