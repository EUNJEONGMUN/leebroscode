n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
#delnum = []
for _ in range(2):
    x,y = map(int,input().split())
    arr = arr[:x-1]+arr[y:]

print(len(arr))
for i in arr:
    print(i)

