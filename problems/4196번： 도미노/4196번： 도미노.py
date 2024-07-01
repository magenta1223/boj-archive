#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 4196                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/4196                          #+#        #+#      #+#     #
#     Solved: 2024-04-16 16:53:57 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
sys.setrecursionlimit(10**5)
input = open(0).readline 
 
# 정방향 dfs, dfs 가 종료되는 노드를 stack에.
def dfs(node):
    visit[node] = 1
    for now in G[node]:
        if visit[now] == 0:
            dfs(now)
    stack.append(node)
 
# 역방향 dfs, 탐색하는 순서대로 stack에.
def reverse_dfs(node):
    visit[node] = 1
    ids[node] = idx
    scc.append(node)
    for now in RG[node]:
        if visit[now] == 0:
            reverse_dfs(now)
 
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    RG = [[] for _ in range(N + 1)]
 
    for _ in range(M):
        x, y = map(int, input().split())
        G[x].append(y)
        RG[y].append(x)
 
    stack, visit = [], [0]*(N+1)
    # forward dfs 
    for i in range(1, N+1):
        if visit[i] == 0:
            dfs(i)
 
    idx, ids, visit, result = 0, [-1]*(N+1), [0]*(N+1), []
    while stack:
        # pop되는 요소에서 역방향 dfs, scc를 결과에.
        scc = []
        node = stack.pop()
        if visit[node] == 0:
            idx += 1
            reverse_dfs(node)
            result.append(sorted(scc))
 
    scc_indegree = [0] * (idx + 1)
 
    for x in range(1, N + 1):
        for nx in G[x]:
            if ids[x] != ids[nx]:
                scc_indegree[ids[nx]] += 1
    cnt = 0
    for x in range(1, len(scc_indegree)):
        if scc_indegree[x] == 0:
            cnt += 1
    print(cnt)
 