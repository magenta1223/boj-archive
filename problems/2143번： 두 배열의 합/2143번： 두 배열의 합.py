#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2143                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2143                          #+#        #+#      #+#     #
#     Solved: 2024-04-08 19:00:37 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import Counter 
def calc_allsubseq(n, arr):
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i,n):
            dp[i][j] = dp[i][j-1] + arr[j]
    agg = []
    for i in range(n):
        agg += dp[i][i:] 
    return dict(Counter(agg))
 
T = int(input())
N, A = int(input()), list(map(int,input().split()))
M, B = int(input()), list(map(int,input().split()))
possible_a = calc_allsubseq(N,A)
possible_b = calc_allsubseq(M,B)
ans = 0
for k, v in possible_a.items():
    if T - k in possible_b:
        ans += v * possible_b[T-k]
print(ans)