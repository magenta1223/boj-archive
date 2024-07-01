#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14499                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14499                         #+#        #+#      #+#     #
#     Solved: 2024-02-08 15:20:56 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M,x,y,K=map(int,input().split())
BOARD = [ list(map(int, input().split()))  for _ in range(N)]
COMMANDS = list(map(int, input().split()))
DICE = [0,0,0,0,0,0] # 1 2 3 4 5 6 
# 1 : right, 2 : left, 3 : up, 4 : down
def roll(dice, direction):
        #  2
        #4 1 3
        #  5
        #  6 
    if direction == 1:
        #  2
        #6 4 1
        #  5
        #  3 
        # -> 4 2 1 6 5 3 = 3 1 0 5 4 2 
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif direction == 2:
        #  2
        #1 3 6
        #  5
        #  4 
        # 3 2 6 1 5 4 = 2 1 5 0 4 3 
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif direction == 3:
        #  1
        #4 5 3
        #  6
        #  2 
        # 5 1 3 4 6 2 
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    else:
        #  6
        #4 2 3
        #  1
        #  5 
        # 2 6 3 4 1 5 
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    return dice 
 
def next_position(x,y,c):
    if c == 1: # right 
        return x, y+1
    elif c == 2:
        return x, y-1
    elif c== 3:
        return x-1, y
    else: # down 
        return x+1, y
 
for c in COMMANDS:
    new_x, new_y = next_position(x,y,c)
    if 0<=new_x<N and 0<=new_y<M:
        DICE = roll(DICE, c)
        # 숫자 변경
        if not BOARD[new_x][new_y]:
            BOARD[new_x][new_y] = DICE[-1]
        else:
            DICE[-1] = BOARD[new_x][new_y]
            BOARD[new_x][new_y] = 0
 
        x, y = new_x, new_y
        
        print(DICE[0])