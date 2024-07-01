#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17412                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17412                         #+#        #+#      #+#     #
#     Solved: 2024-06-05 11:28:53 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
input = open(0).readline
 
N, P = map(int, input().split())
G = [[] for _ in range(N+1)]
 
# capacity, flow
capacity = [[0] * (N+1) for _ in range(N+1)]
flow = [[0] * (N+1) for _ in range(N+1)]
 
# graph update u -> v
for _ in range(P):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u) 
    capacity[u][v] = 1
 
 
def bfs_path(source, sink, visited): 
    q = deque()
    q.append(source)
    while q and visited[sink] == -1: 
        now = q.popleft()
        for next in G[now]: 
            leftover_flow = capacity[now][next] - flow[now][next]
            if visited[next] == -1 and leftover_flow > 0: 
                q.append(next)
                visited[next] = now 
                if next == sink: 
                    break
 
    if visited[sink] == -1: 
        return False
    
    return True
 
def edmonds_karp(source, sink):
    ans = 0
    while True:
        visited = [-1] * (N+1)
        if not bfs_path(source, sink, visited): # path 가 없다면 업데이트 종료
            break
     
        now = sink
        while now != source:
            prev = visited[now]
            flow[prev][now] += 1
            flow[now][prev] -= 1
            now = prev 
 
        ans += 1
    return ans
 
 
print(edmonds_karp(1,2))