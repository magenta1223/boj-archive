#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 25308                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/25308                         #+#        #+#      #+#     #
#     Solved: 2024-07-05 04:09:51 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 볼록 다각형을 만드는 경우의 수. 
# 총 8개의 스탯.
# 최대 4만개니까 그냥 다 해봐도 됨 
# 1. 스탯과 위치를 받아서 좌표를 구하고 
# 2. 1번스탯에서 시작해서 (2,3), (3,4) 순으로 삼각형을 만든다
# 3. 1과 i, 1과 i+1을 잇는 선의 crossProduct값이 부호가 달라지면 너는 오목 다각형이여   

from itertools import permutations 
from math import sqrt 
s2 = sqrt(2)/2
def crossProduct(x1,y1,x2,y2,x3,y3):
    v = (x2-x1)*(y3-y2) - (x3-x2)*(y2-y1)
    if v > 0:
        return 1 
    elif v < 0:
        return -1 
    else:
        return 0 
def statToCoords(stat, idx):
    rot = [[1,0], [0,1]]
    for _ in range(idx):
        rot = [ 
            [rot[0][0]*s2 - rot[0][1] *s2,  rot[0][0]*s2 + rot[0][1] *s2 ],
            [rot[1][0]*s2 - rot[1][1] *s2,  rot[1][0]*s2 + rot[1][1] *s2 ],               
        ]
    return rot[0][1]*stat, rot[1][1]*stat

A = list(map(int,input().split()))
ans = 0
for comb in permutations(list(range(8)), 8):
    for i in range(8):
        x1,y1 = statToCoords(A[comb[i]], i)
        x2,y2 = statToCoords(A[comb[(i+1)%8]], (i+1)%8)
        x3,y3 = statToCoords(A[comb[(i+2)%8]], (i+2)%8)
        if crossProduct(x1,y1,x2,y2,x3,y3) != -1:
            break 
    else:
        ans += 1  
print(ans)