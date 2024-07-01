#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17435                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17435                         #+#        #+#      #+#     #
#     Solved: 2024-04-16 13:05:20 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline
 
def nth_parent(n, x):
    for i in range(K-1,-1,-1):
        powi = (1<<i)
        if n <= 1:
            break 
        if n >= powi:
            n -= powi
            x = parents[x][i]
    print(parents[x][0] if n else x)
 
M,K = int(input()), 19
F = [0] + list(map(int,input().split()))
parents = [[0] * K for _ in range(M+1)] # log2(200000) = 17.6 -> 2**18번째 조상까지 필요 
for i in range(M+1):
    parents[i][0] = F[i] 
for d in range(1,K):
    for i in range(1,M+1):
        parents[i][d] = parents[parents[i][d-1]][d-1]
    
Q = int(input())
for _ in range(Q):
    nth_parent(*map(int,input().split()))