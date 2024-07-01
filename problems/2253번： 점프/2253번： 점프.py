#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2253                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2253                          #+#        #+#      #+#     #
#     Solved: 2024-03-29 16:06:44 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

INF = float("inf")
N,M = map(int, input().split())
dp = [[INF] * (200) for _ in range(N+1)]
trap = [False] * (N+1)
for _ in range(M):
    trap[int(input())] = True 
 
dp[1][0] = 0
 
for n in range(1, N+1):
    for x in range(200):
        # 다음으로 뛰기 
        if dp[n][x] == INF:
            continue
        for nx in [x-1, x, x+1]:
            nn = n+nx
            if nx < 0 or nn > N or trap[nn]:
                continue
            dp[nn][nx] = min(dp[nn][nx], dp[n][x] + 1)
ans = min(dp[-1])
print(ans if ans != INF else -1)