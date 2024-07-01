#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11049                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11049                         #+#        #+#      #+#     #
#     Solved: 2023-12-27 14:32:00 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
M = [list(map(int, input().split())) for _ in range(N)]
 
# dp[i][j] : i번째 행렬부터 j번째 행렬까지 곱할 때 계산량의 최소값
# 일단 인접한 행렬의 계산량을 다 구해서 넣고
# 곱해지는 행렬 개수는 1~N
dp = [[0] * N for _ in range(N)]
 
def calc(A, B):
    return A[0] * B[0] * B[1]
for i in range(N-1):
    dp[i][i+1] = calc(M[i], M[i+1])
for length in range(2, N):
    for i in range(N-length):
        j = i + length
        dp[i][j] = float('inf')
        for k in range(i, j):
            Ma = [M[i][0], M[k][1]]
            Mb = [M[k+1][0], M[j][1]]
            cost = dp[i][k] + dp[k+1][j] + calc(Ma, Mb) 
            dp[i][j] = min(dp[i][j], cost)
 
print(dp[0][-1])