#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2485                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2485                          #+#        #+#      #+#     #
#     Solved: 2023-11-02 16:15:36 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import math
N = int(input())
li = [ int(input()) for _ in range(N)]
gcd = math.gcd(*[li[i+1]-li[i] for i in range(N-1)])
print( (li[-1] - li[0]) // gcd - len(li) + 1  )