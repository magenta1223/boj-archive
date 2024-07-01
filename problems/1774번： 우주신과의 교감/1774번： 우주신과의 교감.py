#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1774                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1774                          #+#        #+#      #+#     #
#     Solved: 2024-04-02 14:02:14 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from math import sqrt 
 
input = open(0).readline
INF = float("inf")
 
def dist(x1,y1,x2,y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)
 
def find(a):
    if a == parent[a]:
        return a 
    parent[a] = find(parent[a])
    return parent[a]
 
def union(a, b):
    parent[b] = parent[a]
 
 
N, M = map(int,input().split())
D = [[INF] * (N) for _ in range(N)]
COORDS = [list(map(int,input().split())) for _ in range(N)]
for _ in range(M):
    a, b = map(int,input().split()) 
    D[a-1][b-1] = 0 
    D[b-1][a-1] = 0
 
for i in range(N):
    for j in range(i):
        if D[i][j]:
            D[i][j] = min(D[i][j], dist(*COORDS[i], *COORDS[j]))
 
parent = [i for i in range(N)]
edges = [ (i,j,D[i][j]) for i in range(N) for j in range(i)]
edges.sort(key = lambda x : x[-1])
 
ans = 0 
for a,b,w in edges:
    a,b = find(a), find(b)
    if a != b:
        union(a, b)
        ans += w
 
print(f"{ans:.2f}")