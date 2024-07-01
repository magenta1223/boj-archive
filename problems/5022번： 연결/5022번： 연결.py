#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 5022                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/5022                          #+#        #+#      #+#     #
#     Solved: 2024-03-12 11:00:26 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
def inRange(x,y):
    return 0<=x<N+1 and 0<=y<M+1 
D = [(-1,0),(0,1),(1,0),(0,-1)]
 
N,M=map(int, input().split())
 
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
B1 = list(map(int, input().split()))
B2 = list(map(int, input().split()))
 
# 1. 하나를 최단거리로 연결 -> path 구하고 
# 2. 그 path를 visited에 반영 -> 가능? 
def bfs(start, end, blocked):
    queue = deque([start])
    visited = [[False] * (M+1) for _ in range(N+1)]
    hist = [[(-1,-1)] * (M+1) for _ in range(N+1)]
    visited[start[0]][start[1]] = True 
    for x,y in blocked:
        visited[x][y] = True 
    done = False 
    while queue and not done:
        x,y = queue.popleft()
        for dx, dy in D:
            nx, ny = x+dx, y+dy 
            if inRange(nx,ny) and not visited[nx][ny]:
                visited[nx][ny] = True 
                queue.append((nx,ny))
                hist[nx][ny] = (x,y)
                if (nx,ny) == end:
                    done = True 
                    break
    # resolve 
    path = []
    x,y = end
    while hist[x][y] != (-1,-1):
        path.append((x,y))
        x,y = hist[x][y]
    path.append(start)
    path.reverse()
    return len(path)-1 if len(path) > 1 else float("inf"), path
 
d1, path_A = bfs(A1, A2, [B1,B2])
d2, _ = bfs(B1, B2, path_A)
 
d3, path_B = bfs(B1, B2, [A1,A2])
d4, _ = bfs(A1, A2, path_B)
 
ans = min(d1+d2, d3+d4)
print(ans if ans != float("inf") else "IMPOSSIBLE")