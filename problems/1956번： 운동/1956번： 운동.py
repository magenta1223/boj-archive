#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1956                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1956                          #+#        #+#      #+#     #
#     Solved: 2024-01-31 11:02:41 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

V, E = map(int, input().split())
INF = float('inf')
graph = [[INF] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
min_cycle = INF
for i in range(1, V + 1):
    min_cycle = min(min_cycle, graph[i][i])
 
if min_cycle == INF:
    print(-1)
else:
    print(min_cycle)