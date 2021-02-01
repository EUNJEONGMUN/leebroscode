from collections import deque
n,k = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
visited = [['F' for _ in range(n)] for _ in range(n)]
state = [[-2 for _ in range(n)] for _ in range(n)]
q = deque()
def InRange(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False
    
def CanGo(x,y):
    if not InRange(x,y):
        return False
    if (visited[x][y] == 'T') or (arr[x][y]==0):
        return False
    return True


def Push(x,y,t):
    visited[x][y] = 'T'
    state[x][y] = t
    q.append([x,y])
    
def BFS():

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    while q:
        x,y = q.popleft()
        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]
            if (CanGo(new_x,new_y)):
                Push(new_x,new_y,state[x][y]+1)


for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            visited[i][j] = 'T'
            Push(i,j,0)

BFS()

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            state[i][j] = -1
        print(state[i][j], end = ' ')
    print()
