#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14442                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14442                         #+#        #+#      #+#     #
#     Solved: 2024-03-13 17:13:12 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
D = [(-1,0), (0,1), (1,0), (0,-1)]
INF = float("inf")
 
N,M,K = map(int,input().split())
B = [list(map(int, input().strip())) for _ in range(N)]
 
 
 
visited = [[[INF] * (K+1) for _ in range(M)] for _ in range(N)]
visited[0][0] = [1] * (K+1)
queue = deque([(0,0,0,1)]) 
 
while queue:
    x,y,k,d = queue.popleft()
    for dx,dy in D:
        nx, ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<M:
            # 벽이면 
            if B[nx][ny] and k < K and visited[nx][ny][k+1] > d+1:
                visited[nx][ny][k+1] = d+1
                queue.append((nx,ny,k+1,d+1))
            elif not B[nx][ny] and visited[nx][ny][k] > d+1:
                visited[nx][ny][k] = d+1 
                queue.append((nx,ny,k,d+1))
 
ans = min(visited[-1][-1])
print(ans if ans != INF else -1)