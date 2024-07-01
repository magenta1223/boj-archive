#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 4134                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/4134                          #+#        #+#      #+#     #
#     Solved: 2023-11-21 15:17:07 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import math 
import sys 
input = sys.stdin.readline
 
def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False 
    return True 
 
N=int(input())
for _ in range(N):
    n = int(input())
    while True:
        if n in [0, 1]:
            print(2)
            break 
        if isPrime(n):
            print(n)
            break 
        else:
            n += 1