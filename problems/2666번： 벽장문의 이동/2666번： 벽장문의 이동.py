#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2666                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2666                          #+#        #+#      #+#     #
#     Solved: 2024-03-18 15:31:51 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
left, right = map(int,input().split())
L = int(input()) 
Cabinets = [int(input()) - 1 for _ in range(L)] 
 
INF = float("inf")
dp = [[[INF] * N for _ in range(N)]  for _ in range(L+1)]
dp[0][left-1][right-1] = 0 
for c in range(1,L+1):
    cab = Cabinets[c-1]
    for i in range(N):
        for j in range(N):
            if dp[c-1][i][j] == INF:
                continue
            if cab < j:
                dp[c][cab][j] = min(dp[c-1][i][j] + abs(i-cab), dp[c][cab][j])
            if i < cab:
                dp[c][i][cab] = min(dp[c-1][i][j] + abs(j-cab), dp[c][i][cab])
 
print(min([min(row) for row in dp[-1]]))