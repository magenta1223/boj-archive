#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1311                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1311                          #+#        #+#      #+#     #
#     Solved: 2024-06-12 15:40:27 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]
INF = float("inf")
dp = [[INF] * N for _ in range(1<<N)]
 
def dfs(bitmask, idx):
    if idx == N:
        return 0
    
    if dp[bitmask][idx] != INF:
        return dp[bitmask][idx]
    
    res = INF 
    for i in range(N):
        if (1<<i) & bitmask:
            continue 
        # i번째 일을 했음. 누가? 남은 사람 중 가장 비용이 작은사람이. 
        res = min(res, dfs(bitmask|(1<<i), idx+1) + D[idx][i])  
    dp[bitmask][idx] = res 
    return dp[bitmask][idx]
print(dfs(0,0))