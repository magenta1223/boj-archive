#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2109                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2109                          #+#        #+#      #+#     #
#     Solved: 2024-07-30 02:36:50 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from heapq import heappop, heappush 
input = open(0).readline 
N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
A.sort(key=lambda x:x[1])
q = []
for p,d in A:
    heappush(q, p)
    while len(q) > d:
        heappop(q)
print(sum(q))