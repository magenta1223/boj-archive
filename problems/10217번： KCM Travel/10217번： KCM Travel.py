#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10217                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10217                         #+#        #+#      #+#     #
#     Solved: 2024-03-05 11:25:28 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
INF = float("inf")
T = int(input())
for _ in range(T):
    N,M,K = map(int,input().split())
    G = {i : [] for i in range(1,N+1)}
    for _ in range(K):
        u,v,c,d = map(int,input().split())
        G[u].append((v,c,d))
 
    # dp array 
    # dp[i][j] = i번째 도시에 j원에 도착하는 최소거리 
    dp = [[INF] * (M+1) for _ in range(N+1)]
    dp[1][0] = 0
    for c in range(M+1):
        for d in range(1, N+1):
            if dp[d][c] == INF:
                continue
            # 다음 도시?
            for ncity,nc,nd in G[d]:
                if c+nc > M:
                    continue
                dp[ncity][nc+c] = min(dp[ncity][nc+c], dp[d][c] + nd)
    
    
    ans = min(dp[-1])
    print(ans if ans != INF else "Poor KCM" )