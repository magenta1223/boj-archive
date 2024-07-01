#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2259                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2259                          #+#        #+#      #+#     #
#     Solved: 2024-06-18 12:10:45 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from math import sqrt 
input = open(0).readline 
INF = float("inf")
N,S = map(int,input().split())
DDG = [list(map(int,input().split())) for _ in range(N)]
DDG.append((0,0,0))
DDG.sort(key= lambda x: x[-1])
dp = [0] * (N+1) 
 
def get_dist(a,b,c,d):
    return sqrt((a-c)**2 + (b-d)**2)
 
for i in range(1,N+1):
    # i번째 두더지를 잡으려면
    res = 0
    for j in range(i):
        # 잡을 수 있음? 
        d = get_dist(*DDG[i][:2], *DDG[j][:2])
        tdiff = DDG[i][-1] - DDG[j][-1]
        if tdiff >= d/S:
            res = max(res, dp[j] + 1)
        # else:
        #     print(f"{j}번째 두더지 직후에 {i} 못잡음. {tdiff}, {d/S}")
    # 한마리도 잡을 수 없는 경우 
    dp[i] = res if res > 0 else -INF
 
print(max(dp))