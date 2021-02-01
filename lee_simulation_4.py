n, r, c = map(int,input().split())
r, c = r-1, c-1
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
max_value = arr[r][c]
print(max_value, end = ' ')
while True:

    mark = 0
    for i in range(4):
        if 0<=r+dx[i]<n and 0<=c+dy[i]<n and arr[r+dx[i]][c+dy[i]] > max_value:
            r, c = r+dx[i],c+dy[i]
            max_value = arr[r][c]
            print(max_value, end = ' ')
            mark = 1
            break
    if mark == 0:
        break
        
            
        
        
    
