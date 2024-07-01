#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2515                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2515                          #+#        #+#      #+#     #
#     Solved: 2024-06-04 14:18:21 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline
N,S = map(int,input().split())
PAINTINGS = [list(map(int,input().split())) for _ in range(N)]
PAINTINGS.sort(key = lambda x: x[0])
dp = [0] * N 
h,c = PAINTINGS[0]
dp[0] = c if h >= S else 0 
 
for i in range(1,N):
    h,c = PAINTINGS[i]   
    lo, hi = 0,i 
    x = h-S+1
    while lo < hi:
        mid = (lo+hi)//2
        if PAINTINGS[mid][0] < x:
            lo = mid+1
        else:
            hi = mid
    idx = lo 
    dp[i] = max(dp[i-1], dp[idx-1]+c)
print(dp[-1])