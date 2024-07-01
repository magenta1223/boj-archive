#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 25192                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/25192                         #+#        #+#      #+#     #
#     Solved: 2023-11-22 17:09:59 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
input=sys.stdin.readline
N=int(input())
s=set()
c=0
for _ in range(N):
    msg=input().rstrip()
    if msg == "ENTER":
        c+=len(s)
        s=set()
    else:
        s.add(msg)
c+=len(s)
print(c)