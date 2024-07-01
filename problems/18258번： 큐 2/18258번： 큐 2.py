#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 18258                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/18258                         #+#        #+#      #+#     #
#     Solved: 2023-11-22 14:11:47 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
q=deque([])
for _ in range(N):
    c=input().strip()
    if len(c.split())>1:
        c,n=c.split()
        n=int(n)
    if c=="push":
        q.append(n)
    elif c=="pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif c=="size":
        print(len(q))
    elif c=="empty":
        print(int(len(q)==0))
    elif c=="front":
        print(q[0] if q else -1)
    else:
        print(q[-1] if q else -1)