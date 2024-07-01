#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10989                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10989                         #+#        #+#      #+#     #
#     Solved: 2023-10-26 16:58:41 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input=sys.stdin.readline
N=int(input())
di= {}
for i in range(N):
    v = int(input())
    if v in di:
        di[v] += 1
    else:
        di[v] = 1
keys = sorted(di.keys())
for k in keys:
    for _ in range(di[k]):
        print(k)