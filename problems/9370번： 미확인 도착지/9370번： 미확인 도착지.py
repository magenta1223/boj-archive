#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 9370                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/9370                          #+#        #+#      #+#     #
#     Solved: 2024-01-29 18:36:47 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def solve(s, G):
    costs = [float(10**9) for _ in range(n+1)]
    costs[s] =0
    heap = [(0,s)]
    
    while heap:
        cost, node = heapq.heappop(heap)
        if cost > costs[node]:
            continue
        for v, w in G[node]:
            if costs[v] > cost + w:
                costs[v] = cost + w
                heapq.heappush(heap, (costs[v], v))
 
    return costs
 
import heapq
 
T = int(input().strip())
 
for _ in range(T):
    n,m,t = map(int, input().split()) # node, edge, goal 후보 개수
    s,g,h = map(int, input().split()) # 시작점, g-h를 잇는 edge를 지났음.
    G = { i : [] for i in range(n+1)}
    # edges
    for _ in range(m):
        a,b,d = map(int, input().split())
        G[a].append((b,d))
        G[b].append((a,d))
    xs = [int(input().strip()) for _ in range(t)]
    
    # 다익스트라 
    depart_s = solve(s,G)
    depart_g = solve(g,G)
    depart_h = solve(h,G)
    results = []
    for x in xs:
        if depart_s[g] + depart_g[h] + depart_h[x] == depart_s[x] or depart_s[h] + depart_h[g] + depart_g[x] == depart_s[x]:
            results.append(x)
 
    print(*sorted(results))