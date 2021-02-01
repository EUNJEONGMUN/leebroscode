n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
newarr = [[0 for i in range(n)] for i in range(n)]
maxnum = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def InRange(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False

def Count(A):
    num = 0
    global maxnum
    for i in range(n):
        for j in range(n):
            if A[i][j] == 0:
                continue
            else:
                for g in range(4):
                    if InRange(i+dx[g],j+dy[g]) and A[i+dx[g]][j+dy[g]] == A[i][j]:
                        num+=1
    maxnum = max(num,maxnum)



def bomb(x,y):
    for i in range(4):
        a,b = x,y
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
    Count(newarr)


for x in range(n):
    for y in range(n):
        point = arr[x][y]
        arr[x][y] = 0
        bomb(x,y)


print(maxnum)
    
