#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 20058                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/20058                         #+#        #+#      #+#     #
#     Solved: 2024-02-21 19:35:30 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def rotate(l):
    c = 2**(N-l)
    s = 2**l
    matrices = [ [[ A[i*s + _i][j*s + _j] for _j in range(s)] for _i in range(s)]  for i in range(c) for j in range(c)] 
    matrices = [_rotate(mx,s) for mx in matrices]
    for i in range(S):
        for j in range(S):
            (i0, i1), (j0,j1) = divmod(i,s), divmod(j,s) 
            idx_m = i0*c + j0
            A[i][j] = matrices[idx_m][i1][j1]
 
def _rotate(matrix, size):
    tmp = [[0] * size for _ in range(size)]    
    for i in range(size):
        for j in range(size):
            tmp[j][size-i-1] = matrix[i][j]
    return tmp 
 
 
def melt():
    tmp = [[0] * S for _ in range(S)]
    for x in range(S):
        for y in range(S):
            if A[x][y] and 3 > sum([1 for dx, dy in D if 0<=x+dx<S and 0<=y+dy<S and A[x+dx][y+dy]]):
                tmp[x][y] = A[x][y] - 1
            else:
                tmp[x][y] = A[x][y]
    return tmp
 
    
 
# 3. 녹이기 
N,Q = map(int,input().split())
S = 2**N
A=[list(map(int,input().split())) for _ in range(S)]
L=list(map(int,input().split()))
D=[(-1,0), (0,-1),(1,0),(0,1)]
 
for l in L:
    rotate(l)
    A = melt()
 
from collections import deque 
 
visited =  [[False] * S for _ in range(S)]
area = 0
for i in range(S):
    for j in range(S):
        if visited[i][j] or not A[i][j]:
            continue
        queue = deque([(i,j)])
        a = 1
        visited[i][j] = True
        while queue:
            x,y=queue.popleft()
            for dx, dy in D:
                nx,ny=x+dx, y+dy
                if 0<=nx<S and 0<=ny<S and A[nx][ny] and not visited[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny] = True 
                    a += 1
        area = max(area, a)
        
         
ans =sum([sum(A[i]) for i in range(S)])
print(ans)
print(area if ans else 0)