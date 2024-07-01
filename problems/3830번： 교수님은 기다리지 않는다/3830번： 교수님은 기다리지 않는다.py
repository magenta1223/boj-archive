#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 3830                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/3830                          #+#        #+#      #+#     #
#     Solved: 2024-03-06 16:40:29 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
 
def find(a):
    if parent[a] != a:
        p, pcost = parent[a], parent_costs[a]
        parent[a] = find(p)    
        costs[a] += costs[p] - pcost 
        parent_costs[a] = costs[parent[a]]
    
    return parent[a]
 
def union(a,b,w):
    w = w - costs[b] + costs[a]
    a, b = find(a), find(b)
    costs[a] -= w 
    parent[a] = b
    parent_costs[a] = costs[b]
 
def answer(a,b):
    return "UNKNOWN" if find(a)!=find(b) else costs[b] - costs[a]
 
while True:
    N,M = map(int,input().split())
    if (N,M) == (0,0):
        break 
    parent = [i for i in range(N+1)]
    costs, parent_costs = [0] * (N+1), [0] * (N+1) 
 
    for _ in range(M):
        qa = list(input().split())
        if qa[0] == "!":
            a,b,w = map(int, qa[1:])
            if find(a) != find(b):
                union(a,b,w)            
        else:
            a,b = map(int, qa[1:])
            print(answer(a,b))