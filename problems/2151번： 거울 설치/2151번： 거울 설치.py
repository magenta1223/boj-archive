#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2151                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2151                          #+#        #+#      #+#     #
#     Solved: 2024-02-29 15:10:15 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
A=[list(input().strip()) for _ in range(N)]
 
from collections import deque 
 
D = [(-1,0), (0,1), (1,0), (0,-1)]
 
start, end = [(i,j) for i in range(N) for j in range(N) if A[i][j] == "#"]
 
 
mirroring = {
    0 : [1,3], # up
    1 : [0,2], # right
    2 : [3,1], # down
    3 : [2,0], # left 
}
 
ans = float("inf")
x,y=start
queue = deque([(x,y,d,0) for d in range(4)])
visited = [[[0] *4 for _ in range(N)] for _ in range(N)]
while queue:
    x,y,d,mirror = queue.popleft()
    dx,dy = D[d]
    nx,ny = x+dx, y+dy 
    # 거울 개수를 세야 함. 
    if 0<=nx<N and 0<=ny<N and A[nx][ny] != '*':
        if not visited[nx][ny][d] or visited[nx][ny][d] > mirror:
            visited[nx][ny][d] = mirror
            # 지나갈 수 있음. 
            queue.append((nx,ny,d,mirror))
            # 만약 거기가 문이라면 -> 끝
            if A[nx][ny] == "!":
                # 거울설치 쌉가능
                queue.append((nx,ny,mirroring[d][0], mirror+1))
                queue.append((nx,ny,mirroring[d][1], mirror+1))
            elif (nx,ny) == end:
                ans = min(ans, mirror)
print(ans)