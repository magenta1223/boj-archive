#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10773                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10773                         #+#        #+#      #+#     #
#     Solved: 2023-11-22 13:22:09 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
input = sys.stdin.readline
K=int(input())
l=[]
for _ in range(K):
    n=int(input())
    if n==0:
        l.pop()
    else:
        l.append(n)
print(sum(l))