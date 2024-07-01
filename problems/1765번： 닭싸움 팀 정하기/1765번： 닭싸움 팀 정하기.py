#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1765                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1765                          #+#        #+#      #+#     #
#     Solved: 2024-06-05 12:11:14 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline
 
def find(a):
    if a == parent[a]:
        return a 
    parent[a] = find(parent[a])
    return parent[a]
 
N=int(input())
M = int(input())
parent = [i for i in range(N+1)]
enemies = [[] for _ in range(N+1)]
for _ in range(M):
    x,p,q = input().split()
    p,q = int(p), int(q)
    if x == "F":
        p,q = find(p), find(q)
        if p != q:
            p,q = (p,q) if p>q else (q,p)
            parent[p] = q 
    else:
        enemies[p].append(q)
        enemies[q].append(p)
 
for i in range(1,N+1):
    for enemy in enemies[i]:
        for anti_enemy in enemies[enemy]:
            p,q = find(i), find(anti_enemy)
            if p != q:
                p,q = (p,q) if p>q else (q,p)
                parent[p] = q 
for i in range(1,N+1):
    find(i)
 
 
print(len(set(parent[1:])))