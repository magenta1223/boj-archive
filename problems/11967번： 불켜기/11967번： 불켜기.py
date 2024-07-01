#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11967                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11967                         #+#        #+#      #+#     #
#     Solved: 2024-05-13 16:34:49 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
input = open(0).readline 
D = [(-1,0), (0,1), (1,0), (0,-1)]
N,M = map(int,input().split())
 
# 방에서 켤 수 있는 스위치 
Switches = {(i,j) : [] for i in range(N) for j in range(N)}
for _ in range(M):
    x,y,a,b = map(int,input().split())
    Switches[(x-1,y-1)].append((a-1,b-1))
 
visited = [[False] * N for _ in range(N)]
visited[0][0] = True 
LIGHTS = [[False] * N for _ in range(N)]
LIGHTS[0][0] = True
 
# --------------------------------- # 
 
# 누를 수 있는 스위치를 전부 누르기 
def switch_on(on):
    for a,b in on:
        LIGHTS[a][b] = True 
 
    # 새로 방문 가능한 곳을 전부 찾는다 
    q = deque([])
    for x in range(N):
        for y in range(N):
            if visited[x][y] or not LIGHTS[x][y]:
                continue
 
            for dx,dy in D:
                nx,ny = x+dx, y+dy 
                if 0<=nx<N and 0<=ny<N and visited[nx][ny]:
                    q.append((x,y))
                    break 
 
    return q 
 
# 현재 방문 가능한 방을 전부 방문
def visit(q:deque):
    ON = []
    for x,y in q:
        ON.extend(Switches[(x,y)])
 
    while q:
        x,y = q.popleft()
        for dx,dy in D:
            nx,ny = x+dx, y+dy 
            if not (0<=nx<N and 0<=ny<N):
                continue 
            if not visited[nx][ny] and LIGHTS[nx][ny]:
                # 방문
                visited[nx][ny] = True 
                q.append((nx,ny))
 
                # 불 켜기 
                for a, b in Switches[(nx,ny)]:
                    ON.append((a,b))
 
    return ON 
                    
q = deque([(0,0)])
for a,b in Switches[(0,0)]:
    LIGHTS[a][b] = True 
 
 
while q:
    next_on = visit(q)
    q = switch_on(next_on)
    for x,y in q:
        visited[x][y] = True 
 
# --------------------------------- # 
 
print(sum([1 for i in range(N) for j in range(N) if LIGHTS[i][j]]))