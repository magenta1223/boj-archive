#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2740                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2740                          #+#        #+#      #+#     #
#     Solved: 2023-12-21 21:37:53 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]
 
# B 행렬을 전치합니다.
B_T = [[B[k][j] for k in range(M)] for j in range(K)]
 
# 행렬 곱셈을 수행합니다.
for i in range(N):
    print(*[sum(a * b for a, b in zip(A[i], B_T[j])) for j in range(K)])
 