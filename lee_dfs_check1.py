n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
visited = [['F' for _ in range(n)] for _ in range(n)]
countmax = 0
countfour = 0
count = 0
countlist = []

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

    

def DFS(x,y):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    global count

    for i in range(4):
        new_x, new_y = x+dx[i], y+dy[i]

        if(CanGo(new_x,new_y)) and arr[x][y] == arr[new_x][new_y]:
            count += 1
            visited[new_x][new_y] = 'T'
            DFS(new_x,new_y)



for i in range(n):
    for j in range(n):
        if visited[i][j] == 'F':
            visited[i][j] = 'T'
            count = 1
            DFS(i,j)
            countlist.append(count)
            count = 1


for i in range(len(countlist)):
    if countlist[i] > 3:
        countfour += 1
    countmax = max(countlist)
print(countfour, countmax)



        
