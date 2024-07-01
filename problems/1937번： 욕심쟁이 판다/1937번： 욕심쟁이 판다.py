#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1937                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1937                          #+#        #+#      #+#     #
#     Solved: 2024-05-03 13:10:19 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
sys.setrecursionlimit(10**5)
 
D = [(-1,0), (0,1), (1,0), (0,-1)]
N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
dp = [[-1] * N for _ in range(N)]
 
# dfs + dp 
 
def dfs(x,y):
    # 더이상 움직일 수 없다. 
    for dx, dy in D:
        nx, ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<N:
            if A[nx][ny] < A[x][y]:
                break 
    else:
        return 1  
    
    if dp[x][y] != -1:
        return dp[x][y]
 
    res = 0
    for dx, dy in D:
        nx, ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<N and A[nx][ny] < A[x][y]:
            res = max(res, dfs(nx,ny))
 
    dp[x][y] = res+1 
    return dp[x][y]
 
ans = 1
for x in range(N):
    for y in range(N):
        ans = max(ans, dfs(x,y))
print(ans)