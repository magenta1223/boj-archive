#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11779                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11779                         #+#        #+#      #+#     #
#     Solved: 2024-02-07 13:45:44 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from heapq import heappop, heappush
N=int(input().strip())
M=int(input().strip())
G = { i : []  for i in range(1, N+1)}
for _ in range(M):
    d,a,c = map(int, input().split())
    G[d].append((a,c))
A,B = map(int, input().split())
dp = [ float('inf') for _ in range(N+1)]
dp[A] = 0
heap = [(0,A)]
history = [ -1 for _ in range(N+1)]
while heap:
    cur_cost, cur_node =  heappop(heap)
    # 여기서 커트
    if dp[cur_node] < cur_cost:
        continue
    for next_node, next_cost in G[cur_node]:
        if dp[next_node] > cur_cost + next_cost:
            dp[next_node] = cur_cost + next_cost
            heappush(heap, (dp[next_node], next_node))
            history[next_node] = cur_node
path = []        
node = B
while node != -1:
    path.append(node)
    node = history[node]
path.reverse()            
print(dp[B])
print(len(path))
print(*path)