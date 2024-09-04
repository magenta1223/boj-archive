#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17071                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17071                         #+#        #+#      #+#     #
#     Solved: 2024-09-02 02:43:52 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


from collections import deque

N,K = map(int, input().split())
q = deque([(N,0,K)])
INF = float("inf")
dp = [[INF] *2 for _ in range(500001)]
dp[N][0%2] = 0 
while q:
    x, t, target = q.popleft()
    nt = t+1 
    nextTarget = target+nt
    if nextTarget > 500_000:
        continue 
    r = nt%2 # 홀짝 
    for nx in [x-1,x+1,2*x]:
        if 0<=nx<=500_000 and dp[nx][r] == INF:
            dp[nx][r] = nt
            q.append((nx,nt,nextTarget))
sec = 0 
while K<=500_000 and dp[K][sec%2] > sec:
    sec+=1 
    K+=sec 
print(-1 if K>500_000 or dp[K][sec%2] > sec else sec)
