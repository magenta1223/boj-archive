#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17386                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17386                         #+#        #+#      #+#     #
#     Solved: 2024-05-21 18:18:57 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def ccw(x1,y1,x2,y2,x3,y3):
    return (x1-x2)*(y2-y3) - (x2-x3)*(y1-y2)
 
def crossed(x1,y1,x2,y2,x3,y3,x4,y4):
    ccw123 = ccw(x1,y1,x2,y2,x3,y3)
    ccw124 = ccw(x1,y1,x2,y2,x4,y4)
    ccw341 = ccw(x3,y3,x4,y4,x1,y1)
    ccw342 = ccw(x3,y3,x4,y4,x2,y2)
    mx1,mx2,mx3,mx4 = min(x1,x2), max(x1,x2), min(x3,x4), max(x3,x4)
    my1,my2,my3,my4 = min(y1,y2), max(y1,y2), min(y3,y4), max(y3,y4)
    if ccw123 * ccw124 < 0 and ccw341 * ccw342 < 0:
        if mx3 <= mx2 and mx4 >= mx1 and my3 <= my2 and my4 >= my1:
            return 1
    # 닿는것도 포함 
    elif not ccw123 or not ccw124 or not ccw341 or not ccw342:
        if mx3 <= mx2 and mx4 >= mx1 and my3 <= my2 and my4 >= my1:
            return 1
    return 0 
 
x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())
print(crossed(x1,y1,x2,y2,x3,y3,x4,y4))