from copy import copy
n,m,t = map(int,input().split())
ball = []
ballmap = [[0 for _ in range(n)]for _ in range(n)]
newmap = [[0 for _ in range(n)]for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(m):
    r,c,d,w = map(str,input().split())
    r,c,w = int(r)-1,int(c)-1,int(w)
    ball.append([r,c,d,w,i+1])
    ballmap[r][c] = [w,d,i+1]



while t:
    for x in range(n):
        for y in range(n):
            if ballmap[x][y]!=0:   # ballmap[x][y]에 공이 있다면
                if ballmap[x][y][1] == 'U':   #근데 그 공의 방향이 위라면
                    if 0<=x+dx[0]:  # 격자 안에 있고-> 방향 바꿀 필요 없음
                        if newmap[x+dx[0]][y+dy[0]] == 0:  #내가 갈 곳에 공이 없다면
                            newmap[x+dx[0]][y+dy[0]] = ballmap[x][y]  # 공 이동
                            
                        else: # 내가 갈 곳에 공이 있다면
                            newmap[x+dx[0]][y+dy[0]][0] += ballmap[x][y][0]  #무게는 더해주고

                            if ballmap[x][y][2]>newmap[x+dx[0]][y+dy[0]][2]:  # 방향은 공 번호 더 큰 쪽으로
                                newmap[x+dx[0]][y+dy[0]][1] = ballmap[x][y][1]
                                newmap[x+dx[0]][y+dy[0]][2] = ballmap[x][y][2]
                        newmap[x][y]=0
            
                    else:  #격자 안에 없음 -> 방향 바꾸면 됨
                        newmap[x][y][1] = 'D'
                                
                elif ballmap[x][y][1] == 'D':
                    if x+dx[1]<n:
                        if newmap[x+dx[1]][y+dy[1]] == 0:
                            newmap[x+dx[1]][y+dy[1]] = ballmap[x][y]
                        else:
                            newmap[x+dx[1]][y+dy[1]][0] += ballmap[x][y][0]

                            if ballmap[x][y][2]>newmap[x+dx[1]][y+dy[1]][2]:
                                newmap[x+dx[1]][y+dy[1]][1] = ballmap[x][y][1]
                                newmap[x+dx[1]][y+dy[1]][2] = ballmap[x][y][2]
                        newmap[x][y]=0

                    else:
                        newmap[x][y][1] = 'U'

                    
                elif ballmap[x][y][1] == 'L':
                    if 0<=y+dy[2]:
                        if newmap[x+dx[2]][y+dy[2]] == 0:
                            newmap[x+dx[2]][y+dy[2]] = ballmap[x][y]
                        else:
                            newmap[x+dx[2]][y+dy[2]][0] += ballmap[x][y][0]

                            if ballmap[x][y][2]>newmap[x+dx[2]][y+dy[2]][2]:
                                newmap[x+dx[2]][y+dy[2]][1] = ballmap[x][y][1]
                                newmap[x+dx[2]][y+dy[2]][2] = ballmap[x][y][2]
                        newmap[x][y]=0

                    else:
                        newmap[x][y][1] = 'R'
                        
                elif ballmap[x][y][1] == 'R':
                    if y+dy[0]<n:
                        if newmap[x+dx[3]][y+dy[3]] == 0:
                            newmap[x+dx[3]][y+dy[3]] = ballmap[x][y]
                        else:
                            newmap[x+dx[3]][y+dy[3]][0] += ballmap[x][y][0]

                            if ballmap[x][y][2]>newmap[x+dx[3]][y+dy[3]][2]:
                                newmap[x+dx[3]][y+dy[3]][1] = ballmap[x][y][1]
                                newmap[x+dx[3]][y+dy[3]][2] = ballmap[x][y][2]
                        newmap[x][y]=0

                    else:
                        newmap[x][y][1] = 'L'
                
    ballmap = copy(newmap)
    

    t-=1
#구슬의 수와 가장 무거운 구슬의 무게
count = 0
weight = 0
for i in range(n):
    for j in range(n):
        if ballmap[i][j]:
            count += 1
            weight = max(weight, ballmap[i][j][0])
print(count, weight)

