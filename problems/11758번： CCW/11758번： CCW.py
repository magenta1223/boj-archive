#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11758                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11758                         #+#        #+#      #+#     #
#     Solved: 2024-04-12 13:19:38 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
ccw = (x1-x2)*(y2-y3) - (x2-x3)*(y1-y2)
if ccw < 0:
    print(-1)
elif ccw > 0:
    print(1)
else:
    print(0)