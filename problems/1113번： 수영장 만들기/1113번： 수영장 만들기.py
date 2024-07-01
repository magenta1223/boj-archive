#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1113                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1113                          #+#        #+#      #+#     #
#     Solved: 2024-05-13 18:28:11 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
 
D = [(-1,0), (0,1), (1,0), (0,-1)]
N,M = map(int,input().split())
POOL = [list(map(int, list(input().strip()))) for _ in range(N)]
depth = max([max(line) for line in POOL])
 
ans = 0 
 
def bfs(x,y):
    q = deque([(x,y)])
    res = depth - POOL[x][y]    
    cells = [(x,y)]
    while q:
        x,y = q.popleft()
 
        for dx,dy in D:
            nx,ny = x+dx, y+dy 
            if 0<=nx<N and 0<=ny<M:
                # 테두리인데 물이 흐를 수 있다
                if (nx in [0,N-1] or ny in [0,M-1]):
                    if POOL[nx][ny] < depth:
                        # 종료 
                        q,res = [], 0
                        break 
                elif not visited[nx][ny] and POOL[nx][ny] < depth:
                    visited[nx][ny] = True 
                    res += depth - POOL[nx][ny]
                    q.append((nx,ny))
                    cells.append((nx,ny))
 
    if res:
        for x,y in cells:
            POOL[x][y] = depth
    
    return res
 
 
ans = 0
while depth:
    for i in range(1,N-1):
        for j in range(1,M-1):
            # if visited[i][j] or POOL[i][j] >= depth:
            #     continue 
            # visited[i][j] = True
            if POOL[i][j] >= depth:
                continue 
            visited = [[False] * M for _ in range(N)]
            visited[i][j] = True 
 
 
            ans += bfs(i,j)
 
    depth -= 1 
 
print(ans)