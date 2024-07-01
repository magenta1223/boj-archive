#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1208                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1208                          #+#        #+#      #+#     #
#     Solved: 2024-03-05 16:06:28 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,S=map(int,input().split())
L = list(map(int,input().split()))
 
left, right = L[:N//2], L[N//2:] 
 
# 각 수열로 부분수열의 합을 전부 구하면 됨 
from collections import Counter 
 
def solve(array):
    n = len(array) 
    dp = [0] * (1<<n)
    # 모든 조합의 합, 그 개수를 구하면 됨 
    for i in range(1<<n):
        for j in range(n):
            if i & (1<<j):
                continue
            # 새 조합 구하기 
            dp[i|(1<<j)] = dp[i] + array[j]
    return Counter(dp)
 
left = solve(left)
right = solve(right)
ans = 0 
for k, v in left.items():
    if S-k in right:
        ans += right[S-k] * left[k]
 
# left에 
print(ans-1 if S ==0 else ans)