#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 9376                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/9376                          #+#        #+#      #+#     #
#     Solved: 2024-03-05 14:23:57 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

EMPTY = '.'
WALL = '*'
TARGET = '$'
DOOR = "#"
INF = float("inf")
D = [(-1,0),(0,1),(1,0),(0,-1)]
from collections import deque 
 
def solve(prison, h, w):
    def bfs(x,y,h,w, prison):
        queue = deque([(x,y,0)])
        visited = [[INF] * w for _ in range(h)]
        visited[x][y] = 0
        while queue:
            x,y,door = queue.popleft()
            for dx,dy in D:
                nx,ny = x+dx, y+dy 
                # 방문 했더라도 문을 적게 열었으면 재방문 
                if 0<=nx<h and 0<=ny<w and prison[nx][ny] != WALL:
                    # 
                    if prison[nx][ny] == DOOR:
                        if visited[nx][ny] > door+1:
                            queue.append((nx,ny,door+1))
                            visited[nx][ny] = door+1
                    else:
                        if visited[nx][ny] > door:                            
                            visited[nx][ny] = door
                            queue.append((nx,ny,door))
        return visited 
    
    # 상근, 죄수 2명이 어느 한 지점으로 간다.
    # 이 때 열어야 하는 문의 수의 총합이 가장 작으면 됨. 
    # 상근이는 감옥밖을 자유롭게 이동 = 빈칸으로 둘러싸기 
    prison = [[EMPTY] * (w+2)] + [ [EMPTY] + row + [EMPTY] for row in prison] + [[EMPTY] * (w+2)]
    
    prisoners = []
    for i in range(h+2):
        for j in range(w+2):
            if prison[i][j] == TARGET:
                prisoners.append((i,j))
    p1, p2 = prisoners 
 
    # bfs로 해당 지점까지 도달 
    v0 = bfs(0,0,h+2, w+2, prison)
    v1 = bfs(*p1,h+2, w+2, prison)
    v2 = bfs(*p2,h+2, w+2, prison)
    
 
    ans = float("inf")
    ans_ = None
    for i in range(h+2):
        for j in range(w+2):
            # 셋 다 방문가능하면서 최솟값 
            if v0[i][j] != INF and v1[i][j] != INF and v2[i][j] != INF:
                v = v0[i][j] + v1[i][j] + v2[i][j]
                if prison[i][j] == DOOR:
                    v -= 2
                ans = min(ans, v)
    return ans 
 
 
 
for _ in range(int(input())):
    H,W = map(int,input().split())
    PRISON = [list(input().strip()) for _ in range(H)]
    
    print(solve(PRISON, H, W))