#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 7576                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/7576                          #+#        #+#      #+#     #
#     Solved: 2024-01-26 15:36:33 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

M,N=map(int, input().split())
array=[list(map(int, input().split())) for _ in range(N)]
from collections import deque
queue = deque([])
candidate = set()
for x in range(N):
    for y in range(M):
        v =array[x][y] 
        if v == 1:
            queue.append([x, y, 0]) 
        elif v == 0:
            candidate.add((x,y)) 
            
D = [[1, 0], [-1,0], [0,1], [0,-1]]
 
if not queue: # 익은 토마토가 없음
    print(-1)
elif not candidate: # 이미 다 익음 
    print(0)
else:
    while queue:
        x,y,c = queue.popleft()
        for dx, dy in D:
            _x,_y=x+dx,y+dy
            if (_x, _y) in candidate and 0<=_x<N and 0<=_y<M:
                queue.append([_x, _y, c+1])
                candidate.remove((_x, _y))    
    if candidate:
        print(-1)
    else:
        print(c)