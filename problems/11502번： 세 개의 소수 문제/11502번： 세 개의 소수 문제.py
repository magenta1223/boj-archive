#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11502                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11502                         #+#        #+#      #+#     #
#     Solved: 2024-05-02 19:20:46 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

primes = [True] * 1001  
for i in range(2,1000):
    if not primes[i]:
        continue 
    for j in range(2, 1000 // i + 1):
        primes[i*j] = False 
 
primes = [i for i in range(2,1001) if primes[i]]
n_primes = len(primes)
 
def func(p):
    k = K-p 
    for i in range(n_primes):
        for j in range(i, n_primes):
            if k == primes[i] + primes[j]:
                return p, primes[i], primes[j]
    return None
 
input = open(0).readline
for _ in range(int(input())):
    K = int(input())
    done = False 
    for p in primes:
        if p > K:
            break 
        res = func(p)
        if res is not None:
            done = True
            break 
    
    if done:
        print(*res)
    else:
        print(0)
 