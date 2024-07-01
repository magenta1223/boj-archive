#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2606                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2606                          #+#        #+#      #+#     #
#     Solved: 2024-01-03 10:41:36 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input()) # n_edge
linked_list = { i : [] for i in range(N+1)} 
for _ in range(int(input())):
    u,v = map(int, input().split())
    linked_list[u].append(v)
    linked_list[v].append(u)
stack = [1]
visited = [False] * (N+1)
while stack:
    node = stack.pop()
    if not visited[node]:
        visited[node] = True
        stack.extend(linked_list[node])
 
# while stack:
#     node = stack.pop()
#     for _ in range(len(linked_list[node])):
#         new_node = linked_list[node].pop()
#         if not visited[new_node]:
#             visited[new_node] = True    
#             stack.append(new_node)
print(sum(visited) -1)