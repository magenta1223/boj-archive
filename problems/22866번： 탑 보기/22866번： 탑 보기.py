#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 22866                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/22866                         #+#        #+#      #+#     #
#     Solved: 2024-05-09 13:40:31 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
A = list(map(int,input().split()))
INF = float("inf")
 
def func(d):
    dp = [0] * N
    nearest = [INF] * N
    for i in range(*[N-2, -1, -1] if d == 1 else [1,N]):
        j = i+d 
        while 0<j<N-1 and A[i] >= A[j]:
            j+=d 
        if A[i] < A[j]:
            dp[i] += dp[j] + 1 
            nearest[i] = j
 
    return dp, nearest
 
dp_left, near_left = func(-1) 
dp_right, near_right = func(1)
 
 
for i in range(N):
    n = dp_left[i] + dp_right[i]
    if n:
        # 가장 가까운 것 중 작은것 
        diff_l, diff_r = abs(i-near_left[i]), near_right[i] - i        
        if diff_l <= diff_r:
            nearest = near_left[i]
        else:
            nearest = near_right[i]
        print(n, nearest+1)
    else:
        print(0)