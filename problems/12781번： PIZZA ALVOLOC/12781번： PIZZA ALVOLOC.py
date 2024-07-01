#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 12781                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/12781                         #+#        #+#      #+#     #
#     Solved: 2024-04-12 13:30:58 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def _ccw(x1,y1,x2,y2,x3,y3):
    return (x1-x2)*(y2-y3) - (x2-x3)*(y1-y2)
 
x1,y1,x2,y2,x3,y3,x4,y4 = map(int,input().split())
 
ccw123 = _ccw(x1,y1,x2,y2,x3,y3)
ccw124 = _ccw(x1,y1,x2,y2,x4,y4)
ccw341 = _ccw(x3,y3,x4,y4,x1,y1)
ccw342 = _ccw(x3,y3,x4,y4,x2,y2)
mx1,mx2,mx3,mx4 = min(x1,x2), max(x1,x2), min(x3,x4), max(x3,x4)
my1,my2,my3,my4 = min(y1,y2), max(y1,y2), min(y3,y4), max(y3,y4)
if ccw123 * ccw124 < 0 and ccw341 * ccw342 < 0:
    if mx3 <= mx2 and mx4 >= mx1 and my3 <= my2 and my4 >= my1:
        print(1)
        exit(0)
print(0)