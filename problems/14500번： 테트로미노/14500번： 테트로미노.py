#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14500                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14500                         #+#        #+#      #+#     #
#     Solved: 2024-02-11 20:04:54 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M=map(int,input().split())
BOARD = [list(map(int, input().split())) for _ in range(N)]
def I(x,y,rot):
    v = []
    # ignore flip
    # rot = 0,1
    if rot == 0:
        if y+3<M:
            v = [BOARD[x][y], BOARD[x][y+1], BOARD[x][y+2], BOARD[x][y+3]]
    else :
        if x+3<N:
            v = [BOARD[x][y], BOARD[x+1][y], BOARD[x+2][y], BOARD[x+3][y]]
    return sum(v)
 
def O(x,y):
    v = []
    # ignore flip, rot
    if x+1<N and y+1<M:
        v = [BOARD[x][y], BOARD[x][y+1], BOARD[x+1][y], BOARD[x+1][y+1]]
    return sum(v)
 
def L(x,y,rot):
    return max(_L(x,y,rot), _L_flip(x,y,rot))
 
def _L(x,y,rot):
    v = []
    # 
    if rot == 0:
        if x+2<N and y+1<M:
            v = [BOARD[x][y], BOARD[x+1][y], BOARD[x+2][y], BOARD[x+2][y+1]]
    elif rot == 1:
        if x+1<N and y-2>=0:
            v = [BOARD[x][y], BOARD[x][y-1], BOARD[x][y-2], BOARD[x+1][y-2]]
    elif rot == 2:
        if x-2>=0 and y-1>=0:
            v = [BOARD[x][y], BOARD[x-1][y], BOARD[x-2][y], BOARD[x-2][y-1]]
    else :
        if x-1>=0 and y+2<M:
            v = [BOARD[x][y], BOARD[x][y+1], BOARD[x][y+2], BOARD[x-1][y+2]]
    return sum(v)
 
def _L_flip(x,y,rot):
    # 
    v = []
    if rot == 0:
        if x+2<N and y-1>=0:
            v = [BOARD[x][y], BOARD[x+1][y], BOARD[x+2][y], BOARD[x+2][y-1]]
    elif rot == 1:
        if x-1>=0 and y-2>=0:
            v = [BOARD[x][y], BOARD[x][y-1], BOARD[x][y-2], BOARD[x-1][y-2]]
    elif rot == 2:
        if x-2>=0 and y+1<M:
            v = [BOARD[x][y], BOARD[x-1][y], BOARD[x-2][y], BOARD[x-2][y+1]]
    else :
        if x+1<N and y+2<M:
            v = [BOARD[x][y], BOARD[x][y+1], BOARD[x][y+2], BOARD[x+1][y+2]]
    return sum(v)
 
def S(x,y,rot):
    return max(_S(x,y,rot), _S_flip(x,y,rot))
 
def _S(x,y,rot):
    # rot=2,3은 할 필요가 없음. 
    v = []
    if rot == 0:
        if x+2<N and y+1<M:
            v = [BOARD[x][y], BOARD[x+1][y], BOARD[x+1][y+1], BOARD[x+2][y+1]]
    elif rot == 1:
        if x+1<N and y-2>=0:
            v = [BOARD[x][y], BOARD[x][y-1], BOARD[x+1][y-1], BOARD[x+1][y-2]]
    # elif rot == 2:
    #     if x-2>=0 and y-1>=0:
    #         v = [BOARD[x][y], BOARD[x-1][y], BOARD[x-1][y-1], BOARD[x-2][y-1]]
    # else :
    #     if x-1>=0 and y+2<M:
    #         v = [BOARD[x][y], BOARD[x][y+1], BOARD[x-1][y+1], BOARD[x-1][y+2]]
    return sum(v)
    
def _S_flip(x,y,rot):
    v = []
    if rot == 0:
        if x+2<N and y-1>=0:
            v = [BOARD[x][y], BOARD[x+1][y], BOARD[x+1][y-1], BOARD[x+2][y-1]]
    elif rot == 1:
        if x-1>=0 and y-2>=0:
            v = [BOARD[x][y], BOARD[x][y-1], BOARD[x-1][y-1], BOARD[x-1][y-2]]
    # elif rot == 2:
    #     if x-2>=0 and y+1<M:
    #         v = [BOARD[x][y], BOARD[x-1][y], BOARD[x-1][y+1], BOARD[x-2][y+1]]
    # else :
    #     if x+1<N and y+2<M:
    #         v = [BOARD[x][y], BOARD[x][y+1], BOARD[x+1][y+1], BOARD[x+1][y+2]]
    return sum(v)
 
def T(x,y,rot):
    # 
    v = []
    if rot == 0:
        if x+1<N and y+2<M:
            v = [BOARD[x][y], BOARD[x][y+1], BOARD[x][y+2], BOARD[x+1][y+1]]
    elif rot == 1:
        if x+2<N and y-1>=0:
            v = [BOARD[x][y], BOARD[x+1][y], BOARD[x+2][y], BOARD[x+1][y-1]]
    elif rot == 2:
        if x-1>=0 and y-2>=0:
            v = [BOARD[x][y], BOARD[x][y-1], BOARD[x][y-2], BOARD[x-1][y-1]]
    else:
        if x-2>=0 and y+1<M:
            v = [BOARD[x][y], BOARD[x-1][y], BOARD[x-2][y], BOARD[x-1][y+1]]
    return sum(v)
 
def check(x, y):
    Is = [I(x,y,0), I(x,y,1)]
    Os = [O(x,y)]
    Ls = [L(x,y,i) for i in range(4)]
    Ss = [S(x,y,i) for i in range(2)]
    Ts = [T(x,y,i) for i in range(4)]
    return max(Is + Os + Ls + Ss + Ts)
 
max_tetromino = 0
for i in range(N):
    for j in range(M):
        now_max = check(i,j)        
        if now_max > max_tetromino:
            max_tetromino = now_max
print(max_tetromino)