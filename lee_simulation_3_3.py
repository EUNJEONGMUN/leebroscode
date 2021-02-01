def solution():
    n,m = map(int,input().split())

    bomb = []
    for _ in range(n):
        bomb.append(int(input()))

    for i in range(len(bomb)):
