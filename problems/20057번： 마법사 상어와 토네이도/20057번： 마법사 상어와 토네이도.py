#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 20057                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/20057                         #+#        #+#      #+#     #
#     Solved: 2024-02-21 18:29:01 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

trunc = lambda x, percentage: int(x * percentage) 
 
def move(nx, ny, p, sand):
    moved, overflowed = 0,0 
    _sand = trunc(sand, p)    
    if 0<=nx<N and 0<=ny<N:
        A[nx][ny] += _sand
        moved = _sand
    else:
        overflowed = _sand
    return moved, overflowed
 
def tornado(x,y,d):
    # toward, left, right 
    (tx, ty), (lx, ly), (rx, ry) = D[d], D[(d+1)%4], D[(d-1)%4]
    sand = A[x+tx][y+ty]
    A[x+tx][y+ty] = 0
    # moved, overflowed 
    m, o = 0, 0    
    locs=[(x+lx, y+ly, 0.01), (x+lx+tx, y+ly+ty, 0.07), (x+2*lx+tx, y+2*ly+ty, 0.02), (x+lx+2*tx, y+ly+2*ty, 0.1),
          (x+rx, y+ry, 0.01), (x+rx+tx, y+ry+ty, 0.07), (x+2*rx+tx, y+2*ry+ty, 0.02), (x+rx+2*tx, y+ry+2*ty, 0.1),
          (x+3*tx, y+3*ty, 0.05)]
 
    for nx, ny, p in locs:
        dm, do = move(nx, ny, p, sand)
        m, o = m+dm, o+do
    
    nx, ny = x+2*tx, y+2*ty
    if 0<=nx<N and 0<=ny<N:    
        A[x+2*tx][y+2*ty] += sand - o - m
        m = sand - o
    else:
        o = sand - m
    return o
 
N=int(input().strip())
A=[list(map(int,input().split())) for _ in range(N)]
start = (N//2, N//2)
 
# 2번 꺾을 때마다 거리가 1씩 커지고
# 방향은 반시계방향 
D = [(0,-1),(1,0), (0,1), (-1,0)]
l,c,t,d,ans = 1,0,0,0,0
while start != (0,-1):
    dx, dy = D[d]
    if c == 2:
        c = 0
        l += 1
    x, y = start
    for _ in range(l):
        overflowed = tornado(x,y,d)
        ans += overflowed
        x,y=x+dx,y+dy 
        if (x,y) == (0,-1):
            break
    start = (x,y)    
    c += 1
    t += 1
    d = (d+1) % 4
print(ans)