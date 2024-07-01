#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1707                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1707                          #+#        #+#      #+#     #
#     Solved: 2024-01-26 18:12:31 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
K=int(input().strip())
for _ in range(K):
    V,E=map(int, input().split())
    G = { i:[] for i in range(1, V+1)}
    for _ in range(E):
        u,v=map(int, input().split())
        G[u].append(v)
        G[v].append(u)
        
    visited = set()
    COLORS = [-1 for _ in range(V+1)]
    NO=False
    
    for start_node in range(1, V+1):
        if start_node not in visited:
            queue = deque([[start_node,0]])    
            while queue and not NO:
                node, color = queue.popleft()
                if node in visited:
                    if COLORS[node] != color: 
                        NO=True
                        break
                    continue
 
                visited.add(node)
                COLORS[node] = color
                next_color = abs(color-1)
                for _node in G[node]:
                    queue.append([_node, next_color])
 
    print("NO" if NO else "YES")