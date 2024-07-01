#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 21736                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/21736                         #+#        #+#      #+#     #
#     Solved: 2024-03-29 20:01:20 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
 
N, M = map(int, input().split())
A = [list(input().strip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
q = False 
for i in range(N):
    for j in range(M):
        if A[i][j] == "I":
            q = deque([(i,j)])
            visited[i][j] = True
            break 
    if q:
        break 
ans = 0
D = [(-1,0), (0,1), (1,0), (0,-1)]
 
while q:
    x,y = q.popleft()
    for dx, dy in D:
        nx, ny = x+dx, y+dy 
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and A[nx][ny] != "X":
            q.append((nx,ny))
            visited[nx][ny] = True 
            if A[nx][ny] == "P":
                ans += 1 
 
print(ans if ans else "TT")