#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2098                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2098                          #+#        #+#      #+#     #
#     Solved: 2024-03-25 16:07:47 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
W = [list(map(int,input().split())) for _ in range(N)]
# x에서 visited 이외의 도시를 전부 방문, 돌아오는 최소 비용 
dp = [ [-1] * (1<<N) for _ in range(N)]
# DFS + DP 
 
def dfs(x, visited):
    # 종료조건 
    if visited == ((1<<N) - 1):
        return W[x][0] if W[x][0] else  float("inf")
 
    if dp[x][visited] != -1:      
        # 이미 최소비용이 계산되어 있다면
        return dp[x][visited]
    dp[x][visited] = float('inf')
    for i in range(1,N):
        # 이동 불가 or 이미 방문 
        if not W[x][i] or (visited & (1<<i)):
            continue
        dp[x][visited] = min(dp[x][visited], dfs(i, (1<<i) | visited) + W[x][i])
    return dp[x][visited] 
print(dfs(0,1))