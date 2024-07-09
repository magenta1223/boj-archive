#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1194                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1194                          #+#        #+#      #+#     #
#     Solved: 2024-05-21 16:03:21 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
 
input = open(0).readline
 
D = [(-1,0), (0,1),(1,0),(0,-1)]
N,M=map(int,input().split())
A=[list(input()) for _ in range(N)]
KEYS = ['a','b','c','d','e','f']
DOORS = ['A','B','C','D','E','F']
 
for i in range(N):
    for j in range(M):
        v = A[i][j] 
        if v == "0":
            x,y = i,j 
            break 
 
q = deque([(x,y,0,0)])
visited = [[[False] * (1<<6) for _ in range(M)] for _ in range(N)]
 
ans, done = -1, False 
while q and not done:
    x,y,d,k = q.popleft()
    for dx,dy in D:
        nx,ny = x+dx, y+dy 
        if 0<=nx<N and 0<=ny<M and A[nx][ny] != "#" and not visited[nx][ny][k]:
            # 문인데 맞는 키가 없는경우 
            if A[nx][ny] in DOORS and not (1<<KEYS.index(A[nx][ny].lower())) & k:
                continue 
            visited[nx][ny][k] = True
            q.append((nx,ny,d+1,k|(1<<KEYS.index(A[nx][ny])) if A[nx][ny] in KEYS else k))
            if A[nx][ny] == "1":
                done = True 
                ans = d+1
                break 
 
print(ans)