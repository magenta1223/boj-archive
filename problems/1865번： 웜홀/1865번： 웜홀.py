#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1865                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1865                          #+#        #+#      #+#     #
#     Solved: 2024-03-29 21:21:50 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

INF = 10 **10 # float("inf")
input = open(0).readline
 
def bellman_ford(start, n, edges):
    dist = [INF] * (n+1)
    dist[start] = 0
    for i in range(n):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                # N번째 루프에서 값이 갱신되면 음수 사이클이 존재
                if i == n-1:
                    return True
    return False
 
for _ in range(int(input())):
    N,M,Wo = map(int,input().split())
    edges = []
    for _ in range(M):
        S,E,T = map(int,input().split())
        edges.append([S,E,T])
        edges.append([E,S,T])
    for _ in range(Wo):
        S,E,T = map(int,input().split())
        edges.append([S,E,-T])
 
    if bellman_ford(1, N, edges):
        print("YES")
    else:
        print("NO")