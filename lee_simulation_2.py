n, t = map(int,input().split())
arr = []
for _ in range(2):
    user = input().split()
    arr.extend("".join(user))
    

count = 0

for i in range(t):
    temp = list(arr.pop())
    arr = temp+arr

for i in range(len(arr)):
    print(arr[i], end = ' ')
    if i%n == n-1:
        print()
