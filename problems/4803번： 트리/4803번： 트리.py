#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 4803                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/4803                          #+#        #+#      #+#     #
#     Solved: 2024-06-12 14:23:08 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

 
def dfs(prev, now):
    for next in G[now]:
        if next == prev:
            continue 
        if visited[next]:
            return True 
        visited[next] = True 
        if dfs(now, next):
            return True 
    return False 
 
input = open(0).readline 
case = 0 
while True:
    case += 1 
    N, M = map(int, input().split())
    
    if N==M==0:
        break
 
    G = {i: [] for i in range(1, N+1)}
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    
    visited, count = [False]*(N+1), 0
    for node in range(1, N+1):
        if visited[node]:
            continue 
        visited[node] = True 
        if not dfs(-1, node):
            count += 1
    if count == 0:
        res = f'No trees.'
    elif count == 1:
        res = 'There is one tree.'
    else:
        res = f'A forest of {count} trees.'
    print(f'Case {case}: {res}') 
 