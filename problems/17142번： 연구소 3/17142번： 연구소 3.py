#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17142                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17142                         #+#        #+#      #+#     #
#     Solved: 2024-02-19 10:57:46 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from itertools import combinations
from collections import deque
N,M=map(int,input().split())
BOARD=[list(map(int,input().split())) for _ in range(N)]
EMPTY = 0
WALL = 1
VIRUS = 2
D = [(-1,0),(1,0),(0,1), (0,-1)]
VIRUSES = [(i,j) for i in range(N) for j in range(N) if BOARD[i][j] == VIRUS]
EMPTIES = set((i,j) for i in range(N) for j in range(N) if BOARD[i][j] == EMPTY)
COMBS=combinations(range(len(VIRUSES)), M)
ans = float('inf')
for comb in COMBS:
    activated = [(*VIRUSES[i], 0) for i in comb]
    infected = set()
    # bfs
    queue = deque(activated)
    visited = [[False] * N for _ in range(N)]
    if infected != EMPTIES:
        while queue:
            x,y,t = queue.popleft()
            for dx, dy in D:
                nx, ny = x+dx, y+dy
                if 0<=nx<N and 0<=ny<N and BOARD[nx][ny] != WALL and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, t+1))
                    if BOARD[nx][ny] == EMPTY:
                        infected.add((nx, ny))
            if infected == EMPTIES:
                break 
        if infected == EMPTIES and ans > t :
            ans = t+1
    else:
        ans = 0
        break
print(ans if ans != float('inf') else -1)