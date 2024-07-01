#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1260                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1260                          #+#        #+#      #+#     #
#     Solved: 2024-01-05 10:58:27 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M,V=map(int, input().split())
linked_list = { i : [] for i in range(N+1)}
for _ in range(M):
    u,v=map(int, input().split())
    linked_list[u].append(v)
    linked_list[v].append(u)
    
ll_dfs = {k : sorted(v, reverse= True) for k, v in linked_list.items()}
ll_bfs = {k : sorted(v) for k, v in linked_list.items()}
 
# dfs 
stack = [V]
visited = [False for _ in range(N+1)]
result = []
while stack:
    node = stack.pop()
    if not visited[node]:
        visited[node]=True
        result.append(node)
        stack.extend(ll_dfs[node])
print(*result)
 
# bfs
from collections import deque
 
stack = deque([V])
visited = [0 for _ in range(N+1)]
result = []
while stack:
    node = stack.popleft()
    if not visited[node]:
        visited[node]=True
        result.append(node)
        stack.extend(ll_bfs[node])
print(*result)
 