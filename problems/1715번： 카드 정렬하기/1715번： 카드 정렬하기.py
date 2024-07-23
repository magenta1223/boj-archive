#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1715                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1715                          #+#        #+#      #+#     #
#     Solved: 2024-07-23 06:25:45 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


input = open(0).readline 
from heapq import heappop, heappush, heapify

N = int(input())
A = [int(input()) for _ in range(N)]
heapify(A)

ans = 0 
while len(A) > 1:
    a,b = heappop(A), heappop(A)
    ans += a+b 
    heappush(A, a+b)
print(ans)
