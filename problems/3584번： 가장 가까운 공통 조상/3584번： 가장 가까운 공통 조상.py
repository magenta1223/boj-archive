#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 3584                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/3584                          #+#        #+#      #+#     #
#     Solved: 2024-02-29 18:27:33 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from math import sqrt
def nca(children, parents, a,b,n):    
    def prepare(n,p0,children):
        max_depth = max(int(sqrt(n)),2)
        parents = [[0] * max_depth for _ in range(n+1)]
        for i in range(1, n+1):
            parents[i][0] = p0[i]
            if not p0[i]:
                root= i 
        for depth in range(1, max_depth):
            for i in range(1,n+1):
                parents[i][depth] = parents[parents[i][depth-1]][depth-1]
        
        # level 
        nodes = [(root,0)]
        levels = [0] * (n+1)
        while nodes:
            node, level = nodes.pop()
            for child in children[node]:
                nodes.append((child, level+1))
                levels[child] = level + 1
        return parents, levels
    
    parents, levels = prepare(n, parents,children)
    max_depth = max(int(sqrt(n)),2)
    
    if levels[a] < levels[b]:
        a,b = b,a
        
    for i in range(max_depth-1, -1, -1):
        if levels[a] - levels[b] >= 2**i:
            a = parents[a][i] 
    if a == b:
        return a
            
    for i in range(max_depth-1, -1, -1):
        if parents[a][i] != parents[b][i]:
            a = parents[a][i] 
            b = parents[b][i] 
    
    return parents[a][0]
 
 
input = open(0).readline
 
T = int(input())
for _ in range(T):
    N = int(input())
    C = {i : [] for i in range(1,N+1)}
    P = [0] * (N+1)
    for _ in range(N-1):
        a,b=map(int,input().split())
        C[a].append(b)
        P[b] = a
    A,B = map(int,input().split())
    print(nca(C,P,A,B,N))