#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 4991                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/4991                          #+#        #+#      #+#     #
#     Solved: 2024-02-29 14:34:06 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
from copy import deepcopy
WALL = 'x'
DUST = '*'
EMPTY = '.'
D = [(-1,0),(0,1),(1,0),(0,-1)]
 
def solve(height, width, room):
    x,y = [(i,j) for i in range(height) for j in range(width) if room[i][j] == 'o'][0]
    dusts = [(i,j) for i in range(height) for j in range(width) if room[i][j] == DUST]
    
    def min_dist(height, width, room, dust, dusts):
        x,y = dust 
        queue = deque([(x,y,0)])
        visited = [[False] * width for _ in range(height)]
        visited[x][y] = True
        dists = [float("inf")] * len(dusts)
        dists[dusts.index(dust)] = 0
        while queue:
            x,y,d = queue.popleft()
            for dx, dy in D:
                nx,ny = x+dx, y+dy 
                if 0<=nx<height and 0<=ny<width and room[nx][ny] != WALL and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny,d+1))
                    if (nx,ny) in dusts:
                        dists[dusts.index((nx,ny))] = d+1
            # 전부 방문했다면 패스 
            if all([visited[x][y] for x,y in dusts]):
                break 
        return dists
    
    dusts = [(x,y)] + dusts
    visited = []
    for dust in dusts:
        visited.append(min_dist(height, width, room, dust, dusts))
    global ans
    ans = float("inf")
    
    def dfs(start, dist, dusts, bitmask):
        global ans
        if bitmask == ((1<<len(dusts)) - 2):
            ans = min(ans, dist)
            return 
        if dist >= ans:
            return 
        for i in range(1, len(dusts)):
            if bitmask & (1<<i):
                continue
            dfs(i, dist + visited[start][i], dusts, bitmask|(1<<i))
 
    dfs(0,0,dusts, 0)
    print(-1 if ans == float('inf') else ans)
 
while True:
    w,h = map(int, input().split())
    if (w,h) == (0,0):
        break 
    ROOM = [list(input().strip()) for _ in range(h)]
    solve(h,w,ROOM)