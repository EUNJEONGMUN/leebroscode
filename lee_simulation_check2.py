import sys

def solution():
    arr = list(input())
    num = sys.maxsize

    if len(arr)==1:
        return 2


    for _ in range(len(arr)-1):
        numcount = strcount(arr)
        num = min(numcount,num)
        
        arr = arr[-1:] + arr[:-1]
    return num

def strcount(my_str):
    answer = ""
    count = 1
    for i in range(len(my_str)-1):
        if my_str[i] == my_str[i+1]:
            count += 1
        else:
            answer+= my_str[i] + str(count)
            count = 1
    answer += my_str[-1] + str(count)
    return len(answer)

print(solution())

