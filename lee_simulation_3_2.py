n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
newarr = [[0 for i in range(n)] for i in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

x,y = map(int,input().split())
point = arr[x-1][y-1]
arr[x-1][y-1] = 0

for i in range(4):
    a,b = x-1,y-1
    for _ in range(1, point):
        if not(0<=a+dx[i]<n and 0<=b+dy[i]<n):
            continue
        else:
            arr[a+dx[i]][b+dy[i]] = 0
            a,b = a+dx[i], b+dy[i]

for i in range(n):
    put = n-1
    for j in range(n-1,-1,-1):
        if arr[j][i] != 0:
            newarr[put][i] = arr[j][i]
            put-=1

for elem in newarr:
    for i in range(len(elem)):
        print(elem[i], end=' ')
    print() 
    
