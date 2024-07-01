#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1030                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1030                          #+#        #+#      #+#     #
#     Solved: 2024-05-27 15:39:14 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

s,N,K,R1,R2,C1,C2=map(int,input().split())
def dfs(x,y,size):
    if size == 1:
        return 0
    nsize = size // N 
    left, right = nsize*(N-K)//2, nsize*(N+K)//2
    if left<=x<right and left<=y<right:
        return 1 
    nx = x%nsize 
    ny = y%nsize
    return dfs(nx,ny,nsize)
 
arr = [[0] * (C2-C1+1) for _ in range(R2-R1+1)]
S = N**s
for i in range(R1, R2+1):
    for j in range(C1,C2+1):
        x,y = i,j 
        arr[x-R1][y-C1] = dfs(x,y,S)        
 
for line in arr:
    print("".join([str(num) for num in line]))