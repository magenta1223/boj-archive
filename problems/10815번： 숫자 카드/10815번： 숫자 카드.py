#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10815                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10815                         #+#        #+#      #+#     #
#     Solved: 2023-10-26 17:58:36 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline
n=int(input())
ns=set(map(int,input().split()))
m=int(input())
ms=list(map(int, input().split()))
print(*[1 if m in ns else 0 for m in ms])
 