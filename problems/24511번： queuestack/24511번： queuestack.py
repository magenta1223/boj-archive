#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 24511                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/24511                         #+#        #+#      #+#     #
#     Solved: 2023-11-22 16:32:51 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
input=sys.stdin.readline
from collections import deque
N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
M=int(input())
C=list(map(int, input().split()))
q=deque()
for i in range(N):
    if not A[i]:
        q.append(B[i])
results=[]
for c in C:
    q.appendleft(c)
    results.append(q.pop())
print(*results, sep=" ")