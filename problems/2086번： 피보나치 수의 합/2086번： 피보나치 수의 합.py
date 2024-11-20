#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2086                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2086                          #+#        #+#      #+#     #
#     Solved: 2024-11-20 01:02:49 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 피보나치 수열의 a항부터 b항까지의 합 % MOD를 구하기 

"""
피보나치 수열의 a항부터 b항까지의 합 % MOD를 구하기 
어.. 일일히 할 수는 없고 

피보나치 수식 전개하면 sum(fib[a:b+1]) = fib(b+2)-fib(a+1)

"""

def matmul(a,b):
    n,m,r = len(a), len(b), len(b[0])
    bt = list(zip(*b))
    mat = [[ sum([a[i][k]*bt[j][k] for k in range(m)]) % MOD  for j in range(r)] for i in range(n)]
    return mat

def get_n_fib(n):
    bin_n = bin(n)[2:][::-1]
    mat = [[1,1]]
    for i in range(len(bin_n)):
        if bin_n[i] == '1':
            mat = matmul(fib_arrs[i], mat)
    return mat[0][0]


MOD = 1_000_000_000 
MAX = 9_000_000_000_000_000_000
a,b = map(int,input().split())

A = [[1,1],[1,0]]
fib_arrs, x = [A], 1
while x <= MAX:
    x *= 2 
    fib_arrs.append(matmul(fib_arrs[-1], fib_arrs[-1]))

# a와 b를 이진수로 만들고, 1이 있으면 그 해당 인덱스의 fibarr을 곱한다. 
print((get_n_fib(b+1) - get_n_fib(a))%MOD)
