#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2751                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2751                          #+#        #+#      #+#     #
#     Solved: 2023-10-26 16:52:40 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input=sys.stdin.readline
 
N=int(input())
li=[]
for i in range(N):
    li.append(int(input()))
for s in sorted(li):
    print(s)