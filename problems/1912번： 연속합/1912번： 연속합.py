#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1912                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1912                          #+#        #+#      #+#     #
#     Solved: 2023-12-18 22:23:46 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
l = list(map(int, input().split()))
for i in range(1, N):
    l[i] = max(l[i], l[i-1] + l[i])
print(max(l))