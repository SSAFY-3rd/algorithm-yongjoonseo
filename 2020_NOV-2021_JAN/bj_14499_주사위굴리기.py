# 이동한 칸의 수 == 0: 주사위 바닥면 수 -> 칸
# else: 칸의 수 -> 주사위 바닥면
# 가장 처음 주사위: 모든 면이 0
# 바깥으로 이동하려는 경우 해당 명령을 무시

# 출력: 주사위가 이동할 때마다의 상단 숫자의 값

# 1. 맵 밖으로 나가는지 체크 (return boolean)
# 2. 이동하는 명령 (구른다)
# 3. 칸 - 주사위 숫자 갱신 (이동할 때마다)

N, M, y, x, K = map(int, input().split())
field = []

class Dice:
    def __init__(self, y, x, top=0, bottom=0, front=0, back=0, left=0, right=0):
        self.top = top
        self.bottom = bottom
        self.front = front
        self.back = back
        self.left = left
        self.right = right
        self.y = y
        self.x = x

    def roll(self, n, y, x):
        if n == 1: # 동쪽
            temp = self.left
            self.left = self.bottom
            self.bottom = self.right
            self.right = self.top
            self.top = temp
        elif n == 2: # 서쪽
            temp = self.left
            self.left = self.top
            self.top = self.right
            self.right = self.bottom
            self.bottom = temp
        elif n == 3: # 북쪽
            temp = self.front
            self.front = self.bottom
            self.bottom = self.back
            self.back = self.top
            self.top = temp
        else: # 남쪽
            temp = self.front
            self.front = self.top
            self.top = self.back
            self.back = self.bottom
            self.bottom = temp
        self.y = y
        self.x = x
    
    def update(self, n, y, x):
        self.roll(n, y, x)
        if field[y][x] == 0:
            field[y][x] = self.bottom
        else:
            self.bottom = field[y][x]
            field[y][x] = 0
        

def in_map(y, x):
    global N, M
    if 0 <= y < N and 0 <= x < M: return True
    else: return False

def move(n, dice):
    if n == 1: # 동쪽
        if in_map(dice.y, dice.x + 1):
            dice.update(1, dice.y, dice.x+1)
            return True
    elif n == 2: # 서쪽
        if in_map(dice.y, dice.x - 1):
            dice.update(2, dice.y, dice.x-1)
            return True
    elif n == 3: # 북쪽
        if in_map(dice.y - 1, dice.x):
            dice.update(3, dice.y-1, dice.x)
            return True
    else: # 남쪽
        if in_map(dice.y + 1, dice.x):
            dice.update(4, dice.y+1, dice.x)
            return True
    return False   

for _ in range(N):
    field.append(list(map(int, input().split())))

dice = Dice(y, x)

orders = list(map(int, input().split()))

for order in orders:
    if move(order, dice):
        print(dice.top)
    