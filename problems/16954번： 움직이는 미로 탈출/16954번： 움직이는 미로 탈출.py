#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 16954                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/16954                         #+#        #+#      #+#     #
#     Solved: 2024-02-29 17:37:15 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
 
A = [list(input().strip()) for _ in range(8)]
D = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(0,0)]
 
def fall(A, t):
    if t == 0:
        return A
    return [['.'] * 8] * t + A[:-t]
 
# 최대 8초간 생존 가능하면 1 아니면 0
 
queue = deque([(7,0,0)])
visited = set([(7,0,0)])
t = 0
while queue and t < 8:
    x,y,t = queue.popleft()
    array_t = fall(A,t)
    for dx, dy in D:
        nx,ny = x+dx, y+dy 
        # nx,ny가 빈칸이면서 그 위도 빈칸이어야 함 
        if 0<=nx<8 and 0<=ny<8 and array_t[nx][ny] == "." and (nx,ny,t+1) not in visited:
            if nx>0:
                if array_t[nx-1][ny] == ".":
                    queue.append((nx,ny,t+1))
                    visited.add((nx,ny,t+1))
            else:
                queue.append((nx,ny,t+1))
                visited.add((nx,ny,t+1))
 
print(1 if t == 8 else 0)