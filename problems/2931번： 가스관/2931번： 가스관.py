#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2931                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2931                          #+#        #+#      #+#     #
#     Solved: 2024-02-29 00:05:03 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M = map(int, input().split()) 
B = [list(input().strip()) for _ in range(N)]
 
for i in range(N):
    for j in range(M):
        if B[i][j] == "M":
            start = (i,j)
        elif B[i][j] == "Z":
            end = (i,j)
 
# 관의 종류에 따라 흐르는 방법이 다름. 
# 현재 나가는 방향을 고려, 
 
D = [(-1,0), (0,1), (1,0), (0,-1)]
# U R D L
# 각 블록별 in / out 
blocks = {
    '|' : {0:0, 2:2},
    '-' : {1:1, 3:3},
    '+' : {0:0,1:1,2:2,3:3},
    '1' : {3:2,0:1},
    '2' : {2:1,3:0},
    '3' : {1:0,2:3},
    '4' : {0:3,1:2}
}
 
blocks_reverse = {
    0: {1:"4", 2 : '|', 3 : "1"},
    1: {0:"4", 2 : '3', 3 : "-"},
    2: {0:'|' , 1: '3', 3:'2'},
    3: {0:'1' , 1: '-' , 2:'2'},
}
 
 
 
def find_missing(x,y):
    B[x][y] = '.'
    for i, (dx, dy) in enumerate(D):
        nx, ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<M and B[nx][ny] in blocks.keys():
            block,d = B[nx][ny], i
            break 
    # 빈 공간이 나올때까지 ㄱㄱ 
    while B[nx][ny] != ".":
        if B[nx][ny] == "+":
            B[nx][ny] = '|' if d % 2 else '-' # 현재 가로 -> 가로는 못씀. 세로만 남기기  
        else: 
            B[nx][ny] = '.' 
        d = blocks[block][d]
        dx, dy = D[d]
        nx, ny = nx+dx, ny+dy
        block = B[nx][ny] 
    return nx, ny, d
 
x, y, dm = find_missing(*start)
_, _, dz = find_missing(*end)
 
 
if all([ B[i][j] == '.' for i in range(N) for j in range(M)]):
    print(x+1, y+1, blocks_reverse[dm][dz])
else:
    print(x+1, y+1, '+')