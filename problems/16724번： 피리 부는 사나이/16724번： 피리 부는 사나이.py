#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 16724                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/16724                         #+#        #+#      #+#     #
#     Solved: 2024-04-11 15:10:23 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
D = {"D" : (1,0), "U" : (-1,0), "L" : (0,-1), "R" : (0,1)}
 
N,M = map(int,input().split())
A = [list(input().strip()) for _ in range(N)] 
visited = [[False] * M for _ in range(N)]
ans = 0
n_cycle = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        q = deque([(i,j)])
        n_cycle += 1 
        while q:
            x,y = q.popleft()
            dx,dy = D[A[x][y]]
            nx,ny = x+dx, y+dy
            if not visited[nx][ny]:
                visited[nx][ny] = n_cycle 
                q.append((nx,ny))
            elif visited[nx][ny] == n_cycle:
                # 사이클임. 
                ans += 1 
            else:
                # 이전에 만들어진 사이클임. 
                pass 
 
print(ans)