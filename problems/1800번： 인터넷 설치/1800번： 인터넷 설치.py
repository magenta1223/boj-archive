#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1800                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1800                          #+#        #+#      #+#     #
#     Solved: 2024-05-07 16:29:36 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from heapq import heappush,heappop
 
input = open(0).readline
INF=1e9
 
N,P,K = map(int,input().split())
 
G = [[] for _ in range(N)]
for i in range(P):
    x,y,w = map(int,input().split())
    G[x-1].append((y-1,w))
    G[y-1].append((x-1,w))
 
DP = [[INF]*N for _ in range(K+1)]
heap = []
heappush(heap,(0,0))
 
while heap:
    w, cur_node = heappop(heap)
    if DP[0][cur_node] <= w:
        continue
    DP[0][cur_node] = w
    for next_node, nw in G[cur_node]:
        heappush(heap,(max(w,nw), next_node))
 
for k in range(1,K+1):
    heap = []
    heappush(heap,(0,0))
    while heap:
        w, cur_node = heappop(heap)
        if DP[k][cur_node] <= w:
            continue
        DP[k][cur_node] = w
        for next_node, nw in G[cur_node]:
            heappush(heap,(DP[k-1][cur_node], next_node))
            heappush(heap,(max(w,nw), next_node))
 
if DP[K][N-1] == INF:
    print(-1)
else:
    print(DP[-1][-1])