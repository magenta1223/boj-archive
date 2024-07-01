#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11659                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11659                         #+#        #+#      #+#     #
#     Solved: 2023-12-20 14:56:20 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
input = sys.stdin.readline
N,M=map(int, input().split())
l=list(map(int, input().split()))
cummulative = [0]*(N+1)
for i in range(N):
    cummulative[i+1] = cummulative[i] + l[i]    
for _ in range(M):
    i,j=map(int, input().split())
    print(cummulative[j] - cummulative[i-1])