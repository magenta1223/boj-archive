#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 21609                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/21609                         #+#        #+#      #+#     #
#     Solved: 2024-02-22 12:59:32 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
 
def rotate():
    tmp = [ [0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[N-j-1][i] = A[i][j]  
    return tmp 
 
def gravity():
    for i in range(N-2, -1, -1):
        for j in range(N):
            if A[i][j] < 0:
                continue
            collide = False
            color, A[i][j] = A[i][j], EMPTY
            for k in range(i,N):
                if A[k][j] != EMPTY:
                    collide = True
                    break 
            k = k-1 if collide else k 
            A[k][j] = color
 
N,M = map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]
D=[(-1,0),(1,0),(0,1),(0,-1)]
move = lambda x,y,dx,dy: (x+dx, y+dy)
RAINBOW = 0
EMPTY = 9
ans = 0
while True:
    max_group = {'blocks' : [], 'r' : 0, 'x' : 0, 'y' : 0}
    for i in range(N):
        for j in range(N):
            color = A[i][j]
            if color < 1 or color == EMPTY:
                continue
            group = [(i,j,True)]
            queue = deque([(i,j)])
            visited = set([(i,j)])
            r = 0
            while queue:
                x,y = queue.popleft()
                for dx, dy in D:
                    nx,ny = move(x,y,dx,dy)
                    if 0<=nx<N and 0<=ny<N and A[nx][ny] in [color, RAINBOW] and (nx,ny) not in visited:
                        visited.add((nx,ny))
                        queue.append((nx,ny))
                        group.append((nx,ny, True if A[nx][ny] else False))
                        r += 0 if A[nx][ny] else 1
            # 정렬 기준 
            group.sort(key = lambda x: (-x[2], x[0], x[1]))
            # 정렬 인덱스 틀려서.. 
            group = {'blocks' : group, 'r' : r, 'x' : group[0][0] , 'y' : group[0][1]}
            if len(max_group['blocks']) < len(group['blocks']):
                max_group = group
            elif len(max_group['blocks']) == len(group['blocks']):
                if max_group['r'] < group['r']:
                    max_group = group
                elif max_group['r'] == group['r']:
                    if max_group['x'] < group['x']:
                        max_group = group
                    elif max_group['x'] == group['x']:
                        if max_group['y'] < group['y']:
                            max_group = group      
    if len(max_group['blocks']) <= 1:
        break
    for x,y,_ in max_group['blocks']:
        A[x][y] = EMPTY
    ans += len(max_group['blocks']) ** 2
    gravity()
    A = rotate()
    gravity()
print(ans)