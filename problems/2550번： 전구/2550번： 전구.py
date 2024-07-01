#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2550                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2550                          #+#        #+#      #+#     #
#     Solved: 2024-06-17 14:33:25 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
S=list(map(int,input().split()))
L=list(map(int,input().split()))
 
Ldict = dict()
for i in range(N):
    Ldict[L[i]] = i 
 
dp = [1] * N 
backtrack = [-1] * N 
 
for i in range(N):
    # 전구
    # l = L.index(S[i])
    l = Ldict[S[i]]
    # 직전 번호까지 연결 가능한지? 
    for j in range(i):
        if l > Ldict[S[j]]:
            if dp[j]+1 > dp[i]:
                dp[i] = dp[j]+1 
                backtrack[i] = j 
 
max_dp = max(dp)
 
node = dp.index(max_dp)
paths = [S[node]]
 
while backtrack[node] != -1:
    node = backtrack[node]
    paths.append(S[node])
 
 
print(max_dp)
print(*sorted(paths))