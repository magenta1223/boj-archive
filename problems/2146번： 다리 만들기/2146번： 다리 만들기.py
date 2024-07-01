#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2146                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2146                          #+#        #+#      #+#     #
#     Solved: 2024-07-01 02:57:17 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

 
from collections import deque 

D = [(-1,0), (0,1), (1,0), (0,-1)]
N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

def findIslands():
    islands = []
    visited = [[False] *N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not A[i][j] or visited[i][j]:
                continue 
            visited[i][j] = True 
            
            q = deque([(i,j)])
            island = [(i,j)]
            while q:
                x,y = q.popleft()
                for dx, dy in D:
                    nx,ny = x+dx, y+dy 
                    if 0<=nx<N and 0<=ny<N and A[nx][ny] and not visited[nx][ny]:
                        visited[nx][ny] = True 
                        q.append((nx,ny))
                        island.append((nx,ny))

            islands.append(island)
    return islands

def shortestPath(islands):
    minD = float("inf")
    for i, islandA in enumerate(islands):
        for ax, ay in islandA:
            for islandB in islands[:i]:
                for bx, by in islandB:
                    # L1거리. 섬 사이에 섬이 있든말든 상관 없다.
                    # 어차피 최소거리 단 하나만을 구하는 것이기 때문에 섬이 사이에 있으면 그 거리가 최소가 될 것 
                    minD = min(abs(ax-bx) + abs(ay-by), minD)
    return minD 

print(shortestPath(findIslands())-1)