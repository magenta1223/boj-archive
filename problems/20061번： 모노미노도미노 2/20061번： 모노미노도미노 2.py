#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 20061                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/20061                         #+#        #+#      #+#     #
#     Solved: 2024-02-20 14:16:10 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline
 
BLUE  = [[0] * 6 for _ in range(4)]
GREEN = [[0] * 4 for _ in range(6)]
N=int(input().strip())
score = 0
T = {1:1, 2:3, 3:2}
 
flip = lambda board: [list(row) for row in zip(*board)]
 
def stack(board, t, y):
    for i in range(6):
        if t == 1 and board[i][y]:
            i-=1
            break 
        elif t == 2 and (board[i][y] or board[i][y+1]):
            i-=1
            break
        elif t == 3 and i>0 and (board[i-1][y] or board[i][y]):
            i-=1
            break 
    if t == 1:
        board[i][y] = 1
    elif t == 2:
        board[i][y] = 1
        board[i][y+1] = 1
    else:
        board[i-1][y] = 1
        board[i][y] = 1
    return board 
 
def stack_green(board,t,x,y):
    board = stack(board, t, y)
    return board 
 
def stack_blue(board, t,x,y):
    return flip(stack_green(flip(board),T[t],y,x))
 
def tetris(board):
    board = [row for row in board if sum(row) != 4]
    score = 6-len(board)
    board = [[0] * 4 for _ in range(score)] + board
    for _ in range(2):
        if sum(board[1]):
            board =  [[0] * 4] + board[:-1]
    return score, board
 
def score_green(board):
    return tetris(board)
 
def score_blue(board):
    score, board = tetris(flip(board))
    return score, flip(board)
 
flip(GREEN)
 
score = 0
for _ in range(N):
    t, x, y = map(int,input().split())
    # 각 보드로 블록 보내기 
    GREEN = stack_green(GREEN, t, x, y)
    BLUE  = stack_blue(BLUE,  t, x, y)
    # print('-------------------- 블록 보내기 ---------------------- ')
    # print('--------GREEN')
    # print(*GREEN, sep='\n')
    # print('--------BLUE')
    # print(*BLUE, sep='\n')
    # 점수, 01처리 
    sg, GREEN = score_green(GREEN)
    sb, BLUE  = score_blue(BLUE)
    score += sg + sb
    # print('-------------------- 테트리스 ---------------------- ')
    # print('--------GREEN')
    # print(*GREEN, sep='\n')
    # print('--------BLUE')
    # print(*BLUE, sep='\n')
 
print(score, sum([sum(GREEN[i]) for i in range(6)]) + sum([sum(BLUE[i]) for i in range(4)]), sep = '\n')