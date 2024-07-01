#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14940                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14940                         #+#        #+#      #+#     #
#     Solved: 2024-03-05 00:59:46 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
 
N,M=map(int,input().split())
 
 
A = [list(map(int,input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if A[i][j] == 2:
            start = (i,j)
            visited[i][j] = 0
        elif A[i][j] == 0:
            visited[i][j] = 0
x,y = start    
queue = deque([(x,y,0)])
D = [(-1,0),(0,1),(1,0),(0,-1)]
 
 
while queue:
    x,y,c = queue.popleft()
    for dx, dy in D:
        nx,ny = x+dx, y+dy 
        if 0<=nx<N and 0<=ny<M and visited[nx][ny] == -1:
            queue.append((nx,ny,c+1))
            visited[nx][ny] = c+1 
            
for row in visited:
    print(*row)