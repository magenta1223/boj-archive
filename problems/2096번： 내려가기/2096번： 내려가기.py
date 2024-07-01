#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2096                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2096                          #+#        #+#      #+#     #
#     Solved: 2024-03-15 15:49:45 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 
 
N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
 
dp_max = A[0]
dp_min = A[0]
 
for i in range(1, N):
    dp_max = [max(dp_max[:2]) + A[i][0], max(dp_max) + A[i][1], max(dp_max[1:]) + A[i][2]]
    dp_min = [min(dp_min[:2]) + A[i][0], min(dp_min) + A[i][1], min(dp_min[1:]) + A[i][2]]
    
print(max(dp_max), min(dp_min))