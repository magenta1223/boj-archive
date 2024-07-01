#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10830                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10830                         #+#        #+#      #+#     #
#     Solved: 2023-12-21 22:27:20 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

MOD=1000
N,B=map(int, input().split())
A=[list(map(int, input().split())) for _ in range(N)]
A_copy=[[1 if i==j else 0 for j in range(N)] for i in range(N)]
 
def matmul(matA, matB):
    matC = [[] for _ in range(N)]
    for i in range(N):
        matC[i] = [(sum([matA[i][k] * matB[k][j] for k in range(N)])) % MOD for j in range(N)]
    return matC
 
binary_B= bin(B)[2:][::-1]
for i, v in enumerate(binary_B):
    if v == "1":
        A_copy = matmul(A_copy, A)
    A = matmul(A, A)
for a in A_copy:
    print(*a)