#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 23289                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/23289                         #+#        #+#      #+#     #
#     Solved: 2024-02-26 11:56:45 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
 
R,C,K = map(int,input().split())
A=[list(map(int,input().split())) for _ in range(R)]
WALLS = [[[False] * 4 for _ in range(C)] for _ in range(R)]
TEMPS = [[0] * C for _ in range(R)]
for _ in range(int(input().strip())):
    x,y,t = map(int,input().split())
    x,y = x-1, y-1
    if t == 0: 
        WALLS[x-1][y][2] = True # 위->아래 
        WALLS[x][y][0] = True # 아래 -> 위 
    else:
        WALLS[x][y][1] = True 
        WALLS[x][y+1][3] = True 
DtoD = {1:1,2:3,3:0,4:2} # heater d -> walls d
HEATERS = [ (i,j,DtoD[A[i][j]])  for i in range(R) for j in range(C) if 0 < A[i][j] < 5]
D=[(-1,0),(0,1),(1,0),(0,-1)]
NEXTS = [
    [[0],[3,0],[1,0]], # 위
    [[1],[0,1],[2,1]], # 오른쪽
    [[2],[3,2],[1,2]], # 아래
    [[3],[0,3],[2,3]], # 왼쪽 
]
TARGETS = [(x,y) for x in range(R) for y in range(C) if A[x][y] == 5]
 
def check_wall(x, y, d):
    return WALLS[x][y][d]
    
def heating():
    for x,y,d in HEATERS:
        visited = [[0]*C for _ in range(R)]
        dx,dy=D[d]
        x,y=x+dx,y+dy
        visited[x][y] = 5
        queue = deque([(x,y,5)])
        while queue:
            x,y,heat = queue.popleft()
            if not heat:
                break 
            for path in NEXTS[d]:
                px,py,nx,ny=x,y,x,y
                blocked = False
                for i,d in enumerate(path):
                    dx, dy = D[d]
                    nx,ny=nx+dx, ny+dy
                    if 0<=nx<R and 0<=ny<C and not visited[nx][ny] and not check_wall(px,py,d):
                        px,py=nx,ny
                    else:
                        blocked = True
                if not blocked:
                    queue.append((nx,ny,heat-1))
                    visited[nx][ny] = heat-1
        for i in range(R):
            for j in range(C):
                TEMPS[i][j] += visited[i][j]
def adjust():
    tmp = [[0]*C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            t = TEMPS[x][y]
            if t:
                for d in range(4):
                    dx,dy=D[d] 
                    nx,ny=x+dx,y+dy
                    if 0<=nx<R and 0<=ny<C and t>TEMPS[nx][ny] and not check_wall(x,y,d): 
                        diff= (t - TEMPS[nx][ny])
                        tmp[nx][ny] += diff // 4
                        tmp[x][y] -= diff //4
    for x in range(R):
        for y in range(C):
            v = TEMPS[x][y] + tmp[x][y] - 1 if x in [0,R-1] or y in [0,C-1] else TEMPS[x][y] + tmp[x][y]
            TEMPS[x][y] = max(v, 0)
 
def check():
    return all([TEMPS[x][y] >= K for x,y in TARGETS])
 
done = False 
ans = 0
for t in range(101):
    heating()
    adjust()
    if check():
        done = True
        ans = t+1
        break 
print(ans if ans else 101)