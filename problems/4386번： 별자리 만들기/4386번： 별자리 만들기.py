#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 4386                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/4386                          #+#        #+#      #+#     #
#     Solved: 2024-03-12 18:23:26 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from heapq import heappop, heapify
from math import sqrt
 
def dist(s1, s2):
    return sqrt(pow(s1[0]-s2[0], 2) + pow(s1[1]-s2[1], 2))
 
def find(a):
    if parent[a] == a:
        return a 
    parent[a] = find(parent[a])
    return parent[a]
 
def union(a,b):
    a,b = find(a), find(b)
    a,b = (a,b) if a<b else (b,a)
    parent[b] = a 
 
N=int(input())
S = [list(map(float, input().split())) for _ in range(N)]
parent = [i for i in range(N)]
heap = [(dist(S[i], S[j]), i,j) for i in range(N) for j in range(N)]
heapify(heap)
ans = 0
connected = 1
while heap and connected < N:
    w,i,j = heappop(heap)
    # 조상이 같으면 연결하면 안됨. cycle 생성 
    if find(i) == find(j): 
        continue
    else:
        connected += 1 
        ans += w 
        union(i,j)
print(int(ans * 100) / 100)