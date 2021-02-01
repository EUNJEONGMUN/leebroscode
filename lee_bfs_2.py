from collections import deque
n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
visited = [['F' for _ in range(m)] for _ in range(n)]
road = [[0 for _ in range(m)] for _ in range(n)]
q = deque()

def InRange(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False
    
def CanGo(x,y):
    if not InRange(x,y):
        return False
    if (visited[x][y] == 'T') or (arr[x][y]==0):
        return False
    return True


def Push(x,y,s):
    visited[x][y] = 'T'
    road[x][y] = s
    q.append([x,y])
    
def BFS():

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    while q:
        x,y = q.popleft()
        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]
            if (CanGo(new_x,new_y)):
                Push(new_x,new_y,road[x][y]+1)



visited[0][0] = 'T'
Push(0,0,0)
BFS()

if visited[n-1][m-1] == 'T':
    print(road[n-1][m-1])
else:
    print(-1)
