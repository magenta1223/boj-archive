#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 28279                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/28279                         #+#        #+#      #+#     #
#     Solved: 2023-11-22 15:53:14 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input=sys.stdin.readline
from collections import deque
N=int(input())
q=deque([])
for _ in range(N):
    c= list(map(int, input().split()))
    if c[0]==1:
        q.appendleft(c[1])
    elif c[0]==2:
        q.append(c[1])
    elif c[0]==3:
        print(q.popleft() if q else -1)
    elif c[0]==4:
        print(q.pop() if q else -1) 
    elif c[0]==5:
        print(len(q))
    elif c[0]==6:
        print(1 if not q else 0)
    elif c[0]==7:
        print(q[0] if q else -1)
    else:
        print(q[-1] if q else -1)