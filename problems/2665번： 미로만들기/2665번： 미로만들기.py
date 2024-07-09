#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2665                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2665                          #+#        #+#      #+#     #
#     Solved: 2024-07-09 02:00:33 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 

INF = float("inf")
D = [(-1,0), (0,1), (1,0), (0,-1)]
N = int(input())
A = [ list(map(int,list(input()))) for _ in range(N)]
A = [[abs(A[i][j] - 1) for j in range(N)] for i in range(N)]

dp = [[INF] * N for _ in range(N)]
dp[0][0] = 0 # 항상 뚫려있음
 
q = deque([(0,0)])

while q:
    x,y = q.popleft()
    for dx, dy in D:
        nx,ny = x+dx, y+dy 
        if 0<=nx<N and 0<=ny<N and dp[nx][ny] > dp[x][y] + A[nx][ny]:
            dp[nx][ny] = dp[x][y] + A[nx][ny]
            q.append((nx,ny))

print(dp[-1][-1])
