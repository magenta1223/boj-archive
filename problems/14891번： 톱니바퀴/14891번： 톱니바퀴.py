#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14891                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14891                         #+#        #+#      #+#     #
#     Solved: 2024-02-13 16:13:13 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
GEAR = [ [ int(s) for s in input().strip()] for _ in range(4)]
K=int(input().strip())
def _rot(g,direction):
    return [g[-1]] + g[:-1] if direction == 1 else g[1:] + [g[0]]
def rot(g1, g2, isLeft, direction):
    rotated = False
    if isLeft and g1[2] != g2[6]:
        g2 = _rot(g2, -direction)
        rotated = True    
    elif not isLeft and g1[6] != g2[2]:
        g2 = _rot(g2, -direction)
        rotated = True    
    return g2, rotated
        
ADJ = {
    0 : [1],
    1 : [0,2],
    2 : [1,3],
    3 : [2]
}
 
for _ in range(K):
    g1, direction = map(int,input().split())
    g1 -= 1
    queue = deque([[g1, direction]])
    next_gears = [0] * 4
    next_gears[g1] = _rot(GEAR[g1], direction)
    rotated = [False] * 4
    while queue:
        g1, direction = queue.popleft()
        if rotated[g1]:
            continue
        rotated[g1] = True
        for g2 in ADJ[g1]:
            g2_rotated, isRotated = rot(GEAR[g1], GEAR[g2], g1 < g2, direction)
            if isRotated:
                queue.append([g2, direction * (-1)])
                next_gears[g2] = g2_rotated
    for i in range(4):
        GEAR[i] = next_gears[i] if next_gears[i] != 0 else GEAR[i]
print(sum([GEAR[i][0] * (2**i) for i in range(4)]))