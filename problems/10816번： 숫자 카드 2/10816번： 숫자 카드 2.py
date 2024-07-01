#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10816                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10816                         #+#        #+#      #+#     #
#     Solved: 2023-11-02 14:24:07 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
input = sys.stdin.readline
N = int(input())
di = {}
ns = list(map(int, input().split()))
for n in ns:
    if n not in di:
        di[n] = 1
    else:
        di[n] += 1
M = int(input())
ms = list(map(int, input().split()))
print(*[ di[m] if m in di else 0 for m in ms])