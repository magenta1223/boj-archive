#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2631                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2631                          #+#        #+#      #+#     #
#     Solved: 2024-03-15 16:06:47 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
L = [int(input()) for _ in range(N)]
# 최대 이동수는 N임. 그냥 순서대로 찾아 옮기면 그만. 
# LIS문제임. 
from bisect import bisect_left 
LIS = []
for i in range(N):
    idx = bisect_left(LIS, L[i])
    if idx >= len(LIS):
        LIS.append(L[i])
    else:
        LIS[idx] = L[i]
print(N-len(LIS))