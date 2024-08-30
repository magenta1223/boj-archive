#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 16985                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/16985                         #+#        #+#      #+#     #
#     Solved: 2024-08-30 01:05:09 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


from itertools import permutations 
from collections import deque 

D = [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]

def rotate(arr, deg):
    def _rotate(arr):
        tmp = [[0]*5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                tmp[4-j][i] = arr[i][j]
        return tmp 
    for _ in range(deg):
        arr = _rotate(arr)
    return arr 

def getRotations(x):
    rotations = []
    for _ in range(5):
        if x>=4:
            x,r = divmod(x,4)
            rotations.append(r) 
        else:
            rotations.append(x)
            x=0
    return tuple(rotations)

check = lambda x,y,z: (0<=x<5 and 0<=y<5 and 0<=z<5) 

def bfs(cube, start, end):
    x,y,z = start
    tx,ty,tz = end 

    if not cube[x][y][z] or not cube[tx][ty][tz]:
        return -1 

    visited = [[[-1] * 5 for _ in range(5)] for _ in range(5)]
    visited[x][y][z] = 0 
    q = deque([(x,y,z,0)])
    done = False 
    while q and not done:
        x,y,z,t = q.popleft()
        for dx,dy,dz in D:
            nx,ny,nz = x+dx,y+dy,z+dz 
            if check(nx,ny,nz) and visited[nx][ny][nz]==-1 and cube[nx][ny][nz]:
                visited[nx][ny][nz] = t+1 
                q.append((nx,ny,nz,t+1)) 
                if (nx,ny,nz) == end:
                    done = True 
                    break 

    return visited[tx][ty][tz]


A = [[list(map(int, input().split()))  for _ in range(5)] for _ in range(5)]

ROTATIONS=[]
for i in range(5):
    ROTATIONS.append([rotate(A[i], deg) for deg in range(4)])


rotations = set([getRotations(i) for i in range(1024)])
INOUT = [
    ((0,0,0), (4,4,4)),
    ((0,0,4), (4,4,0)),
    ((0,4,0), (4,0,4)),
    ((4,0,0), (0,4,4)),
]

ans = float("inf")
done = False
for perm in permutations(range(5),5):
    for rot in rotations:
        arrs = [ROTATIONS[i][rot[i]] for i in perm]
        # 선택가능한 모든 입구를 찾고 
        for inCoords, outCoords in INOUT:
            t = bfs(arrs,inCoords,outCoords)
            if t != -1:
                ans = min(ans, t)
            if t == 12:
                done = True
                break 
        if done:
            break 
    if done:
        break 
    
print(ans if ans!=float("inf") else -1)    


