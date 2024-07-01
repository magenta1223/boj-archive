#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 16928                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/16928                         #+#        #+#      #+#     #
#     Solved: 2024-01-26 16:28:44 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M=map(int, input().split())
LADDERS = {depart : arrive  for depart, arrive in [list(map(int, input().split())) for _ in range(N)]}
SNAKES = {depart : arrive  for depart, arrive in [list(map(int, input().split())) for _ in range(M)]}
from collections import deque 
queue = deque([[1, 0]])
ns = []
visited = set()
min_n = float("inf")
while queue:
    node, n = queue.popleft()
    if n >= min_n:
        continue
    if node >= 94:
        ns.append(n+1)
        if n+1 < min_n:
            min_n = n+1
        continue
    for i in range(1,7):
        next_node = node + i
        if next_node not in visited:
            if next_node in LADDERS:
                next_node = LADDERS[next_node]
            elif next_node in SNAKES:
                next_node = SNAKES[next_node]
            visited.add(next_node)
            queue.append([next_node, n+1])
print(min(ns))