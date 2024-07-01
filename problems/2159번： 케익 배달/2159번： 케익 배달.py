#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2159                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2159                          #+#        #+#      #+#     #
#     Solved: 2024-03-25 20:01:32 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
R = list(map(int, input().split()))
P = [list(map(int, input().split())) for _ in range(N)]
 
# 주문 들어온 순으로 배달. 
# 전달하려면 -> 인접지점 or 직접 도달해야 함. 
# 최단거리 구하세용 
def dist(x,y,px,py):
    return abs(x-px) + abs(y-py)
 
pX = [(*R, 0)]
 
D = [(0,0), (-1,0), (0,1), (1,0), (0,-1)]
for x,y in P:
    # 인접 or 직접 
    X = [(x+dx, y+dy) for dx, dy in D]
    xx = []
    for x,y in X:
        minD = float("inf")
        for px,py,pd in pX:
            minD = min(dist(x,y,px,py) + pd, minD)
        xx.append((x,y,minD))
    pX = xx 
 
pX.sort(key = lambda x: x[-1])
print(pX[0][-1])