#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11066                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11066                         #+#        #+#      #+#     #
#     Solved: 2023-12-27 13:18:49 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
input = sys.stdin.readline
T=int(input())
 
def min_cost_to_combine_files(file_sizes):
    n = len(file_sizes)
    # dp[i][j]는 i번째부터 j번째 파일을 합치는데 필요한 최소 비용을 저장합니다.
    dp = [[0] * n for _ in range(n)]
 
    # 누적합을 계산하여 각 구간의 파일 크기 합을 빠르게 구할 수 있도록 합니다.
    sum_sizes = [0] * (n+1)
    for i in range(1, n+1):
        sum_sizes[i] = sum_sizes[i-1] + file_sizes[i-1]
 
    # 작은 구간의 합을 구하고
    # 이를 이용해 다음 구간의 합을 구하고 
 
    # 구간의 크기를 2부터 n까지 증가시키며 최소 비용을 계산합니다.
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
 
            # k를 기준으로 구간을 나누어 최소 비용을 계산합니다.
            for k in range(i, j):
                # 구간의 길이가 작은 것 부터 시작 -> 늘린다
                # 
                cost = dp[i][k] + dp[k+1][j] + sum_sizes[j+1] - sum_sizes[i] # i부터 j까지의 구간합 + 
                dp[i][j] = min(dp[i][j], cost)
 
    return dp[0][n-1]
# 
for _ in range(T):
    K=int(input())
    l = list(map(int, input().split()))
    # 
    dp = [[0] * K for _ in range(K)]
    print(min_cost_to_combine_files(l))
 