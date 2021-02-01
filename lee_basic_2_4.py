n = int(input())
arr = list(map(int, input().split()))


turn = n
while turn:
    my_max = arr[0]

    for i in range(turn):
        if arr[i]>my_max:
            my_max = arr[i]
            num = min(num, i+1)
    print(num, end = " ")
    turn = num
            
