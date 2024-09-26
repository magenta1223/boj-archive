#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2610                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2610                          #+#        #+#      #+#     #
#     Solved: 2024-09-26 05:04:13 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 1. union-find로 위원회의 갯수와 각 위원회에 속한 사람을 찾고
# 2. dijkstra로 최단 의사전달시간을 갖는 대표자를 찾기 
# N은 100이하이므로 충분히 가능 

from heapq import heappop, heappush 
input = open(0).readline 

def find(a):
    if a==parent[a]:
        return a 
    parent[a] = find(parent[a])
    return parent[a]

def get_groups(parent):
    _groups = list(set(parent[1:]))
    n_groups = len(_groups)
    groups = [[] for _ in range(n_groups)] 
    for i in range(1,N+1):
        groups[_groups.index(parent[i])].append(i)
    return n_groups, groups

def dijkstra(start, group):
    q = [(0, start)]
    cost = [INF] * (N+1)  
    cost[start] = 0 
    while q:
        cur_cost, cur = heappop(q)
        for next in G[cur]:
            if cost[next] > cur_cost+1:
                cost[next] = cur_cost+1 
                heappush(q, (cur_cost+1, next))
    # group 내의 모든 곳에 도달하는 시간의 최댓값  
    return max([cost[g] for g in group])

INF = float("inf")
N = int(input())
M = int(input())
parent = [i for i in range(N+1)]
G = {i : [] for i in range(1,N+1)}
for _ in range(M):
    a,b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)  
    a,b = find(a), find(b)
    if a!=b:
        a,b = (b,a) if a>b else (a,b)
        parent[b] = a
for i in range(1, N+1):
    parent[i] = find(i)
n_groups, groups = get_groups(parent)
print(n_groups)
print(*sorted([sorted([(dijkstra(start, group), start)  for start in group])[0][1] for group in groups]), sep = '\n')

 
        