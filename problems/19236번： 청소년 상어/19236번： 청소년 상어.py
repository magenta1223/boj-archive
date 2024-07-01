#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 19236                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/19236                         #+#        #+#      #+#     #
#     Solved: 2024-02-20 17:01:17 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from copy import deepcopy
 
BOARD = []
fishes = dict()
for i in range(4):
    l = list(map(int,input().split()))
    row = []
    for j in range(4):
        n, d = l[j*2:j*2+2]
        row.append(n)
        fishes[n] = (i,j,d-1)
    BOARD.append(row)
    
D = [(-1,0),(-1,-1), (0,-1),(1,-1), (1,0), (1,1), (0,1),(-1,1)]
 
def move_fish(shark, fishes, board):
    sx, sy, _ = shark 
    for i in sorted(fishes.keys()):
        x,y,d = fishes[i]
        for j in range(8):
            dx, dy = D[(d+j)%8]
            nx, ny = x+dx, y+dy
            if (nx,ny) == (sx,sy):
                continue 
            if 0<=nx<4 and 0<=ny<4:
                if board[nx][ny]: # swap
                    swap_fish = board[nx][ny]
                    _,_,swap_d = fishes[swap_fish]
                    fishes[i] = nx, ny, (d+j)%8
                    fishes[swap_fish] = x,y,swap_d
                    board[x][y] = swap_fish
                    board[nx][ny] = i
                else: # 빈칸으로 이동하기 
                    fishes[i] = nx, ny, (d+j)%8
                    board[x][y] = 0
                    board[nx][ny] = i
                break 
    return fishes, board
 
def eat(x,y, board, fishes, score):
    fish_idx = board[x][y]
    _x, _y, d = fishes.pop(fish_idx)
    assert (x,y) == (_x,_y), f"{x,y} vs {_x,_y}"
    shark = x,y,d
    board[x][y] = 0
    return shark, board, fishes, score + fish_idx
 
 
ans = 0
 
def dfs(shark, fishes, board, score):
    global ans
    x, y = shark
    shark, board, fishes, score = eat(x,y,board, fishes, score)
    ans = max(score, ans)
    
    fishes, board = move_fish(shark, fishes, board)
    x, y, d = shark
    dx, dy = D[d]
    nx, ny = x+dx, y+dy
    while 0<=nx<4 and 0<=ny<4:
        if board[nx][ny]:
            dfs((nx, ny), deepcopy(fishes), deepcopy(board), score)
        nx, ny = nx+dx, ny+dy
dfs((0,0), fishes, BOARD, 0)
print(ans)