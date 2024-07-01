#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 7562                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/7562                          #+#        #+#      #+#     #
#     Solved: 2024-01-26 14:40:23 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

T=int(input())
ds = [[1,2], [2,1], [2,-1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
from collections import deque 
def solve(l, x,y,t_x,t_y):
    visited = set()    
    queue = deque([[x,y,0]])
    while queue:
        x,y,c=queue.popleft()
        if x==t_x and y==t_y:
            print(c)
            break 
        for dx, dy in ds:
            _x, _y = x+dx, y+dy
            if  (_x, _y) not in visited and 0 <= _x < l and 0<= _y < l:
                queue.append([_x, _y, c+1])
                visited.add((_x,_y))
 
for _ in range(T):
    L=int(input())
    x,y=map(int, input().split())
    t_x, t_y = map(int, input().split())
    solve(L, x,y,t_x, t_y)