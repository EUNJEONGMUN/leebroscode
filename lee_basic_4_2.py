n = int(input())
start = []
for _ in range(n):
    start.append(list(map(int, input().split())))
    
end = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        end[i][j] = start[n-1-j][i]

for elem in end:
    for i in range(len(elem)):
        print(elem[i], end = ' ')
    print()
    
