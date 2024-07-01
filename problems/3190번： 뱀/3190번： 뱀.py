#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 3190                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/3190                          #+#        #+#      #+#     #
#     Solved: 2024-02-08 14:02:15 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
def parse(x,c):
    return int(x), c
def move_to(x,y,direction):
    if direction == 'left':
        new_x, new_y = x-1,y
    elif direction == 'right':
        new_x, new_y = x+1, y
    elif direction == 'down':
        new_x, new_y = x, y-1
    else:
        new_x, new_y = x, y+1
    
    return new_x, new_y
 
ROT = {
    'left' : {
        'L' : 'down',
        'D' : 'up',
    },
    'right' : {
        'L' : 'up',
        'D' : 'down',
    },
    'up' : {
        'L' : 'left',
        'D' : 'right',
    },
    'down' : {
        'L' : 'right',
        'D' : 'left',
    },
}
N=int(input().strip())
K=int(input().strip())
APPLES=[list(map(int, input().split())) for _ in range(K)]
L=int(input().strip())
COMMANDS=deque([parse(*input().split()) for _ in range(L)])
WALL = 9
A = 2
BODY = 1
# initialize board 
BOARD = [ [0] * (N+2)  for _ in range(N+2)]
BOARD[0] = [WALL] * (N+2) 
BOARD[-1] = [WALL] * (N+2)
for i in range(1,N+1):
    BOARD[i][0] = WALL
    BOARD[i][-1] = WALL
# place apples 
for x,y in APPLES:
    BOARD[x][y] = A
# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
x,y,l = 1,1,1
t = 0
direction = 'up'
snakes = deque([(1,1)])
BOARD[1][1] = BODY
while True:    
    if COMMANDS and COMMANDS[0][0] == t:
        _, c = COMMANDS.popleft()
        direction = ROT[direction][c]
    
    # direction대로 이동 
    x, y = move_to(x,y,direction)
    # 종료조건을 만족하는지? 
    if BOARD[x][y] in [BODY, WALL]:
        break 
    # 지도에 칠한다
    if BOARD[x][y] != A:
        tail_x, tail_y = snakes.popleft()
        BOARD[tail_x][tail_y] = 0
    BOARD[x][y] = BODY
    snakes.append((x,y))
    t += 1
    
print(t+1)    