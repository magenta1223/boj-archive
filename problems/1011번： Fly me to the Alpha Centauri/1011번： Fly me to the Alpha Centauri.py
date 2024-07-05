#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1011                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1011                          #+#        #+#      #+#     #
#     Solved: 2024-07-01 11:39:43 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from math import sqrt 
 
T = int(input())
INF = float("inf")
 
 
for _ in range(T):
    x,y = map(int,input().split())
    x,y = 0,y-x
 
    n = int(sqrt(y))
    ans = 2*n-1
    y -= n**2 
    for i in range(n,0,-1):
        if not y:
            break 
        if y >= i:
            move, y = divmod(y, i)
            ans += move 
    print(ans)