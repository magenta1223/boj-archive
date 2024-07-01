#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 5213                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/5213                          #+#        #+#      #+#     #
#     Solved: 2024-03-08 13:54:17 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
input = open(0).readline 
 
def to(v, dest):
    # dest = tile or coords 
    if dest == "tile":
        i,j = v
        t = (i//2)*(2*N-1)
        t += (N +(j-1)//2) if i % 2 else j//2 
        return t
    else:
        x,y = divmod(v, N+N-1)
        a,b = divmod(y, N)
        row = 2*x+a
        return row, b*2+1 if row % 2 else b*2 
 
D = [(-1,0), (0,1), (1,0), (0,-1)]
 
N = int(input())
n_row, n_col = N, 2*N
A = [ [0] * (2*N)  for _ in range(N)] # value array 
T = [(0,0) for i in range(N*N-N//2)] # tile to coords 
 
for i in range(N*N-N//2):
    bx, by = to(i, "coords")
    A[bx][by:by+2] = map(int,input().split())
    T[i] = (bx,by)
 
queue = deque([(0,1,1)])
visited = [[0] * (2*N) for _ in range(N)]
visited[0][0:2] = 1,1
hist = [-1 for _ in range(N*N-N//2)]
 
while queue:
    x,y,n_tiles = queue.popleft()
    for dx, dy in D:
        nx, ny = x+dx, y+dy
        if 0<=nx<n_row and 0<=ny<n_col and A[nx][ny]:
            tile, next_tile = to((x,y), "tile"), to((nx,ny), "tile")
            if tile != next_tile and A[x][y] == A[nx][ny] and not visited[nx][ny]:
                # 다른 타일, 같은 값 
                # 타일 내의 다른 값도 visit 처리 
                nx,ny = T[next_tile] 
                queue.append((nx,ny,n_tiles+1))      
                queue.append((nx,ny+1,n_tiles+1))      
                visited[nx][ny] = n_tiles + 1
                visited[nx][ny+1] = n_tiles + 1
                hist[next_tile] = tile
                
for t in range(N*N-N//2-1,-1,-1):
    x, y = T[t]
    if visited[x][y]:
        break
path = []
while hist[t] != -1:
    path.append(t+1)
    t = hist[t]
path.append(1)
path.reverse()
print(visited[x][y])
print(*path)