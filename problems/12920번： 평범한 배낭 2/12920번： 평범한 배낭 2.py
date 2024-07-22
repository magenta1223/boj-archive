#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 12920                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/12920                         #+#        #+#      #+#     #
#     Solved: 2024-07-22 09:30:15 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 시간초과 예상
# S최댓값 1M x M최댓값 10K -> 10B 

# input = open(0).readline 
# N,M = map(int,input().split())
# S = 0 
# L = []
# V = []
# for i in range(N):
#     v,c,k = map(int,input().split())
#     L += [(i,c)] * k 
#     S += k 
#     V.append(v)
# dp = [0] * (M+1)
# for i in range(S):
#     idx, c = L[i]
#     for v in range(M, V[idx]-1,-1):
#         dp[v] = max(dp[v], dp[v-V[idx]]+c)
# print(max(dp))


input = open(0).readline 

N,M = map(int,input().split())
L = []

for i in range(N):
    v,c,k = map(int,input().split())
    bulk = 0 
    while k:
        x = min(1<<bulk, k)
        L.append((v*x, c*x))
        k -= x 
        bulk += 1 

S = len(L)
dp = [0] * (M+1)
for i in range(S):
    v, c = L[i]
    for nv in range(M, v-1,-1):
        dp[nv] = max(dp[nv], dp[nv-v]+c)
print(max(dp))