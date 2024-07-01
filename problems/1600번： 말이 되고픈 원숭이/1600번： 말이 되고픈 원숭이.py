#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1600                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1600                          #+#        #+#      #+#     #
#     Solved: 2024-04-01 17:30:34 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
D = [(-1,0), (0,1), (1,0), (0,-1)]
H = [(-1,-2), (-1,2), (2,1), (-2,1), (1,2), (1,-2), (2,-1), (-2,-1)]
 
K = int(input())
M,N = map(int,input().split())
A=[list(map(int, input().split())) for _ in range(N)]
 
INF = float("inf")
q = deque([(0,0,0,0)])
visited = [[[INF] * (K+1) for _ in range(M)] for _ in range(N)]
visited[0][0] = [0] * (K+1)
 
while q:
    x,y,d,h = q.popleft()
 
    # 일반 움직임 
    for dx, dy in D:
        nx, ny = x+dx, y+dy 
        if 0<=nx<N and 0<=ny<M and not A[nx][ny] and visited[nx][ny][h] > d+1:
            visited[nx][ny][h] = d+1 
            q.append((nx,ny,d+1, h))
 
    for dx, dy in H:
        nx, ny = x+dx, y+dy 
        if 0<=nx<N and 0<=ny<M and not A[nx][ny] and h < K and visited[nx][ny][h+1] > d+1:
            visited[nx][ny][h+1] = d+1 
            q.append((nx,ny,d+1, h+1))      
 
 
ans = min(visited[-1][-1])
print(ans if ans != INF else -1)