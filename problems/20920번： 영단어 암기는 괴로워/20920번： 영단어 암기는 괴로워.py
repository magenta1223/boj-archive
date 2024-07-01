#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 20920                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/20920                         #+#        #+#      #+#     #
#     Solved: 2023-11-22 17:49:22 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import Counter
import sys
input=sys.stdin.readline
N,M=map(int, input().split())
l=[]
for _ in range(N):
    w=input().rstrip()
    if len(w) >= M:
        l.append(w)
c=Counter(l)
x=sorted([ (k,v) for k, v in c.items()], key=lambda x:(-x[1], -len(x[0]),x[0]), reverse=True)
for xx in x[::-1]:
    print(xx[0])