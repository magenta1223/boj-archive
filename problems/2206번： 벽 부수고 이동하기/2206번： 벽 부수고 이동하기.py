#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2206                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2206                          #+#        #+#      #+#     #
#     Solved: 2024-01-26 17:01:01 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M=map(int, input().split())
array = [ [ int(x) for x in input().strip()] for _ in range(N)]
W = { (i,j) for j in range(M) for i in range(N) if array[i][j]}
from collections import deque 
D = [[1,0], [-1,0], [0,1], [0,-1]]
visited = set()
# x, y, 길이, 벽부숨?
queue = deque([[0,0,1,False]])
sucess = False
while queue:
    x,y,l,wallbreak=queue.popleft()
    if x==N-1 and y==M-1:
        sucess=True
        break
    for dx, dy in D:
        _x,_y=x+dx,y+dy
        if (_x,_y, wallbreak) not in visited and 0<=_x<N and 0<=_y<M:
            if (_x,_y) in W:
                # 벽인데 이전에 벽 안부쉈음. 부수기 
                if not wallbreak:
                    visited.add((_x,_y,wallbreak))
                    queue.append([_x,_y,l+1,True])
                else: # 이전에 부쉈음. 못한다. 
                    pass 
            else:
                visited.add((_x,_y,wallbreak))
                queue.append([_x,_y,l+1,wallbreak])
if sucess:
    print(l)
else:
    print(-1)