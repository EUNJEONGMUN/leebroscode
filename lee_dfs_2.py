n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
visited = [[0 for _ in range(m)] for _ in range(n)]

def DFS(x,y):
    dx = [1,0]
    dy = [0,1]

    for i in range(2):
        new_x, new_y = x+dx[i], y+dy[i]

        if new_x<n and new_y<n and visited[new_x][new_y] == 0 and arr[new_x][new_y]==1:
            visited[new_x][new_y] == 1
            DFS(new_x, new_y)
    


visited[0][0] = 1
DFS(0,0)
if visited[n-1][n-1] == 1:
    print(1)
else:
    print(0)
