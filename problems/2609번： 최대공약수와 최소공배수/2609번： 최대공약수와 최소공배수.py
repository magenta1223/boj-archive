#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2609                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2609                          #+#        #+#      #+#     #
#     Solved: 2024-04-04 14:23:41 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from math import gcd, lcm
A,B=map(int,input().split())
print(gcd(A,B))
print(lcm(A,B))