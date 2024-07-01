#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1735                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1735                          #+#        #+#      #+#     #
#     Solved: 2023-11-02 15:39:53 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import math 
a, b = map(int, input().split())
c, d = map(int, input().split())
e=a*d+c*b
f=b*d
gcd=math.gcd(e, f)
print(e//gcd, f//gcd)