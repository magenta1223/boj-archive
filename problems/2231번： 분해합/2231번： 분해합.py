#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2231                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2231                          #+#        #+#      #+#     #
#     Solved: 2023-10-26 16:07:18 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
isGen=False
for i in range(1, N):
    if i+ sum([int(n) for n in str(i)]) == N:
        isGen=True
        break
if isGen:
    print(i)
else:
    print(0)