#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1261                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1261                          #+#        #+#      #+#     #
#     Solved: 2024-07-09 01:49:31 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



# 벽 부수고 이동하기 
# dp array
# dp[i][j]: 0,0에서 i,j에 도달하기 위해 부숴야하는 벽의 최소 갯수
# 


from collections import deque 

INF = float("inf")
D = [(-1,0), (0,1), (1,0), (0,-1)]
M,N = map(int,input().split())
A = [ list(map(int,list(input()))) for _ in range(N)]

dp = [[INF] * M for _ in range(N)]
dp[0][0] = 0 # 항상 뚫려있음
 
q = deque([(0,0)])

while q:
    x,y = q.popleft()
    for dx, dy in D:
        nx,ny = x+dx, y+dy 
        if 0<=nx<N and 0<=ny<M and dp[nx][ny] > dp[x][y] + A[nx][ny]:
            dp[nx][ny] = dp[x][y] + A[nx][ny]
            q.append((nx,ny))

print(dp[-1][-1])
