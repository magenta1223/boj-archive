#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10971                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10971                         #+#        #+#      #+#     #
#     Solved: 2024-08-26 01:00:05 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

INF = float("inf")

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * N for _ in range(1<<N)]

FULL = (1<<N) -1 

def dfs(bitmask, cur):
    if bitmask == FULL:
        return W[cur][0] if W[cur][0] else INF
    
    if dp[bitmask][cur] != -1:
        return dp[bitmask][cur]
    
    dp[bitmask][cur] = INF 
    for next in range(1,N):
        if not W[cur][next] or bitmask & (1<<next):
            continue 
        dp[bitmask][cur] = min(dp[bitmask][cur], dfs(bitmask|(1<<next), next) + W[cur][next])

    return dp[bitmask][cur]

print(dfs(1,0))