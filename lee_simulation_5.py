n,m,t = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
point = []
for _ in range(m):
    point.append(list(map(int, input().split())))

count = [[0 for _ in range(n)] for _ in range(n)]
new_count = [[0 for _ in range(n)] for _ in range(n)]

for i in range(t):
    move()
        
def move():
    
