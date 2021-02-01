from collections import deque
n,k,u,d = map(int,input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
visited = [['F' for _ in range(n)] for _ in range(n)]
q = deque()
town = 0

def InRange(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False
    
def CanGo(x,y):
    if not InRange(x,y):
        return False
    if (visited[x][y] == 'T'):
        return False
    return True


def Push(x,y):
    global town
    town += 1
    visited[x][y] = 'T'
    q.append([x,y])
    
def BFS():

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    count = k
 
    while count:
        x,y = q.popleft()
        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]
            if (CanGo(new_x,new_y)) and (u<=abs(arr[x][y]-arr[new_x][new_y])<=d):
                Push(new_x,new_y)
        count -= 1

if k == 1:
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 'F':
                visited[i][j] = 'T'
                Push(i,j)
                BFS()
elif k == 2:
    for i in range(n*n):
        for j in range(i+1, n*n):
            if visited[i//n][i%n] == 'F' and visited[j//n][j%n] == 'F':
                visited[i//n][i%n] = 'T'
                visited[j//n][j%n] = 'T'
                Push(i//n, i%n)
                Push(j//n, j%n)
                BFS()
else:
    for i in range(n*n):
        for j in range(i+1, n*n):
            for g in range(j+1,n*n):
                if visited[i//n][i%n] == 'F' and visited[j//n][j%n] == 'F' and visited[g//n][g%n] == 'F':
                    visited[i//n][i%n] = 'T'
                    visited[j//n][j%n] = 'T'
                    visited[g//n][g%n] = 'T'
                    Push(i//n, i%n)
                    Push(j//n, j%n)
                    Push(g//n, g%n)
                    BFS()

print(town)
