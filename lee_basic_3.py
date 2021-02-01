my_str, num = list(map(str, input().split()))
call = []
for _ in range(int(num)):
    call.append(int(input()))

for elem in call:
    if elem == 1:
        my_str = my_str[1:]+my_str[0]
        print(my_str)
    elif elem == 2:
        my_str = my_str[-1] + my_str[:-1]
        print(my_str)
    else:
        my_str = my_str[::-1]
        print(my_str)
