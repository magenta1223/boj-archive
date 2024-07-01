#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2579                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2579                          #+#        #+#      #+#     #
#     Solved: 2023-12-18 23:20:23 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
stairs = [int(input()) for _ in range(N)]
 
if N==1:
    print(stairs[-1])
elif N==2:
    print(sum(stairs))
else:
    sum_stairs = [s for s in stairs]
    sum_stairs[1] = stairs[0] + stairs[1] 
    sum_stairs[2] = max(stairs[0], stairs[1]) + stairs[2]
    for i in range(3, N):
        sum_stairs[i] = max(sum_stairs[i-3] + stairs[i-1] + stairs[i], sum_stairs[i-2] + stairs[i])
    print(sum_stairs[-1])