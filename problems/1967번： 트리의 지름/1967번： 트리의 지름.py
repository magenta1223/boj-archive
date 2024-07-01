#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1967                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1967                          #+#        #+#      #+#     #
#     Solved: 2024-03-30 00:32:03 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
sys.setrecursionlimit(10**4) 
 
def dfs(node, weight):
    for next_node, next_weight in graph[node]:
        if distances[next_node] == -1: # 아직 방문하지 않은 노드인 경우
            distances[next_node] = weight + next_weight
            dfs(next_node, weight + next_weight)
 
N = int(input())
graph = [[] for _ in range(N+1)]
 
# 트리 구성
for _ in range(N-1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))
 
distances = [-1] * (N+1)
distances[1] = 0
dfs(1, 0)
farthest_node = distances.index(max(distances))
 
distances = [-1] * (N+1)
distances[farthest_node] = 0
dfs(farthest_node, 0)
 
print(max(distances)) # 트리의 지름 출력