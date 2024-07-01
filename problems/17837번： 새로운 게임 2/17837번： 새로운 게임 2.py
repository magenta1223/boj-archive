#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17837                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17837                         #+#        #+#      #+#     #
#     Solved: 2024-02-19 13:59:14 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

W,R,B=0,1,2
D = [(0,1), (0,-1), (-1,0), (1,0)]
N,K=map(int,input().split())
# B가 맵 바깥과 같은 판정 -> 그냥 board를 B로 둘러버리면 됨
BOARD = [[B] * (N+2)] + [[B]+list(map(int,input().split()))+[B] for _ in range(N)] +[[B] * (N+2)]
BOARD_WITH_PIECES = [[[] for _ in range(N+2)] for _ in range(N+2)]
PIECES = dict()
for k in range(1,K+1):
    x, y, d = map(int,input().split())
    BOARD_WITH_PIECES[x][y].append(k)
    PIECES[k] = (x,y,*D[d-1])
 
def _move(x,y,nx,ny,idx, backward = False):
    pieces = BOARD_WITH_PIECES[x][y][idx:]
    targets = pieces[::-1] if backward else pieces
    for _k in targets:
        BOARD_WITH_PIECES[nx][ny].append(_k)
        _, _, _dx, _dy = PIECES[_k]
        PIECES[_k] = nx, ny, _dx, _dy
    BOARD_WITH_PIECES[x][y] = BOARD_WITH_PIECES[x][y][:idx]
 
t, done = 0, False
while t < 1001 and not done:
    for k in range(1,K+1):
        x,y,dx,dy = PIECES[k]
        nx, ny = x+dx, y+dy
        idx = BOARD_WITH_PIECES[x][y].index(k)
        if BOARD[nx][ny] == W:
            _move(x,y,nx,ny,idx)
        elif BOARD[nx][ny] == R:
            _move(x,y,nx,ny,idx, True)
        else:
            dx, dy = -dx, -dy
            nx, ny = x+dx, y+dy
            if BOARD[nx][ny] == W:
                _move(x,y,nx,ny,idx,)
            elif BOARD[nx][ny] == R:
                _move(x,y,nx,ny,idx, True)
            else:
                nx, ny = x, y
        PIECES[k] = nx, ny, dx, dy
        if len(BOARD_WITH_PIECES[nx][ny]) > 3:
            done = True
            break     
    t += 1
print(-1 if t > 1000 else t)