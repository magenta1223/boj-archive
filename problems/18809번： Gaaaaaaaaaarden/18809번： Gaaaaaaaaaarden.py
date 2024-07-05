#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 18809                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/18809                         #+#        #+#      #+#     #
#     Solved: 2024-07-02 19:48:30 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from itertools import combinations 
from collections import deque 
 
 
# 뿌릴 수 있는 땅의 개수는 10개 이하다. 
 
# 10 C G 
# (10-G) C R 
# -> 전부 확인 
 
def sim(greens, reds):
    def diffuse(q:deque):
        nq = set()
        while q:
            x,y = q.popleft()
            for dx, dy in D:
                nx,ny = x+dx, y+dy 
                if 0<=nx<N and 0<=ny<M and A[nx][ny] >=1 and not visited[nx][ny] and (nx,ny) not in nq:
                    nq.add((nx,ny))
        return nq 
 
    nFlowers = 0 
    visited = [[False] * M for _ in range(N)]
 
    for x,y in greens+reds:
        visited[x][y] = True 
 
    gq, rq = deque(greens), deque(reds)
    while gq or rq:
        # 매초마다
        # 1. gq, rq를 확산
        # 2. 동시확산된 곳이 있으면 꽃의 개수를 추가하고, 그 위치를 다음 gq, rq에서 제거 
        gq, rq = diffuse(gq), diffuse(rq)
        # 동시 확산된 곳이 있는지? 
        intersection = gq.intersection(rq)
        if intersection:
            for (x,y) in intersection:
                nFlowers += 1 
                gq.remove((x,y))
                rq.remove((x,y))
                visited[x][y] = True 
 
        for x,y in gq.union(rq):
            visited[x][y] = True 
        
        gq = deque(list(gq))
        rq = deque(list(rq))
    
    return nFlowers
 
D = [(-1,0), (0,1), (1,0), (0,-1)]
N,M,G,R = map(int,input().split())
A = [list(map(int, input().split())) for _ in range(N)]
targets = [(i,j) for i in range(N) for j in range(M) if A[i][j] == 2]
ans = 0 
 
for gIndices in combinations(list(range(len(targets))),G):
    greens = [targets[idx] for idx in gIndices]
    left = list(set(targets) - set(greens))
    for rIndices in combinations(list(range(len(left))),R):
        reds = [left[idx] for idx in rIndices]
        ans = max(ans, sim(greens, reds))
 
print(ans)