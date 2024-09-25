#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1938                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1938                          #+#        #+#      #+#     #
#     Solved: 2024-09-25 05:34:35 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 이거 왜이럼 
# 회전할 때는 중심 기준 3x3 안에 벽이 없어야 함. 
# 

from collections import deque 

def parse(block):
    # 1->가로, 0-> 세로
    return 1 if all([block[0][0] == b[0] for b in block]) else 0, *block[1] 

def check(d,x,y,func):
    coords = [(x,y-1), (x,y), (x,y+1)] if d else [(x-1,y), (x,y), (x+1,y)]
    cond1 = all([0<=x<N and 0<=y<N and A[x][y] == '0' for x,y in coords])
    if func == turn:
        coords = [(x,y), (x,y-1), (x,y+1), (x-1,y), (x+1,y), (x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1)]
        return cond1 & all([0<=x<N and 0<=y<N and A[x][y] == '0' for x,y in coords])
    else:
        return cond1

def up(d,x,y):
    return d, x-1, y
def down(d,x,y):
    return d, x+1, y
def left(d,x,y):
    return d, x, y-1
def right(d,x,y):
    return d, x, y+1
def turn(d,x,y):
    return abs(d-1), x, y

moves = [up, down, left, right, turn]

N = int (input())
A = [list(input()) for _ in range(N)]

block = []
dst = []
for i in range(N):
    for j in range(N):
        if A[i][j] == 'B':
            block.append((i,j))
            A[i][j] = '0'
        elif A[i][j] == 'E':
            dst.append((i,j))
            A[i][j] = '0'


d_block, x_block, y_block = parse(block)
d_dst, x_dst, y_dst = parse(dst)
visited = [[[0] * N for _ in range(N)] for _ in range(2)]
q = deque([(d_block, x_block, y_block,0)])
while q:
    d,x,y,t = q.popleft()
    for func in moves:
        nd, nx, ny = func(d, x,y)
        if check(nd,nx,ny,func) and not visited[nd][nx][ny]:
            q.append((nd,nx,ny,t+1))
            visited[nd][nx][ny] = t+1  
print(visited[d_dst][x_dst][y_dst])

