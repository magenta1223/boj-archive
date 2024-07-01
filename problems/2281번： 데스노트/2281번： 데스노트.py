#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2281                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2281                          #+#        #+#      #+#     #
#     Solved: 2024-03-25 19:37:43 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M = map(int,input().split())
 
INF = float("inf")
# dp[i][j] : i번째 이름을 추가했을 때, j번째 칸에서 종료하는 점수의 최솟값 
dp = [[INF for _ in range(M)] for _ in range(N)]
L=[int(input()) for _ in range(N)]
# 종료 index이므로 1 빼줌 
dp[0][L[0]-1] = 0 
for i in range(1,N):
    name = L[i]
    for j in range(M):
        lineChange, next_j = divmod(j+1+name, M)
        if lineChange:
            # 반드시 바꿈. 
            dp[i][name-1] = min(dp[i-1][j] + (M-j-1)**2, dp[i][name-1])
        else:  
            dp[i][name-1] = min(dp[i-1][j] + (M-j-1)**2, dp[i][name-1])
            dp[i][next_j] = min(dp[i-1][j], dp[i][next_j])
            
print(min(dp[-1]))