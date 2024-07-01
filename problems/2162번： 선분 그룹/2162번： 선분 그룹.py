#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2162                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2162                          #+#        #+#      #+#     #
#     Solved: 2024-04-09 14:59:40 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import Counter
 
def find(a):
    if parent[a] == a:
        return a 
    parent[a] = find(parent[a])
    return parent[a]
 
def _ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)
 
def ccw(x1, y1, x2, y2, x3, y3, x4, y4):
    mx1, my1, mx2, my2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
    mx3, my3, mx4, my4 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)
 
    ccw123 = _ccw(x1, y1, x2, y2, x3, y3)
    ccw124 = _ccw(x1, y1, x2, y2, x4, y4)
    ccw341 = _ccw(x3, y3, x4, y4, x1, y1)
    ccw342 = _ccw(x3, y3, x4, y4, x2, y2)
    # 두 선분이 일직선상에 위치 
    if ccw123*ccw124 == 0 and ccw341*ccw342 == 0:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            return 1
    # 교차 -> 반드시 만남 
    elif ccw123*ccw124 <= 0 and ccw341*ccw342 <= 0:
        return 1
    # 한 선분의 모든 점이 다른 선분의 한 쪽에 위치 
    return 0
 
N = int(input())
parent = [i for i in range(N)]
lines = [list(map(int,input().split())) for _ in range(N)]
 
for i in range(N):
    x1,y1,x2,y2 = lines[i]
    for j in range(i):
        x3,y3,x4,y4 = lines[j]
        if ccw(x1,y1,x2,y2,x3,y3,x4,y4):
            i, j = find(i), find(j)
            if i != j:
                parent[j] = parent[i]
for i in range(N):
    find(i)
 
print(len(set(parent)))
print(max(Counter(parent).values()))