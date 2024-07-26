#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 13976                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/13976                         #+#        #+#      #+#     #
#     Solved: 2024-07-25 03:17:11 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

MOD = 1_000_000_007
def matmul(A,B):
    n,m,l = len(A), len(B), len(B[0])
    B = list(zip(*B))
    return  [[sum([A[i][k] * B[j][k] for k in range(m)])%MOD for j in range(l)] for i in range(n)]

N = int(input())

if N%2:
    print(0)
    exit(0)


A = [[3,1,2],[2,1,0],[0,0,1]]
N = str(int(bin(N//2-1)[2:]))
Matrices = []
L = len(N)
for i in range(L):
    Matrices.append(A)
    A = matmul(A,A)
    
M =[[1,0,0], [0,1,0], [0,0,1]]
for i in range(len(N)):
    if N[L-i-1] == "1":
        M = matmul(M, Matrices[i])
print(matmul(M, [[3],[0],[1]]) [0][0]%MOD)

