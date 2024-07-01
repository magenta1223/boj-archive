#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2170                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2170                          #+#        #+#      #+#     #
#     Solved: 2024-05-22 19:44:47 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from heapq import heappop, heappush
 
input = open(0).readline 
N=int(input())
LINES = []
for _ in range(N):
    a,b = map(int,input().split())
    heappush(LINES, (a,b))
 
s,e = heappop(LINES)
ans = e-s
 
while LINES:
    a,b = heappop(LINES)
    if s <= a and b <= e:
        continue 
    elif e <= a:
        ans += b-a
        s,e = a,b
    else:
        ans += b-e 
        e = b
print(ans)