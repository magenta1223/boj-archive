#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1037                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1037                          #+#        #+#      #+#     #
#     Solved: 2023-11-22 17:03:07 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
l=list(map(int, input().split()))
print(min(l) * max(l))