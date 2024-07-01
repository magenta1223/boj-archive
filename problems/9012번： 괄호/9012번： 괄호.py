#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 9012                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/9012                          #+#        #+#      #+#     #
#     Solved: 2023-11-22 13:31:50 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline
N=int(input())
# (가 나오면 +1 아니면 -1
# 값이 0이면 YES아니면 No
for _ in range(N):
    strs=input().strip()
    v=0
    for s in strs:
        if s == "(":
            v+=1
        else:
            v-=1
        if v<0:
            v -= 100
            break
    if v == 0:
        print("YES")
    else:
        print("NO")