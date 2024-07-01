#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 24416                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/24416                         #+#        #+#      #+#     #
#     Solved: 2023-12-18 20:18:57 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
f = [0 for i in range(N)]
recOps = 0
dpOps=0
def fib(n):
    if n == 1 or n == 2:
        global recOps
        recOps += 1
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))
def fibonacci(n):
    global f, dpOps
    f[0] = f[1] = 1
    for i in range(2, N):
        f[i] = f[i-1] + f[i-2]
        dpOps += 1
    return f[n-1]
fib(N)
fibonacci(N)
print(recOps, dpOps)