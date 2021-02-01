n,m = map(int,input().split())
edge = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    edge[a][b] = 1
    edge[b][a] = 1

count = 0

def DFS(start):
    global count
    for i in range(1,n+1):
        if visited[i]==0 and edge[start][i]:
            visited[i]=1
            count += 1

            DFS(i)
visited[1]=1
DFS(1)
print(count)
    
