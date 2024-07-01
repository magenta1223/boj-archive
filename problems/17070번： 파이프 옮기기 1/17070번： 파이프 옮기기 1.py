#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17070                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17070                         #+#        #+#      #+#     #
#     Solved: 2024-04-04 14:14:55 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def vaild(x,y):
    return True if not A[x][y] else False
 
def check(x,y,d):
    return vaild(x,y) and vaild(x-1,y) and vaild(x,y-1) if d==1 else vaild(x,y)     
 
D = {0: [(0,1,0), (1,1,1)], 1: [(0,1,0), (1,0,2), (1,1,1)], 2:  [(1,0,2), (1,1,1)]}
N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
# dfs + dp 
dp = [[[-1] * 3 for _ in range(N)] for _ in range(N)] 
def dfs(x,y,d):
    if (x,y) == (N-1,N-1):
        return 1 
    if dp[x][y][d] != -1:
        return dp[x][y][d]
    dp[x][y][d] = 0
    for dx,dy,nd in D[d]:
        nx,ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<N:
            if check(nx,ny,nd):
                dp[x][y][d] += dfs(nx,ny,nd)
            else:
                dp[nx][ny][nd] = 0 
    return dp[x][y][d]
print(dfs(0,1,0))