#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 13334                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/13334                         #+#        #+#      #+#     #
#     Solved: 2024-05-22 19:25:48 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from heapq import heappop, heappush 
 
input = open(0).readline
 
N=int(input())
 
LINES = []
for _ in range(N):
    a,b = map(int,input().split())
    if a>b:
        a,b = b,a
    heappush(LINES, (b,a))
D = int(input())
 
idx = 0
 
peoples = []
ans = 0
while LINES:
    e,s = heappop(LINES)
    l,r = e-D, e
    heappush(peoples, (s,e))
    while peoples and peoples[0][0] < l:
        heappop(peoples)
 
    ans = max(ans, len(peoples))
 
print(ans)