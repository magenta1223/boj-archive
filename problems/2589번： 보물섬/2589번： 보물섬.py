#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2589                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2589                          #+#        #+#      #+#     #
#     Solved: 2024-08-14 01:17:10 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


from collections import deque 

N,M = map(int,input().split())
A = [list(input().strip()) for _ in range(N)]
D = [(-1,0), (0,1), (1,0), (0,-1)]
# 1. 모든 L에서 시작 -> 최대 시간을 구한다. 

def bfs(i,j):
    visited = [[False] * M for _ in range(N)]
    visited[i][j] = True 
    q = deque([(i,j,0)])

    while q:
        x,y,t = q.popleft()

        for dx,dy in D:
            nx,ny = x+dx,y+dy 
            if 0<=nx<N and 0<=ny<M and A[nx][ny] == "L" and not visited[nx][ny]:
                q.append((nx,ny,t+1))
                visited[nx][ny] = True 
    return t 

print(max([ bfs(i,j) for i in range(N) for j in range(M) if A[i][j] == "L"]))