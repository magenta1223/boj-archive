#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 16236                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/16236                         #+#        #+#      #+#     #
#     Solved: 2024-02-15 20:07:21 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
N=int(input().strip())
BOARD=[list(map(int,input().split())) for _ in range(N)]
D=[(-1,0),(0,-1),(0,1),(1,0)]
 
# 체크한번하고 -> 다음 먹이로 움직이고 
shark = None
for i in range(N):
    for j in range(N):
        if BOARD[i][j] == 9:
            shark = i,j,2,0
            BOARD[i][j] = 0
            break 
    if shark is not None:
        break 
    
ans = 0
 
while True:
    x,y,s,eat = shark 
    queue = deque([(x,y,0)])
    visited = [ [False] * N for _ in range(N)]
    visited[x][y] = True
    next_targets = []
    min_dist = float("inf")
 
    while queue:
        x, y, t = queue.popleft()
        if 0 < BOARD[x][y] < s:
            if t < min_dist:
                min_dist = t
                next_targets = [(x,y)]
            elif t == min_dist:
                next_targets.append((x,y))
            continue
        for dx, dy in D:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and BOARD[nx][ny] <= s:
                # 이동 가능
                queue.append((nx, ny, t+1))
                visited[nx][ny] = True
    if not next_targets:
        break 
    else:
        next_targets.sort()
        nx, ny = next_targets[0]
        BOARD[nx][ny] = 0
        eat += 1
        if eat == s:
            shark = nx, ny, s+1, 0
        else:
            shark = nx, ny, s, eat
        ans += min_dist
print(ans)