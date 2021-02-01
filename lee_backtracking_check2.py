n = int(input())
num = [0]+list(map(int,input().split()))
numsum = []

#def Print(cnt):
#    numsum.append(cnt)

def move(state, count):
    if state == n:
        #Print(count)
        numsum.append(count)
        return

    for i in range(1,num[state]+1):
        move(state+i, count+1)
        
move(1,0)
if numsum:
    print(min(numsum))
else:
    print(-1)
