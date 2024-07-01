#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 19237                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/19237                         #+#        #+#      #+#     #
#     Solved: 2024-04-16 12:21:57 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

D = {0: (-1,0), 1: (1,0), 2: (0,-1), 3: (0,1)}
DR = {(-1,0): 0, (1,0) : 1, (0,-1) :2, (0,1) :3} #reverse 
N,M,K = map(int,input().split())
 
# array
A = [list(map(int,input().split())) for _ in range(N)]
SMELL = [[(0,0) for _ in range(N)] for _ in range(N)]
 
SHARKS = {i : {"dir" : 0, "pos" : 0, "prev_pos" : 0} for i in range(1,M+1)}
PREFERENCE = {i : [0] * 4  for i in range(1,M+1)}
 
for i in range(N):
    for j in range(N):
        if A[i][j]:
            shark = A[i][j]
            SHARKS[shark]['pos'] = (i,j)
            SMELL[i][j] = (shark, K)
 
for i, init_dir in enumerate(map(int,input().split()),1):
    SHARKS[i]['dir'] = init_dir-1
 
for s in range(1,M+1):
    for i in range(4):
        PREFERENCE[s][i] = [d-1 for d in list(map(int,input().split()))]
 
t = 0 
while t < 1001 and len(SHARKS.keys()) > 1:
    tmp = [[0] *N for _ in range(N)]
    sharks = sorted(list(SHARKS.keys()))
    for shark in sharks:
        # move sharks 
        now_dir, now_pos = SHARKS[shark]['dir'], SHARKS[shark]['pos']
        x,y = now_pos
        back = None 
        for next_dir in PREFERENCE[shark][now_dir]:
            dx, dy = D[next_dir]
            nx, ny = x+dx, y+dy 
            if 0<=nx<N and 0<=ny<N:
                if SMELL[nx][ny] == (0,0):
                    break 
                if back is None and SMELL[nx][ny][0] == shark:
                    back = nx,ny
        else: # 
            nx,ny = back  
            next_dir = DR[(nx-x, ny-y)]
 
        if not tmp[nx][ny]:
            tmp[nx][ny] = shark 
            SHARKS[shark]['dir'] = next_dir
            SHARKS[shark]['pos'] = (nx, ny)
        elif tmp[nx][ny]:
            del SHARKS[shark]
 
    for i in range(N):
        for j in range(N):
            if SMELL[i][j]:
                s, l = SMELL[i][j]
                SMELL[i][j] = (s, l-1) if l > 1 else (0, 0)
            if tmp[i][j]:
                SMELL[i][j] = (tmp[i][j], K)
    A = tmp
    t += 1
    
print(-1 if t == 1001 else t)