#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14502                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14502                         #+#        #+#      #+#     #
#     Solved: 2024-02-12 15:03:22 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from itertools import combinations 
from collections import deque
# print(len(list(combinations(list(range(64)), 3))) )
N,M=map(int,input().split())
BOARD=[list(map(int,input().split())) for _ in range(N)]
# 빈 공간
 
EMPTY=[]
VIRUS=[]
for i in range(N):
    for j in range(M):
        if not BOARD[i][j]:
            EMPTY.append((i,j))
        elif BOARD[i][j] == 2:
            VIRUS.append((i,j))            
COMBS = list(combinations(range(len(EMPTY)), 3))
DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]
def solve(b, new_walls):
    board = [[ b[i][j] for j in range(M)]  for i in range(N)]
    for cell_index in new_walls:
        x,y = EMPTY[cell_index]
        board[x][y] = 1
        
    visited = [[False] * M for _ in range(N)]
    # calc safety zone
    # 인접한 벽이 아닌 인접한 칸을 바이러스로 채움 
    queue = deque(VIRUS)
    while queue:
        vx, vy=queue.popleft()
        for dx, dy in zip(DX, DY):
            new_x, new_y=vx+dx,vy+dy
            if 0<=new_x<N and 0<=new_y<M and board[new_x][new_y] == 0 and not visited[new_x][new_y]:
                visited[new_x][new_y] = True 
                queue.append((new_x,new_y))
                board[new_x][new_y] = 2
    safety_zone = sum([1 for i in range(N) for j in range(M) if board[i][j] == 0 ])
    return safety_zone
ans = 0
for i, wall_combination in enumerate(COMBS):
    res = solve(BOARD, wall_combination)
    if res > ans:
        ans = res 
print(ans)