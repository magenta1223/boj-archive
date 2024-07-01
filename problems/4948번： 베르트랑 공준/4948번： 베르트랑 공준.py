#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 4948                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/4948                          #+#        #+#      #+#     #
#     Solved: 2023-11-21 15:44:18 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import math
import sys 
input = sys.stdin.readline
def isPrime(n):
    if n == 1:
        return 0 
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return 0
    return 1 
 
m=123456
l=[isPrime(i) for i in range(1, 2*m+1)]
while True:
    n=int(input())
    if n==0:
        break
    print(sum([l[i-1] for i in range(n+1,2*n+1)]))
 