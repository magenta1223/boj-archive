#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1929                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1929                          #+#        #+#      #+#     #
#     Solved: 2023-11-21 15:26:30 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import math 
M,N=map(int, input().split())
def isPrime(n):
    if n == 1:
        return False 
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False 
    return True 
for i in range(M, N+1):
    if isPrime(i):
        print(i)