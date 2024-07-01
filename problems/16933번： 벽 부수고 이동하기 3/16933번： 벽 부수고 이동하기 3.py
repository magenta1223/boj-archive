#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 16933                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/16933                         #+#        #+#      #+#     #
#     Solved: 2024-03-11 17:30:05 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
import sys 
input = sys.stdin.readline
 
N,M,K = map(int,input().split())
A = [list(map(int,list(input().strip()))) for _ in range(N)]
D = [(-1,0), (0,1),(1,0), (0,-1)]
INF = float("inf")
 
# x,y,d,누적 벽 
queue = deque([(0,0,1,0)])
visited = [[[INF for _ in range(K+1)] for _ in range(M)] for _ in range(N)] # 
visited[0][0][0] = 1
 
while queue:
    x,y,d,k = queue.popleft()    
    day = d%2 
    for dx, dy in D:
        nx,ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<M:
            if A[nx][ny] and k < K and visited[nx][ny][k+1] > d+1:
                if day: 
                    visited[nx][ny][k+1] = d+1
                    queue.append((nx,ny,d+1, k+1))
                else:
                    queue.append((x,y,d+1, k))                
            elif not A[nx][ny] and visited[nx][ny][k] > d+1: 
                visited[nx][ny][k] = d+1
                queue.append((nx,ny,d+1,k))
 
ans = min(visited[-1][-1])
print(ans if ans != INF else -1)