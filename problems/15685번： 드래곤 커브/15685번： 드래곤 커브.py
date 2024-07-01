#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 15685                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/15685                         #+#        #+#      #+#     #
#     Solved: 2024-02-14 17:58:38 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input().strip())
CURVES = [list(map(int,input().split())) for _ in range(N)]
BOARD = [[False] * (100+1) for _ in range(100+1)]
D = [(1,0), (0,-1), (-1,0), (0,1)]
def dragon_curve(curve, directions):
    """
    커브의 각 좌표와 방향 list를 받는다.
    끝점부터 역으로 그려나가면 됨
    이전 방향을 90도 반시계방향으로 회전 
    """
    next_directions = []
    for i in range(len(directions)):
        x, y = curve[-1]
        dx, dy = directions[-i-1]
        curve.append((x+dy, y-dx))
        next_directions.append((dy, -dx))
    return curve, directions + next_directions
 
for x,y,d,g in CURVES:
    dx, dy = D[d]
    curve, directions = [(x,y)], [(dx, dy)]
    curve.append((x+dx, y+dy))
    for i in range(g):
        curve, directions = dragon_curve(curve, directions)
    for x, y in curve:
        BOARD[x][y] = True
ans = 0
for i in range(100):
    for j in range(100):
        if all([BOARD[i][j], BOARD[i][j+1], BOARD[i+1][j], BOARD[i+1][j+1]]):
            ans += 1
print(ans)