n = int(input())

answer = [[0 for _ in range(n)] for _ in range(n)]

x, y = n//2, n//2
count = 2
new = 1
my = 1
answer[x][y] = 1
while not(x==n-1 and y==0) :
    for _ in range(my):
        y += new
        answer[x][y]=count
        count+=1
    new *= -1
    for _ in range(my):
        x += new
        answer[x][y]=count
        count+=1
    my+=1
for _ in range(my-1):
    y+=1
    answer[x][y] = count
    count+=1


for elem in answer:
    for i in range(len(elem)):
        print(elem[i], end=' ')
    print()
