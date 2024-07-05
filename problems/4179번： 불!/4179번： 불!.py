#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 4179                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/4179                          #+#        #+#      #+#     #
#     Solved: 2024-07-01 14:14:07 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
 
D = [(-1,0), (0,1), (1,0), (0,-1)]
N,M = map(int,input().split())
A = [list(input().strip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
burned = [[False] * M for _ in range(N)]
 
fires = deque([])
 
for i in range(N):
    for j in range(M):
        if A[i][j] == "J":
            q = deque([(i,j,0)])
            A[i][j] = "."
            visited[i][j] = True 
        elif A[i][j] == "F":
            fires.append((i,j))
            burned[i][j] = True 
 
def move(q:deque):
    nq = deque([])
    done = False 
    while q:
        x,y,t = q.popleft()
        if burned[x][y]:
            continue
        for dx,dy in D:
            nx,ny = x+dx, y+dy 
            if not 0<=nx<N or not 0<=ny<M:
                done = True 
                break 
            
            if 0<=nx<N and 0<=ny<M and A[nx][ny] == "." and not burned[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True 
                nq.append((nx,ny,t+1))
    return nq, done
 
def spreadFire(fires:deque):
    nfires = deque([])
    while fires:
        x,y = fires.pop()
        for dx,dy in D:
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M and A[nx][ny] == "." and not burned[nx][ny]:
                burned[nx][ny] = True 
                nfires.append((nx,ny))
    return nfires 
 
t = 0
done = False 
while not done:
    t += 1 
    q, done = move(q)
    fires = spreadFire(fires)
    # 미로 탈출 불가능인 경우가 있다. 
    # 1. 탈출 못했는데 이동 가능한 영역이 없을 때 -> 불이 번져서 사망
    if not done and not q:
        t = "IMPOSSIBLE"
        break 
print(t)