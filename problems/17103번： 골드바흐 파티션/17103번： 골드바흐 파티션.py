#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17103                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17103                         #+#        #+#      #+#     #
#     Solved: 2023-11-21 17:37:05 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
import math
input = sys.stdin.readline
l = [True for _ in range(1000001)]
for i in range(2,1001):
    if l[i]:
        for j in range(i + i , 1000001, i):
            l[j] = False
n=int(input())
for _ in range(n):
    N=int(input())
    c=0
    for i in range(2, N // 2 + 1):
        if l[i] and l[N-i]:
            c+=1
    print(c)
    