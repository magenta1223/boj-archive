#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1766                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1766                          #+#        #+#      #+#     #
#     Solved: 2024-04-08 18:14:35 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import heapq
 
input = open(0).readline 
N, M = map(int,input().split())
 
count = {i : 0 for i in range(1,N+1)}
connect  = {i : [] for i in range(1,N+1)}
 
for _ in range(M):
    a,b =  map(int,input().split())
    count[b] += 1 
    connect[a].append(b)
 
q = [i for i in range(1,N+1) if not count[i]]
heapq.heapify(q)
ans = []
 
while q:
    x = heapq.heappop(q)
    ans.append(x)
    for nx in connect[x]:
        count[nx] -= 1
        if not count[nx]:
            heapq.heappush(q, nx)
 
print(" ".join(map(str, ans)))