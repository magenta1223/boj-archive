#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 20303                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/20303                         #+#        #+#      #+#     #
#     Solved: 2024-04-11 14:11:27 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def find(a):
    if parent[a] == a:
        return a 
    parent[a] = find(parent[a])
    return parent[a]
 
input = open(0).readline 
 
N,M,K = map(int,input().split())
parent = [i for i in range(N+1)]
C = list(map(int,input().split()))
for _ in range(M):
    a,b = map(int,input().split())
    a, b = find(a), find(b)
    a, b = (a,b) if a<b else (b,a)
    if a!=b:
        parent[b] = parent[a]
 
for i in range(1,N+1):
    find(i)
 
groups = {k : [0,0] for k in set(parent[1:])}
for i in range(1,N+1):
    groups[parent[i]][0] += 1
    groups[parent[i]][1] += C[i-1]
 
dp = [0] * K
for n, candy in groups.values():
    for k in range(K-1,-1,-1):
        if k < n: # 
            continue
        dp[k] = max(dp[k-n]+candy, dp[k])
print(max(dp))