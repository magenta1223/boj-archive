#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2573                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2573                          #+#        #+#      #+#     #
#     Solved: 2024-05-16 12:17:28 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
 
D = [(-1,0), (0,1), (1,0), (0,-1)]
 
N,M = map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]
 
# 1. 얼음 녹이기 
# 1-1) 인접한 바다의 개수를 미리 저장해서 그만큼 녹이고
# 1-2) 0이 되면 인접한 셀에 바다 개수 += 1 
def init_adjs():
    adjs = [[0] * M for _ in range(N)]
    n_cell = 0
    for x in range(N):
        for y in range(M):
            if not A[x][y]:
                continue
            n_cell += 1 
            cnt = 0
            for dx,dy in D:
                nx,ny = x+dx, y+dy 
                if 0<=nx<N and 0<=ny<M and not A[nx][ny]:
                    cnt += 1 
            adjs[x][y] = cnt 
    return adjs, n_cell
 
def melt(n_cell):
    tmp = [[ADJS[i][j] for j in range(M)] for i in range(N)]
    for x in range(N):
        for y in range(M):
            if not A[x][y]:
                continue
 
            if A[x][y] <= ADJS[x][y]:
                A[x][y] = 0
                n_cell -= 1 # 새로 된 것만 
                for dx,dy in D:
                    nx,ny = x+dx, y+dy 
                    if 0<=nx<N and 0<=ny<M:
                        tmp[nx][ny] += 1
            else:
                A[x][y] -= ADJS[x][y]
    return tmp, n_cell
 
# 2. 빙산의 개수를 찾기 
def bfs(n_cell):
    done = False 
    for x in range(N):
        for y in range(M):
            if A[x][y]:
                done = True 
                break 
        if done:
            break 
 
    if not done:
        # 다녹음. 
        return None 
 
    q  = deque([(x,y)])
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True 
    cnt = 1
    while q:
        x,y = q.popleft()
        for dx, dy in D:
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M and A[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True 
                q.append((nx,ny))
                cnt += 1 
 
    return n_cell == cnt 
 
ADJS, n_cell = init_adjs()
 
t = 0
while True:
    ADJS, n_cell = melt(n_cell)
    t += 1 
    res = bfs(n_cell)
    if not res or res is None:
        break 
 
print(0 if res is None else t)
    