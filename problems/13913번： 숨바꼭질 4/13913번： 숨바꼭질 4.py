#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 13913                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/13913                         #+#        #+#      #+#     #
#     Solved: 2024-02-07 11:58:35 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,K=map(int,input().split())
from collections import deque
queue = deque([[N,0]])
visited = set([N])
history = dict()
while queue:
    node,t = queue.popleft()
    if node == K:
        break
    for next_node in [node-1, node+1, node*2]:
        if next_node not in visited and 0<= next_node <= 100_000:
            visited.add(next_node)
            queue.append([next_node, t+1])
            history[next_node] = node 
 
path = []
node = K
while node != N:
    path.append(node)
    node = history[node]
path.append(N)
path.reverse()
print(t)
print(*path)