#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2581                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2581                          #+#        #+#      #+#     #
#     Solved: 2023-10-26 14:14:26 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

M = int(input())
N = int(input())
primes = []
for i in range(M, N+1):
    isPrime = True
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break 
        if isPrime:
            primes.append(i)
if len(primes) > 0:
    print(sum(primes))
    print(primes[0])
else:
    print(-1)