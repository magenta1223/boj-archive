#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1027                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1027                          #+#        #+#      #+#     #
#     Solved: 2024-07-16 06:40:56 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# ccw 

def crossProduct(x1,y1,x2,y2,x3,y3):
    v = (x2-x1)*(y3-y2) - (x3-x2)*(y2-y1)
    if v > 0:
        return 1 
    elif v < 0:
        return -1 
    else:
        return 0 

def ccw(x1,y1,x2,y2,x3,y3,x4,y4):

    _123 = crossProduct(x1,y1,x2,y2,x3,y3)
    _124 = crossProduct(x1,y1,x2,y2,x4,y4)
    _341 = crossProduct(x3,y3,x4,y4,x1,y1)
    _342 = crossProduct(x3,y3,x4,y4,x2,y2)

    mx1, mx2, mx3, mx4 = min(x1, x2), max(x1, x2), min(x3, x4), max(x3, x4)
    my1, my2, my3, my4 = min(y1, y2), max(y1, y2), min(y3, y4), max(y3, y4)
    
    # 접해도 만나는거임. 
    if _123*_124 < 0 and _341*_342 < 0:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            return True 
    if not _123*_124 or not _341*_342:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            return True 
    return False 


N = int(input())
A = list(map(int,input().split()))

def calc(idx):
    buildings = [(i,0,i,A[i]) for i in range(N)]
    x1, y1 = idx, A[idx]
    res = 0 
    for i in range(N):
        if i == idx:
            continue 
        x2, y2 = i, A[i]
        if abs(i-idx) == 1:
            res += 1 
            continue 
        for j in range( min(i,idx)+1, max(i,idx)):
            x3,y3,x4,y4 = buildings[j]
            if ccw(x1,y1,x2,y2,x3,y3,x4,y4):
                break 
        else:
            res += 1 
    return res 

print(max([calc(i) for i in range(N)]))
