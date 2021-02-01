n,m,t = map(int,input().split())
arr = [[0 for _ in range(n+1)] for _ in range(n+1)]
newarr = [[0 for _ in range(n+1)] for _ in range(n+1)]
ball = [[0 for _ in range(n+1)] for _ in range(n+1)]


def InRange(x,y):
    if 1<=x<=n and 1<=y<=n:
        return True
    else:
        return False

def getmax(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    max_num = 0
    max_pos = (0,0)

    for i in range(4):
        next_x, next_y = x+dx[i], y+dy[i]

        if InRange(next_x, next_y) and arr[next_x][next_y]>max_num:
            max_num = arr[next_x][next_y]
            max_pos = (next_x, next_y)
    return max_pos

def move(x,y):
    next_x, next_y = getmax(x,y)
    newarr[next_x][next_y] += 1

def move_all():
    for i in range(1,n+1):
        for j in range(1,n+1):
            newarr[i][j] = 0

    for i in range(1,n+1):
        for j in range(1,n+1):
            if ball[i][j] == 1:
                move(i,j)

    for i in range(1,n+1):
        for j in range(1,n+1):
            ball[i][j] = newarr[i][j]

def Remove():
    for i in range(1,n+1):
        for j in range(1,n+1):
            if ball[i][j] >= 2:
                ball[i][j] = 0

def solution():

    move_all()

    Remove()

for i in range(1,n+1):
    A = list(map(int,input().split()))
    for j, elem in enumerate(A, start = 1):
        arr[i][j] = elem
        
for _ in range(m):
    a,b = tuple(map(int,input().split()))
    ball[a][b] = 1

for _ in range(t):
    solution()

answer = sum([ball[i][j] for i in range(1, n + 1) for j in range(1, n + 1)])

print(answer)
             
             
             
             