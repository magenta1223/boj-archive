#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1987                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1987                          #+#        #+#      #+#     #
#     Solved: 2024-04-02 15:53:57 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from string import ascii_uppercase
 
D = [(-1,0), (0,1), (1,0), (0,-1)]
R, C = map(int,input().split())
A = [list(input().strip()) for _ in range(R)]
# string bitmask 
A = [[ ascii_uppercase.index(A[r][c])  for c in range(C)] for r in range(R)]
ans = 0 
visited = [[-1] * C for _ in range(R)]
 
def dfs(x,y,bitmask,d):
    global ans 
    if visited[x][y] == bitmask:
        return 
    ans = max(d, ans)
    for dx, dy in D:
        nx, ny = x+dx, y+dy 
        if 0<=nx<R and 0<=ny<C:
            bit = A[nx][ny]
            if (1<<bit) & bitmask:
                continue
            next_bitmask = bitmask|(1<<bit)
            dfs(nx,ny,next_bitmask,d+1)
            visited[nx][ny] = next_bitmask
 
dfs(0,0,1<<A[0][0],1)
print(ans)