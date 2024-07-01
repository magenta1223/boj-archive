#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 13511                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/13511                         #+#        #+#      #+#     #
#     Solved: 2024-04-12 17:37:28 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
 
input = open(0).readline 
 
def init():
    parents = [[1] * K for _ in range(N+1)]
    costs = [[0] * K for _ in range(N+1)]
    q = deque([(1,1)])
    levels = [False] * (N+1)
    levels[1] = 1
    while q:
        x,l = q.popleft()
        for nx in G[x].keys():
            if levels[nx]: continue
            parents[nx][0] = x
            costs[nx][0] = G[x][nx]
            levels[nx] = l+1
            q.append((nx,l+1)) 
 
    for i in range(1,K):
        for x in range(1,N+1):
            parents[x][i] = parents[parents[x][i-1]][i-1]
            costs[x][i] = costs[x][i-1] + costs[parents[x][i-1]][i-1]
    return parents, levels, costs
 
 
def find_kth(x,k):
    for i in range(K-1, -1, -1):
        if not k:
            return x 
        pow2 = (1<<i)
        if pow2 <= k:
            x = P[x][i]
            k -= pow2 
    return x
 
def solve(q, a, b, k=None):
    if q == 1:
        cost = 0
        if L[a] > L[b]:
            a,b = b,a 
 
        for i in range(K-1, -1, -1):
            if L[b] - L[a] >= (1<<i):
                cost += C[b][i]
                b = P[b][i]
 
        if a == b:
            return cost
    
        for i in range(K-1, -1, -1):
            if P[a][i] != P[b][i]:
                cost += C[a][i] + C[b][i]
                a = P[a][i]
                b = P[b][i]
        return cost + C[a][i] + C[b][i]
 
    else:
        k -= 1 
        oa,ob,swap,path = a,b,False, [0,0]
        if L[a] > L[b]:
            a,b = b,a 
            swap = True 
 
        for i in range(K-1, -1, -1):
            if L[b] - L[a] >= (1<<i):
                path[1] += (1<<i)
                b = P[b][i]
        if a == b:
            if swap:
                return find_kth(oa, k)
            else:
                return find_kth(ob, sum(path)-k)
 
        for i in range(K-1, -1, -1):
            if P[a][i] != P[b][i]:
                len_path = (1<<i)
                path[0] += len_path
                path[1] += len_path
                a = P[a][i]
                b = P[b][i]
        
        path[0] += 1
        path[1] += 1 
        # k가 oa에서 lca에 이르는 거리보다 긴가?
        # swap시 oa = b이므로 1  
        if k > path[1 if swap else 0]:
            # k를 넘기면, sum(path) - k를 ob에서 거슬러 올라온 노드가 답
            return find_kth(ob, sum(path) - k)
        else:
            return find_kth(oa, k)
 
N = int(input())
K = 17 # n levels 
G = {i : {} for i in range(1,N+1)}
for _ in range(N-1):
    a,b,w = map(int,input().split())
    G[a][b] = w 
    G[b][a] = w 
 
P, L, C = init()
M = int(input())
for i in range(M):
    print(solve(*map(int,input().split())))