n = int(input())
answer = []
for i in range(n):
    x,y = map(int,input().split())
    answer.append((abs(0-x)+abs(0-y),i+1))

answer.sort(key = lambda x: (x[0],x[1]))
for i in range(len(answer)):
    print(answer[i][1])
