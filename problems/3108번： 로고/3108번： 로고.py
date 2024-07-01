#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 3108                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/3108                          #+#        #+#      #+#     #
#     Solved: 2024-03-07 14:25:25 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
def find(a):
    if parent[a] == a:
        return a 
    parent[a] = find(parent[a])
    return parent[a]
 
def union(a,b):
    a,b = find(a), find(b)
    parent[b] = a 
    
 
def to_edges(x1,y1,x2,y2):
    return [(x1,y1,x2,y1,0),(x1,y1,x1,y2,1),(x2,y1,x2,y2,1),(x1,y2,x2,y2,0)]
    
RECTANGLES = [to_edges(0,0,0,0)] + [to_edges(*map(int,input().split())) for _ in range(N)]
N += 1
parent = [i for i in range(N)]
 
def isOverlapped(rect1, rect2):
    def edge_overlap(e1, e2):
        v1, v2 = e1[-1], e2[-1] # isVertical 
        meet_type = v1+v2
        if not meet_type: 
            e1, e2 = (e1,e2) if e1[0] < e2[0] else (e2,e1)
            return True if e1[1] == e2[1] and e2[0] <= e1[2] else False
        elif meet_type == 1:
            e1, e2 = (e1, e2) if v1 else (e2, e1) 
            return True if e1[1] <= e2[1] <=e1[3] and e2[0] <= e1[0] <=e2[2] else False 
        else:
            e1, e2 = (e1,e2) if e1[1] < e2[1] else (e2,e1)
            return True if e1[0] == e2[0] and e2[1] <= e1[3] else False
    
    for i in range(4):
        e1 = rect1[i]
        for j in range(4):
            e2 = rect2[j]
            if edge_overlap(e1, e2):
                return True 
    return False 
 
for i in range(N-1):
    for j in range(i+1,N):
        rect1 = RECTANGLES[i]
        rect2 = RECTANGLES[j]
        if isOverlapped(rect1, rect2):
            union(i, j)
 
for i in range(N):
    find(i)
print(len(set(parent))-1)