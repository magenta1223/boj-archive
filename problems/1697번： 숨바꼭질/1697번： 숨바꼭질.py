#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1697                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1697                          #+#        #+#      #+#     #
#     Solved: 2024-01-26 13:59:34 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,K=map(int, input().split())
from collections import deque 
queue = deque([[N, 0]])
visited = set()
 
while queue:
    node, depth = queue.popleft()
    visited.add(node)
    if node == K:
        break   
    for node in  [node-1, node+1, node * 2]:
        if node not in visited and 0 <= node <= 100_000:
            queue.append([node, depth + 1])
        
print(depth)