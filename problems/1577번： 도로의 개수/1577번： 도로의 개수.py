#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1577                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1577                          #+#        #+#      #+#     #
#     Solved: 2024-03-27 17:06:39 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M = map(int,input().split())
K = int(input()) # 0~50
 
blocked = set()
for _ in range(K):
    a,b,c,d = map(int,input().split())
    blocked.add((a,b,c,d))
 
dp = [[0] * (M+1) for _ in range(N+1)]
dp[0][0] = 1
 
def cond(a,b,c,d):
    return False if (a,b,c,d) in blocked or (c,d,a,b) in blocked else True 
 
for i in range(N+1):
    for j in range(M+1):
        if not i and not j:
            continue
        if cond(i,j,i-1,j):
            dp[i][j] += dp[i-1][j]
        if cond(i,j,i,j-1):
            dp[i][j] += dp[i][j-1]
 
# print(*dp, sep = '\n')
print(dp[-1][-1])