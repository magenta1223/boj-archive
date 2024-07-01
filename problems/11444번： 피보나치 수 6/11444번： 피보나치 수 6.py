#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11444                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11444                         #+#        #+#      #+#     #
#     Solved: 2023-12-22 12:18:01 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

MOD = 1000000007
 
def matmul(A, B):
    return [[sum(x * y for x, y in zip(row, col)) % MOD for col in zip(*B)] for row in A]
 
def matpow(A, n):
    result = [[1, 0], [0, 1]]  # 단위 행렬
    while n > 0:
        if n % 2 == 1:
            result = matmul(result, A)
        A = matmul(A, A)
        n //= 2
    return result
 
def fibonacci(n):
    if n == 0:
        return 0
    F = [[1, 1], [1, 0]]
    return matpow(F, n - 1)[0][0]
 
n = int(input())
print(fibonacci(n))
 