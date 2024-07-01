#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11657                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11657                         #+#        #+#      #+#     #
#     Solved: 2024-01-30 17:40:10 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

V,E=map(int, input().split())
G = []
for _ in range(E):
    u,v,w = map(int, input().split())
    G.append((u,v,w))
 
heap = [(0, 1)]
costs = [float("inf") for _ in range(V+1)]
costs[1] = 0
 
for _ in range(V):
    for u,v,w in G:
        if costs[u] != float("inf") and costs[v] > costs[u] + w:
            costs[v] = costs[u] + w
 
for u,v,w in G:
    if costs[u] != float("inf") and costs[v] > costs[u] + w:
        costs = None
        break 
 
if costs is None:
    print(-1)
else:
    for c in costs[2:]:
        if c == float("inf"):
            print(-1)
        else:
            print(c)