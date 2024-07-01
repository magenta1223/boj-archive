#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1103                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1103                          #+#        #+#      #+#     #
#     Solved: 2024-05-27 10:03:54 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

H="H"
D = [(-1,0),(0,1),(1,0),(0,-1)]
N,M = map(int,input().split())
A = [list(input()) for _ in range(N)]
 
dp = [[-1]*M for _ in range(N)]
 
def dfs(x,y):
    if not (0<=x<N and 0<=y<M) or A[x][y] == H:
        return 0 
 
    if dp[x][y] not in [-1, -2]:
        return dp[x][y]
    
    if dp[x][y] == -2:
        print(-1)
        exit(0)
 
    dp[x][y] = -2 
 
    res = 0
    d = int(A[x][y])
    for dx,dy in D:
        nx,ny = x+d*dx, y+d*dy             
        res = max(res, dfs(nx,ny)+1)
        
    dp[x][y] = res 
    return dp[x][y]
 
print(dfs(0,0))