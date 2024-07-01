#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 20149                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/20149                         #+#        #+#      #+#     #
#     Solved: 2024-05-21 18:55:40 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def ccw(x1,y1,x2,y2,x3,y3,x4,y4):
    def cross_product(x1,y1,x2,y2,x3,y3):
        v = (x1-x2)*(y2-y3) - (x2-x3)*(y1-y2)
        return v
    ccw123 = cross_product(x1,y1,x2,y2,x3,y3)
    ccw124 = cross_product(x1,y1,x2,y2,x4,y4)
    ccw341 = cross_product(x3,y3,x4,y4,x1,y1)
    ccw342 = cross_product(x3,y3,x4,y4,x2,y2)
 
    mx1,mx2,mx3,mx4 = min(x1,x2), max(x1,x2), min(x3,x4), max(x3,x4)
    my1,my2,my3,my4 = min(y1,y2), max(y1,y2), min(y3,y4), max(y3,y4)
 
    if ccw123*ccw124 < 0 and ccw341*ccw342 < 0:
        if mx3<=mx2 and mx1<=mx4 and my3<=my2 and my1<=my4:
            return 1  
    elif not ccw123 and mx1<=x3<=mx2 and my1<=y3<=my2:
        return 1 
    elif not ccw124 and mx1<=x4<=mx2 and my1<=y4<=my2:
        return 1 
    elif not ccw341 and mx3<=x1<=mx4 and my3<=y1<=my4:
        return 1 
    elif not ccw342 and mx3<=x2<=mx4 and my3<=y2<=my4:
        return 1 
    return 0 
 
def calc(x1,y1,x2,y2):
    if x2 == x1:
        return 1,0,x1 
    a = (y2-y1)/(x2-x1) 
    b = y1-a*x1
    return a,-1,-b 
 
def cross(x1,y1,x2,y2,x3,y3,x4,y4):
    a,b,k1 = calc(x1,y1,x2,y2)
    c,d,k2 = calc(x3,y3,x4,y4)
    det = a*d-b*c 
    if not det: # 평행 
        # 한점교차만 판단하면 됨. 
        A,B,C,D = (x1,y1), (x2,y2), (x3,y3), (x4,y4)
        A,B = sorted([A,B])
        C,D = sorted([C,D])
        if A==C and (B<=A<=D or D<=A<=B):
            return A 
        elif A==D and (B<=A<=C or C<=A<=B):
            return A
        elif B==C and (A<=B<=D or D<=B<=A):
            return B 
        elif B==D and (A<=B<=C or C<=B<=A):
            return B 
        else:
            return None 
        
    return (d*k1-b*k2) / det, (-c*k1+a*k2) / det 
 
L1 = list(map(int,input().split()))
L2 = list(map(int,input().split()))
 
 
if ccw(*L1, *L2):
    print(1)
    crossing_pt = cross(*L1, *L2)
    if crossing_pt is not None:
        print(*crossing_pt)
 
else:
    print(0)