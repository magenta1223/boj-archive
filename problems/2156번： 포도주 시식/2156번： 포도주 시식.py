#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2156                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2156                          #+#        #+#      #+#     #
#     Solved: 2023-12-19 16:44:06 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
l = [int(input()) for _ in range(N)]
cum_l = [0 for _ in l]
cum_l[0] = l[0]
if N>1:
    cum_l[1] = l[0] + l[1]
for i in range(2, N):
    cum_l[i] = max(cum_l[i-2]+l[i], cum_l[i-3] + l[i-1] + l[i], cum_l[i-1])
print(cum_l[-1])