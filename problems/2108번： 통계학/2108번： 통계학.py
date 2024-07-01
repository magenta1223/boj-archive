#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2108                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2108                          #+#        #+#      #+#     #
#     Solved: 2023-11-22 17:38:08 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import Counter
import sys
input=sys.stdin.readline
N=int(input())
l=sorted([int(input())  for _ in range(N)])
c=[(k,v)  for k, v in Counter(l).items()]
print(round(sum(l)/len(l)))
print(l[N//2])
 
s=sorted(c, key=lambda x:x[1])
ms=[]
mode_v=s[-1][1]
for m in s[::-1]:
    if m[1] < mode_v:
        break
    else:
        ms.append(m[0])
if len(ms) > 1:
    mode=sorted(ms)[1]
else:
    mode=ms[0]
print(mode)
print(max(l) - min(l))