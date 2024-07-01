#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2638                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2638                          #+#        #+#      #+#     #
#     Solved: 2024-03-06 14:44:05 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
 
N,M=map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
D = [(-1,0),(0,1),(1,0),(0,-1)]
 
def update_airs(array, starts, visited):
    queue = deque(starts)
    for x,y in starts:
        visited[x][y] = True
    while queue:
        x,y = queue.popleft()
        for dx, dy in D:
            nx,ny = x+dx, y+dy 
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and not array[nx][ny]:
                visited[nx][ny] = True 
                queue.append((nx,ny))
    return visited
    
def melt(array, visited):
    tmp = []
    for i in range(N):
        for j in range(M):
            if visited[i][j] or not array[i][j]: # already melted 
                continue
            if sum([visited[i+dx][j+dy] for dx, dy in D]) > 1:
                tmp.append((i,j))
    for i, j in tmp:
        array[i][j] = 0
    return array, tmp 
 
def check(array):
    return False if sum([sum(row) for row in array]) else True 
 
t=0
visited = [[False] * M for _ in range(N)]
starts = [(0,0)]
while True:
    if check(A):
        break 
    visited = update_airs(A, starts, visited)
    A, starts = melt(A, visited)
    t += 1
print(t)