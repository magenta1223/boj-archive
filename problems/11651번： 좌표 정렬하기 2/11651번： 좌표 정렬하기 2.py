#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11651                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11651                         #+#        #+#      #+#     #
#     Solved: 2023-10-26 17:18:03 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

for i in sorted([[*map(int,s.split())]for s in open(0)][1:], key=lambda x : (x[1], x[0])):print(*i)