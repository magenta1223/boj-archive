#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 16946                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/16946                         #+#        #+#      #+#     #
#     Solved: 2024-02-29 20:48:07 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
import sys
input = sys.stdin.readline
 
 
N,M = map(int,input().split())
A = [list(map(int, input().rstrip())) for _ in range(N)]
D = [(-1,0), (0,1), (1,0), (0,-1)]
visited = [[False] * M for _ in range(N)]
ANS = [[0] * M for _ in range(N)]
G = [[0] * M for _ in range(N)]
AREA = dict()
 
g = 1
for i in range(N):
    for j in range(M):
        if not A[i][j] and not visited[i][j]:
            visited[i][j] = True 
            queue = deque([(i,j)])
            cnt = 1
            G[i][j] = g
            while queue:
                x,y = queue.popleft()
                for dx, dy in D:
                    nx,ny = x+dx, y+dy 
                    if 0<=nx<N and 0<=ny<M and not A[nx][ny] and not visited[nx][ny]:
                        queue.append((nx,ny))
                        G[nx][ny] = g
                        visited[nx][ny] = True
                        cnt += 1
            AREA[g] = cnt
            g += 1
            
for i in range(N):
    for j in range(M):
        if A[i][j]:
            groups = set()
            # 벽이 있는 곳의 인접한 빈칸 
            for dx, dy in D:
                nx, ny = i+dx, j+dy 
                if 0<=nx<N and 0<=ny<M and not A[nx][ny]:
                    groups.add(G[nx][ny])
            ANS[i][j] = str((1 + sum([AREA[g] for g in groups])) % 10)
        else:
            ANS[i][j] = "0"
for row in ANS:
    print(''.join(row))