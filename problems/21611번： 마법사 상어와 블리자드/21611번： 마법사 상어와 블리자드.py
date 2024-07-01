#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 21611                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/21611                         #+#        #+#      #+#     #
#     Solved: 2024-03-25 15:48:24 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 21611                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: magenta1223 <boj.kr/u/magenta1223>          +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/21611                          #+#        #+#      #+#     #
#    Solved: 2024/03/25 15:48:08 by magenta1223   ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import Counter 
N,M=map(int,input().split())
B=[list(map(int,input().split())) for _ in range(N)]
COMMANDS = [list(map(int,input().split())) for _ in range(M)]
 
D=[(0,-1),(1,0),(0,1),(-1,0)]
# 0. linked list를 만들어야 함.
# 중앙에서 왼쪽보고 시작
# 1번 꺾을 때 마다 방향이 반시계로 돌고
# 2번 꺾을 때 마다 거리가 1씩 는다.
x,y,d,l,c,n = N//2, N//2,0,1,0,0
G = { 0:{'pos' : [x,y], 'adj' : []}}
while True:
    dx, dy = D[d%4]
    for _ in range(l):
        nx,ny = x+dx, y+dy
        if (nx,ny) == (0,-1):
            x, y = nx, ny
            break
        G[n]['adj'].append((nx,ny))
        n+=1
        G[n] = {'pos' : [nx,ny], 'adj' : [(x, y)]}
        x,y = nx, ny
    d+=1
    
    if not d % 2:
        l+=1
    if (x,y) == (0,-1):
        break
 
D=[(-1,0),(1,0),(0,-1),(0,1)]
# 1. 블리자드
def blizzard(d,s):
    x, y = N//2, N//2
    dx, dy = D[d]
    for i in range(1, s+1):
        B[x+i*dx][y+i*dy]=0
        
# 2. 움직이기 
def move():
    idx = 2
    while idx < N**2-1:
        x,y = G[idx]['pos']
        if not B[x][y]:
            idx += 1
            continue
        back = 1
        while True:
            try:
                prev_x, prev_y = G[idx-back]['pos']
            except:
                assert 1==0, f"{idx}, {back}"
            if B[prev_x][prev_y]:
                last_empty_x, last_empty_y = G[idx-back]['adj'][-1]
                break 
            back += 1
        B[x][y], B[last_empty_x][last_empty_y] = 0, B[x][y]
        idx += 1
 
def destroy():
    # 1) 4개이상의 그룹을 모두 찾고
    # 1번 위치부터 시작
    def check(v,x,y):
        return True if v == B[x][y] else False
    idx = 1
    counter = [0,0,0]
    while idx < N**2-1:
        (x,y), adjs = G[idx].values()
        bead = B[x][y]
        if bead:
            group = [(x,y)]
            while idx < N**2-1 and check(bead, *adjs[1]):
                idx += 1
                (x,y), adjs = G[idx].values()
                group.append((x,y))
            if len(group) >= 4:
                # 2) 파괴 
                counter[bead-1] += len(group)
                for x, y in group:
                    B[x][y] = 0
        idx += 1
    return counter, True if not sum(counter) else False
 
def change():
    def check(v,x,y):
        return True if v == B[x][y] else False
    idx = 1
    next_beads = []
    while idx < N**2-1:
        (x,y), adjs = G[idx].values()
        bead = B[x][y]
        if bead:
            group = [(x,y)]
            while idx < N**2-1 and check(bead, *adjs[1]):
                idx += 1
                (x,y), adjs = G[idx].values()
                group.append((x,y))
            # 2) 파괴 
            for x, y in group:
                B[x][y] = 0
            next_beads.extend([len(group), bead]) 
        idx += 1
    # 처음부터 다시 채워넣기 
    for idx in range(1, min(N**2,len(next_beads)+1)):
        x,y=G[idx]['pos']
        B[x][y] = next_beads[idx-1]
    
ans = 0 
B[N//2][N//2] = 9
for d, s in COMMANDS:
    blizzard(d-1,s)
    while True:
        move()
        counter, stop_destroy = destroy()
        if stop_destroy:
            break 
        for i, v in enumerate(counter):
            ans += (i+1)*v        
    change()
    move()
print(ans)