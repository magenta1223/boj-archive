#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 3197                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/3197                          #+#        #+#      #+#     #
#     Solved: 2024-02-27 11:59:34 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
import sys
input = sys.stdin.readline
 
def init_array(n,m,v):
    return [[v] * m for _ in range(n)]
 
def melt(wq, arr, melted):
    wq_next = deque([])
    # 녹이기 
    while wq:
        x,y = wq.popleft()
        A[x][y] = 0 
        for dx, dy in D:
            nx,ny= x+dx, y+dy 
            # 
            if 0<=nx<R and 0<=ny<C and not melted[nx][ny]:
                if arr[nx][ny]: # 벽
                    wq_next.append((nx,ny))
                else:
                    wq.append((nx,ny))    
                melted[nx][ny] = 1 # 미리 녹여두는거 아닌가? 상관 없.. 지 
    return wq_next, arr, melted 
 
def check(sq, arr, visited):
    global target 
    sq_next, done = deque([]), False 
    while sq and not done:
        x,y = sq.popleft()
        for dx, dy in D:
            nx,ny= x+dx, y+dy 
            if 0<=nx<R and 0<=ny<C and not visited[nx][ny]:
                if arr[nx][ny]:
                    sq_next.append((nx,ny))
                else:
                    sq.append((nx,ny))
                visited[nx][ny] = 1 #
                if (nx,ny) == target:
                    done = True
                    break 
    return sq_next, visited, done 
 
R,C=map(int,input().split())
A=[list(input()) for _ in range(R)]
 
T = {'.' : 0, "X" : 1, "L" : 0}
D = [(-1,0),(0,1),(1,0),(0,-1)]
 
wq, sq = deque([]),deque([])
melted, visited = init_array(R,C,0), init_array(R,C,0)
SWANS = []
 
for i in range(R):
    for j in range(C):
        v = A[i][j]
        A[i][j] = T[v]
        if T[v] == 0:
            melted[i][j] = 1 # 방문처리.. 
            wq.append((i,j))
        if v == "L":
            if not sq:
                start = (i,j)
                sq.append(start)
                visited[i][j] = 1
            else:
                target = (i,j)
            SWANS.append((i,j))
t = 0
done = False
while True:
    wq, A, melted = melt(wq, A, melted)
    sq, visited, done = check(sq, A, visited)
    if done:
        break
    t += 1
print(t)
 