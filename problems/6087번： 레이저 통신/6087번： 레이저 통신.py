#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 6087                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/6087                          #+#        #+#      #+#     #
#     Solved: 2024-02-29 11:15:50 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
W,H = map(int,input().split())
A = [list(input().strip()) for _ in range(H)]
D = [(-1,0), (0,1), (1,0), (0,-1)]
# 입사각, 거울 
lasor_reflect = {
    0 : {'/' : 1, '\\' : 3,}, # up 
    1 : {'/' : 0, '\\' : 2,}, # right
    2 : {'/' : 3, '\\' : 1,}, # down
    3 : {'/' : 2, '\\' : 0,}, # left
}
 
start, end = [(i,j) for i in range(H) for j in range(W) if A[i][j] == 'C']
for x,y in [start,end]:
    A[x][y] = '.'
 
x,y = start
queue = deque([(x,y,d,0) for d in range(4)])
visited = [[[-1] * 4 for _ in range(W)] for _ in range(H)]
visited[x][y][0] = -1
visited[x][y][1] = -1
visited[x][y][2] = -1
visited[x][y][3] = -1
 
ans = H*W
 
while queue:
    x,y,d,n_mirror = queue.popleft()
    # if (x,y) == end:
    #     ans = min(ans, n_mirror)
 
    dx,dy = D[d]
    nx,ny = x+dx, y+dy
    if 0<=nx<H and 0<=ny<W and A[nx][ny] == ".":
        # 같은 거울을 반대에서 다시 마주치는 경우 -> 불필요한 탐색
        # 그냥 직진 or 거울 2가지만 고려하면 된다. 
        
        # 방문하지 않았거나, 방문했더라도 거울을 더 적게 사용하면 
        if visited[nx][ny][d] == -1 or visited[nx][ny][d] > n_mirror:
            if (nx,ny) == end:
                ans = min(ans, n_mirror)
                
            visited[nx][ny][d] = n_mirror 
            # 직진
            queue.append((nx,ny,d, n_mirror))
 
            
            # 거울
            queue.append((nx,ny,lasor_reflect[d]['/'], n_mirror+1))
            queue.append((nx,ny,lasor_reflect[d]['\\'], n_mirror+1))
            
print(ans)
 