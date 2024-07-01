#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1948                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1948                          #+#        #+#      #+#     #
#     Solved: 2024-05-17 10:29:45 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
input = open(0).readline 
 
N,M = int(input()), int(input())
G = {i : [] for i in range(1,N+1)}
count = {i : 0 for i in range(1,N+1)}
costs = [0] *(N+1)
roads = [[] for _ in range(N+1)]
 
for i in range(M):
    a,b,c = map(int,input().split())
    G[a].append((b,c,i))
    count[b] += 1 
 
S,E =  map(int,input().split())
 
q = deque([S])
 
while q:
    now = q.popleft()
    for b,c,idx in G[now]:
        count[b] -= 1
        if costs[b] < costs[now]+c:
            costs[b] = costs[now]+c
            roads[b] = [(now, idx)] 
        elif costs[b] == costs[now] + c:
            roads[b].append((now, idx))
 
        if not count[b]:
            q.append(b)
 
q = deque([E])
routes = set()
while q:
    now = q.popleft()
    for city,road in roads[now]:
        if road in routes:
            continue
        routes.add(road)
        q.append(city)
 
print(costs[E], len(routes), sep = '\n')