#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 7569                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/7569                          #+#        #+#      #+#     #
#     Solved: 2024-01-26 15:55:02 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

M,N,H=map(int, input().split())
array=[[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
from collections import deque
queue = deque([])
candidate = set()
for h in range(H):
    for x in range(N):
        for y in range(M):
            v =array[h][x][y] 
            if v == 1:
                queue.append([h, x, y, 0]) 
            elif v == 0:
                candidate.add((h, x,y)) 
            
D = [[1, 0, 0], [-1,0, 0], [0,1,0], [0,-1,0], [0,0,1], [0,0,-1]]
 
if not queue: # 익은 토마토가 없음
    print(-1)
elif not candidate: # 이미 다 익음 
    print(0)
else:
    while queue:
        h,x,y,c = queue.popleft()
        for dh, dx, dy in D:
            _h,_x,_y=h+dh,x+dx,y+dy
            if (_h, _x, _y) in candidate and 0<=_h<H and 0<=_x<N and 0<=_y<M:
                queue.append([_h,_x, _y, c+1])
                candidate.remove((_h,_x, _y))    
    if candidate:
        print(-1)
    else:
        print(c)