#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 23288                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/23288                         #+#        #+#      #+#     #
#     Solved: 2024-05-13 15:04:22 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
 
def fill_scores(x,y):
    if visited[x][y]:
        return
    q = deque([(x,y)])
    B = MAP[x][y]
    C = 1 
    cluster = [(x,y)]
    visited[x][y] = True 
    while q:
        x,y = q.popleft()
 
        for dx, dy in D:
            nx, ny = x+dx, y+dy 
            if 0<=nx<N and 0<=ny<M and MAP[nx][ny] == B and not visited[nx][ny]:
                C += 1 
                visited[nx][ny] = True 
                cluster.append((nx,ny))
                q.append((nx,ny))
    score = B*C
    for x,y in cluster:
        Scores[x][y] = score 
 
def rotate(dx,dy,clockwise):
    if clockwise:
        return dy,-dx 
    else:
        return -dy, dx 
 
DICE = [2,4,1,3,5,6]
BOT = -1 
def go(dx,dy):
    if (dx,dy) == (-1,0):
        DICE[0],DICE[2],DICE[4],DICE[5] = DICE[2],DICE[4],DICE[5],DICE[0]
    elif (dx,dy) == (1,0):
        DICE[0],DICE[2],DICE[4],DICE[5] = DICE[5],DICE[0],DICE[2],DICE[4]
 
    elif (dx,dy) == (0,-1):
        DICE[1],DICE[2],DICE[3],DICE[5] = DICE[2],DICE[3],DICE[5],DICE[1]
    else:
        DICE[1],DICE[2],DICE[3],DICE[5] = DICE[5],DICE[1],DICE[2],DICE[3]
 
 
D = [(-1,0), (0,1), (1,0), (0,-1)]
N,M,K = map(int, input().split())
MAP=[list(map(int,input().split())) for _ in range(N)]
 
Scores = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
 
for i in range(N):
    for j in range(M):
        fill_scores(i,j)
 
x,y,dx,dy = 0,0,0,1
ans = 0
for _ in range(K):
    # 굴리기 ~ 
    nx,ny = x+dx, y+dy 
    if not (0<=nx<N and 0<=ny<M):
        dx,dy = -dx, -dy
        nx,ny = x+dx, y+dy 
 
    go(dx,dy)
    A,B = DICE[-1], MAP[nx][ny]
    if A>B:
        dx,dy = rotate(dx,dy,True)
    elif A<B:
        dx,dy = rotate(dx,dy,False)
    ans += Scores[nx][ny]
    x,y = nx,ny
 
 
 
print(ans)
 