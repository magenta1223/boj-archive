#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 6497                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/6497                          #+#        #+#      #+#     #
#     Solved: 2024-06-12 15:16:14 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
sys.setrecursionlimit(3*10**5)
 
def find(a):
    if a == parent[a]:
        return a 
    parent[a] = find(parent[a])
    return parent[a]
 
while True:
    N,M = map(int,input().split())
    if N==M==0:
        break
    edges, full = [], 0
    for _ in range(M):
        x,y,z = map(int,input().split())
        edges.append((z,x,y))
        full += z 
    edges.sort(key= lambda x: x[0])
 
    ans = 0 
    parent = [i for i in range(N)]
    for i in range(M):
        z,x,y = edges[i]
        x,y = find(x), find(y)
        if x!=y:
            ans += z 
            parent[x] = y 
 
    for i in range(N):
        find(i)
 
    print(full-ans)