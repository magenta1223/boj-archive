#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 15686                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/15686                         #+#        #+#      #+#     #
#     Solved: 2024-02-14 19:44:38 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from itertools import combinations
get_dist = lambda x1, y1, x2, y2: abs(x1-x2) + abs(y1-y2)
N,M=map(int,input().split())
BOARD=[list(map(int,input().split())) for _ in range(N)]
empty, house, chicken = 0,1,2
 
# 
HOUSE = []
CHICK = []
for i in range(N):
    for j in range(N):
        if BOARD[i][j] == house:
            HOUSE.append((i,j))
        elif BOARD[i][j] == chicken:
            CHICK.append((i,j)) 
 
COMBS=list(combinations(range(len(CHICK)), M))
min_chickdist = 1300
for comb in COMBS:
    chicks = [CHICK[i] for i in comb]
    # 치킨거리 구하기 
    # 그냥 구할까 ? 
    chick_dist = 0
    for x,y in HOUSE:
        dist = 100
        for cx, cy in chicks:
            dist = min(dist, get_dist(x,y,cx,cy))
        chick_dist += dist
    min_chickdist = min(min_chickdist, chick_dist)
print(min_chickdist)