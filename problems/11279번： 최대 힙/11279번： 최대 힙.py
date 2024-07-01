#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11279                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11279                         #+#        #+#      #+#     #
#     Solved: 2023-12-27 11:18:02 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
import heapq 
input = sys.stdin.readline
N=int(input())
heap = []
for _ in range(N):
    x = int(input())
    if not x:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -x)