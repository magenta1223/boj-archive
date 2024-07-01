#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 24479                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/24479                         #+#        #+#      #+#     #
#     Solved: 2024-01-02 11:50:00 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
order = 1
 
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
 
# 각 노드의 인접 노드를 사전에 정렬
for adj in graph:
    adj.sort(reverse=True)
 
stack = [R]
visited[R] = order
 
while stack:
    v = stack[-1]
    if not graph[v]:  # 더 이상 방문할 인접 노드가 없는 경우
        stack.pop()
        continue
 
    u = graph[v].pop()
    if not visited[u]:
        order += 1
        visited[u] = order
        stack.append(u)
 
for i in range(1, N + 1):
    print(visited[i])
 