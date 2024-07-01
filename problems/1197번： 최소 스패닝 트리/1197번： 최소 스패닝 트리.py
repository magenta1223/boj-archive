#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1197                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1197                          #+#        #+#      #+#     #
#     Solved: 2024-04-02 13:14:28 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline
V,E = map(int,input().split())
 
# 모든 정점을 연결하는 subgraph 중 가중치 합이 최소인 graph 
# 크루스칼 알고리즘
# 1. edge를 가중치 순으로 정렬
# 2. cycle을 형성하지 않는다면 -> edge를 선택
# 3. N-1개까지 
# cycle 형성 여부 판단 = union-find 
 
def find(a):
    if a == parent[a]:
        return a 
    parent[a] = find(parent[a])
    return parent[a]
 
def union(a, b):
    if a != b:
        parent[b] = parent[a]
 
edges = [list(map(int,input().split())) for _ in range(E)]
edges.sort(key = lambda x: x[-1])
parent = [i for i in range(V+1)]
 
ans = 0
 
for a,b,w in edges:
    # cycle을 형성하는지? 
    a, b = find(a), find(b)
    if a == b:
        continue
    else:
        ans += w 
        union(a,b)
 
print(ans)