#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1389                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1389                          #+#        #+#      #+#     #
#     Solved: 2024-03-04 22:51:37 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M = map(int, input().split())
W = [[float('inf')] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    W[a-1][b-1] = 1
    W[b-1][a-1] = 1
for i in range(N):
    W[i][i] = 0
 
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            W[i][j] = min(W[i][j], W[i][k] + W[k][j])
            
s = [sum(W[i]) for i in range(N)]
print(s.index(min(s)) + 1)