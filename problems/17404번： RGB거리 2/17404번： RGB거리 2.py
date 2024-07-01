#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17404                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17404                         #+#        #+#      #+#     #
#     Solved: 2024-03-03 15:15:55 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
COSTS = [list(map(int,input().split())) for _ in range(N)]
 
def min_cost_startswith(start_color):
    dp = [[0] * 3  for _ in range(N)]
    dp[0][start_color] = COSTS[0][start_color]
    dp[0][start_color-1] = 1001
    dp[0][start_color-2] = 1001
    for i in range(1, N):
        cost = COSTS[i]
        for j, c in enumerate(cost):
            dp[i][j] = min([dp[i-1][j-1], dp[i-1][j-2]]) + c
    return min([dp[-1][start_color-1], dp[-1][start_color-2]])
 
print(min(min_cost_startswith(c) for c in range(3)))