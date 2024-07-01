#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17135                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17135                         #+#        #+#      #+#     #
#     Solved: 2024-04-01 14:07:21 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from itertools import combinations
from collections import deque 
 
NEXT = [(-1,0), (0,1), (0,-1)]
N,M,D = map(int, input().split())
A= [list(map(int, input().split())) for _ in range(N)]
 
 
 
def find(arr, idx):
    min_dist, n = None,  len(arr)
    # bfs 
    q = deque([(n, idx,0)])
    visited = [[False] * M for _ in range(n)]
    targets = []
    while q:
        x,y,d = q.popleft()
        for dx, dy in NEXT:
            nx, ny = x+dx, y+dy 
            # 조건에 맞고, 안가봤고, 범위 이내 
            if 0<=nx<n and 0<=ny<M and not visited[nx][ny] and d+1 <= D:
                # 아직 적을 못본 경우 
                if min_dist is None:
                    # 적을 마주침. 최단거리 갱신. bfs이므로 반드시 최단거리임. 
                    visited[nx][ny] = True 
                    if arr[nx][ny]:
                        min_dist = d+1
                        targets.append((nx,ny))
                    else:
                        q.append((nx,ny,d+1))
                else:
                    if d+1 == min_dist and arr[nx][ny]:
                        targets.append((nx,ny))
    if targets:
        targets.sort(key=lambda x: x[1])
        return [targets[0]]
    else:
        return []
 
# 구현 / 시뮬레이션이네 
ans = 0
for a,b,c in combinations(range(M), 3):
    res = 0 
    arr = [[ A[i][j] for j in range(M)] for i in range(N)]
    for _ in range(N):
        _a = find(arr, a)
        _b = find(arr, b)    
        _c = find(arr, c)  
        
        for x, y in _a + _b + _c:
            if arr[x][y]:
                arr[x][y] = 0 
                res += 1 
        arr.pop()
    ans = max(ans, res)
print(ans)