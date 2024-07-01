#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2306                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2306                          #+#        #+#      #+#     #
#     Solved: 2024-03-12 21:03:56 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

S = list(input().strip())
N = len(S)
 
# bottom up 
# dp[i][j] = gene[i:j+1]을 사용해 만든 KOI의 최대 길이 
dp = [[-1] * N for _ in range(N)]
 
 
def dfs(x,y):
    if x+1 == y:
        if (S[x] =='a' and  S[y]=='t') or (S[x] =='g' and  S[y]=='c'):
            dp[x][y] = 2
            return 2
        else:
            dp[x][y] = 0
            return 0
    if x == y:
        return 0 
    if dp[x][y] != -1:
        return dp[x][y]
    if (S[x] =='a' and  S[y]=='t') or (S[x] =='g' and  S[y]=='c'):
        dp[x][y] = max(dp[x][y],dfs(x+1, y-1)+2)
    for k in range(x,y):
        dp[x][y] = max(dp[x][y], dfs(x,k)+dfs(k+1,y))
    return dp[x][y]
 
dfs(0,N-1)
print(dp[0][-1])