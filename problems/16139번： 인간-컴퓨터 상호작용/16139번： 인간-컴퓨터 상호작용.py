#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 16139                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/16139                         #+#        #+#      #+#     #
#     Solved: 2023-12-20 15:44:11 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
from string import ascii_lowercase
input = sys.stdin.readline
S=input()
q=int(input())
cdict = { a : [0] * (len(S)+1) for a in ascii_lowercase}
for i in range(len(S)):
    for k, v in cdict.items():
        if k == S[i]:
            cdict[k][i+1] = cdict[k][i] + 1
        else:
            cdict[k][i+1] = cdict[k][i]
            
for _ in range(q):
    a,l,r = input().split()
    l,r = int(l), int(r)
    print(cdict[a][r+1] - cdict[a][l])