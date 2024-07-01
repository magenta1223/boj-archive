#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 15683                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/15683                         #+#        #+#      #+#     #
#     Solved: 2024-02-13 17:37:06 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M=map(int, input().split())
ROOM=[list(map(int,input().split())) for _ in range(N)]
# CCTV는 최대 8개를 넘지 않음. 
# -> 4^8 = 2^16 = 65536 = 65K
# 시간 넉넉함. 
D = [(1,0), (-1,0), (0,1), (0,-1)]
 
def _fill(room, x,y, direction):
    dx, dy = direction
    while 0<=x+dx<N and 0<=y+dy<M:
        if room[x+dx][y+dy] != 6:
            room[x+dx][y+dy] = "#"
            x+=dx
            y+=dy
        else:
            break     
    return room 
 
def fill(room, x, y, cctv, direction):
    dx,dy = direction
    room = _fill(room, x, y, direction)
    if cctv == 2:
        room = _fill(room, x, y, [-dx, -dy])
    elif cctv == 3:
        # 90도 회전한 방향 = 현재 방향을 0으로 만들고, 다른 방향을 + 1
        room = _fill(room, x, y, [dy, -dx])
    elif cctv >= 4:
        room = _fill(room, x, y, [dy, -dx])
        room = _fill(room, x, y, [-dy, dx])
        if cctv == 5:
            room = _fill(room, x, y, [-dx, -dy])
    return room 
 
CCTVS = []
for i in range(N):
    for j in range(M):
        if 0<ROOM[i][j]<6:
            CCTVS.append((i,j,ROOM[i][j]))
CCTVS_DIR = []
def solve(room):
    return sum([1 for i in range(N) for j in range(M) if room[i][j] == 0])
ANS=float("inf")
D = {
    1 : [(1,0), (-1,0), (0,1), (0,-1)],
    2 : [(1,0), (0,1)],
    3 : [(1,0), (-1,0), (0,1), (0,-1)],
    4: [(1,0), (-1,0), (0,1), (0,-1)],
    5: [(1,0)]
}
def dfs(room, depth):
    global ANS
    if depth == len(CCTVS):
        for x, y, cctv, direction in CCTVS_DIR:
            room = [[room[i][j] for j in range(M)] for i in range(N)]
            room = fill(room, x,y,cctv, direction)
        s = solve(room)
        if ANS > s:
            ANS = s
        return 
    x,y,cctv = CCTVS[depth]
    for direction in D[cctv]:
        CCTVS_DIR.append((x,y,cctv,direction))
        dfs(room, depth+1)
        CCTVS_DIR.pop()
dfs(ROOM, 0)
print(ANS)