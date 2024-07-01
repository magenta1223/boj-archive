#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 18500                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/18500                         #+#        #+#      #+#     #
#     Solved: 2024-05-07 12:49:25 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
R,C=map(int,input().split())
A=[[s for s in input().strip()] for _ in range(R)]
N=int(input().strip())
H=list(map(int, input().split()))
D = [(-1,0), (0,1), (1,0), (0,-1)]
 
# 클러스터는 한번에 최대 몇개 만들어질까?
# 쏘기 전에는 반드시 1개임. 
# 쐈을 때 최대 3개까지 생긴다. 
 
 
# 구현해야 하는 것
# 1. 벽돌깨기 
def throw_stick(arr, height, isLeft):    
    row = R-height 
    seq = (0,C) if isLeft else (C-1, -1, -1)
    for i in range(*seq):
        if arr[row][i] == "x":
            arr[row][i] = '.'
            break 
    return arr 
 
# 2. 클러스터들을 찾고
def find_clusters(arr):
    visited = [[False] * C for _ in range(R)]
    clusters = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == "." or visited[i][j]:
                continue
            queue = deque([(i,j)])
            visited[i][j] = True
            cluster = [(i,j)]
            while queue:
                x,y = queue.popleft()
                for dx, dy in D:
                    nx,ny = x+dx, y+dy 
                    if 0<=nx<R and 0<=ny<C and arr[nx][ny] == 'x' and not visited[nx][ny]:
                        queue.append((nx, ny))
                        cluster.append((nx,ny))
                        visited[nx][ny] = True 
 
            clusters.append(cluster)
    return clusters
 
# 3. 바닥으로 
def drop(arr, clusters):    
    # 바닥과 닿은 cluster는 pass 
    for cluster in clusters:
        # 바닥과 닿았나요? 
        if any([ x == R-1  for x,y in cluster]):
            continue
        # 얼만큼 떨굴 수 있는지? 
        # i만큼 내렸을 때, 
        # 1. 범위 안인지? 
        # 2. 이동 했을 때, 자기 자신이거나, 다른 빈 공간인지? 
        i = 1        
        while all([x+i<R for x,y in cluster]) and all([(x+i,y) in cluster or arr[x+i][y] == "." for x,y in cluster]):
            i += 1
        i -= 1    
        for x,y in cluster:
            arr[x][y] = '.'
        for x,y in cluster:
            arr[x+i][y] = 'x'
    return arr 
 
isLeft = True
for h in H:
    A = throw_stick(A, h, isLeft)
    clusters = find_clusters(A) 
    A = drop(A, clusters)
    isLeft = not isLeft
    
print(*[''.join(A[i]) for i in range(R)], sep = '\n')