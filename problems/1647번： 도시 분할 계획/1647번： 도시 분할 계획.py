#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1647                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1647                          #+#        #+#      #+#     #
#     Solved: 2024-04-08 18:36:42 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import heapq 
input = open(0).readline 
def find(a):
    if parent[a] == a:
        return a 
    parent[a] = find(parent[a])
    return parent[a]
 
N,M = map(int,input().split())
parent = [i for i in range(N+1)]
edges = []
for _ in range(M):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
heapq.heapify(edges)
ans = 0 
while edges:
    c,a,b = heapq.heappop(edges)
    a,b = find(a), find(b)
    if a != b:
        parent[b] = parent[a]
        ans += c 
        last = c  
print(ans - last)