#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2887                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2887                          #+#        #+#      #+#     #
#     Solved: 2024-04-02 15:31:09 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 
 
def find(a):
    if a == parent[a]:
        return a 
    parent[a] = find(parent[a])
    return parent[a]
 
N = int(input())
xs, ys, zs = [], [], []
for i in range(N):
    x, y, z = map(int, input().split())
    xs.append((x,i))
    ys.append((y,i))
    zs.append((z,i))
xs.sort()
ys.sort()
zs.sort()
 
edges = []
for s in [xs, ys, zs]:
    for i in range(N-1):
        xa, a = s[i]
        xb, b = s[i+1]
        edges.append((abs(xa-xb), a, b))
 
edges.sort(key = lambda x: x[0])
 
ans = 0
parent = [i for i in range(N)]
for w,a,b in edges:
    a, b = find(a), find(b)
    if a != b:
        parent[b] = parent[a]
        ans += w 
 
print(ans)