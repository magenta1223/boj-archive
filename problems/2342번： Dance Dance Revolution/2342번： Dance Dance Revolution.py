#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2342                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2342                          #+#        #+#      #+#     #
#     Solved: 2024-03-06 11:03:45 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

L = list(map(int,input().split()))[:-1]
N = len(L)
COSTS = [         # 시작지점
    [0 ,2,2,2,2], # 0 
    [99,1,3,4,3], # 1  
    [99,3,1,3,4], # 2
    [99,4,3,1,3], # 3
    [99,3,4,3,1], # 4 
]
INF = float("inf")
dp = [[[INF] * 5 for _ in range(5)]  for _ in range(N)]
 
# 첫 명령
c = L[0]
# 왼발로 수행 
dp[0][c][0] = COSTS[0][c]
dp[0][0][c] = COSTS[0][c]
 
# 비용이 존재하는 경우에 업데이트 
for idx in range(1, N):
    c = L[idx]
    for i in range(5):
        for j in range(5):
            if dp[idx-1][i][j] == INF:
                continue
            # 발이 모이는 경우는 없음 
            if c != j:
                dp[idx][c][j] = min(dp[idx][c][j], dp[idx-1][i][j] + COSTS[i][c])
            if c != i:
                dp[idx][i][c] = min(dp[idx][i][c], dp[idx-1][i][j] + COSTS[j][c])
 
print( min([min(row) for row in dp[-1]]))