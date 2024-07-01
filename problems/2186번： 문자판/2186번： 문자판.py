#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2186                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2186                          #+#        #+#      #+#     #
#     Solved: 2024-03-05 13:47:04 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline
 
N,M,K = map(int,input().split())
A=[list(input().strip()) for _ in range(N)]
T = input().strip()
D = []
for i in range(1,K+1):
    D.extend([(-i,0), (0,i), (i,0), (0,-i)])
    
# -1
dp = [[[-1] * len(T) for _ in range(M)] for _ in range(N)]
# dp[i][j][k] =  
# dp의 i,j에서 target[k:] 문자열을 만드는 방법의 수 
def dfs(x,y,i):
    if i == len(T)-1:
        return 1 
    if dp[x][y][i] != -1:
        return dp[x][y][i]    
    # if dp[x][y][i]: # 0으로 설정 시 -> 실제로 완성하는 방법이 없어 값이 0인 상황에서도 다시 찾게됨
    #     return dp[x][y][i]    
    cnt = 0
    for dx, dy in D:
        nx,ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<M and T[i+1] == A[nx][ny]:
            cnt += dfs(nx,ny,i+1)
    dp[x][y][i] = cnt
    return dp[x][y][i] 
 
ans = 0
 
for i in range(N):
    for j in range(M):
        if A[i][j] == T[0]:
            ans += dfs(i,j,0)
 
print(ans)