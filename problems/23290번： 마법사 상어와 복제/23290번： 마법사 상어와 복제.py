#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 23290                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/23290                         #+#        #+#      #+#     #
#     Solved: 2024-10-08 04:23:53 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


"""
4x4 격자에서 연습 
격자에는 총 M마리의 물고기가 있다.

초기 상태는 다음과 같다. 

물고기는
- 한 칸에 한 마리 
- 이동방향이 있음
- 8방이동가능

마법사 상어도 격자 안에 있다.

여러 물고기 및 상어가 한 칸에 있을 수 있다. 

마법 연습은 
1. 모든 물고기에 복제마법을 건다
2. 모든 물고기가 한 칸 이동. 
    - 상어가 있거나
    - 물고기의 냄새가 있거나
    - 격자 바깥
    으로는 이동할 수 없다. 
    이동 가능한 칸을 찾을 때까지 "반시계" 방향으로 45도 회전한다. 
    이동 가능한 칸이 없다면 이동하지 않는다. 
3. 상어는 3칸 연속이동. 
    - 상하좌우 인접한 칸으로 이동 가능. 
    - 연속 이동의 결과가 격자 바깥이라면 그것은 이동 불가임. 
    - 이동과정에서 마주치는 물고기는 격자에서 제외 
    - 제외되는 물고기는 거기에 물고기 냄새를 남긴다. 
    - 가장 많은 물고기를 제외하도록 움직인다. 
    - 여러가지라면 "사전순으로 가장 앞서는" 방법으로 움직인다. 
4. 2턴 전의 물고기 냄새가 사라진다. 
5. 남은 물고기들을 복제함. 

구현 할 것
1. 물고기의 이동
2. 물고기의 냄새 남기기
3. 상어의 이동
4. 물고기의 제외 
5. 물고기 냄새 1턴 감소 
6. 물고기 복제 

계획
1. 물고기 격자를 만들어서 id를 부여함.
2. 몰고기 index로 방향을 조회하는 dict
3. 물고기 냄새의 잔여 턴 수를 다루는 격자 
4. 방향 회전 함수
"""



def move_fishes():
    for fid in getFish.keys():
        x, y, d = getFish[fid]
        dx, dy,orig_d = *D[d],d
        for _ in range(8):
            nx, ny = x+dx, y+dy 
            if 0<=nx<4 and 0<=ny<4 and (nx,ny) != (sx, sy) and not Scent[nx][ny]:
                break 
            else:
                d = (d-1)%8 
                dx, dy = D[d]
        else: # 이동 불가. 
            nx,ny = x,y 
            d = orig_d
        tmpArr[nx][ny].append(fid)
        getFish[fid] = nx,ny,d
    
def move_shark():
    global sx, sy 
    mx = -1
    for dx1, dy1 in DS:
        nx1, ny1 = sx+dx1, sy+dy1
        if not (0<=nx1<4 and 0<=ny1<4):
            continue 
        for dx2, dy2 in DS:
            nx2, ny2 = nx1+dx2, ny1+dy2 
            if not (0<=nx2<4 and 0<=ny2<4):
                continue 
            for dx3, dy3 in DS:
                nx3, ny3 = nx2+dx3, ny2+dy3
                if not (0<=nx3<4 and 0<=ny3<4):
                    continue 
                _path = [(nx1, ny1), (nx2, ny2), (nx3, ny3)]
                cnt = sum([len(tmpArr[_x][_y]) for _x, _y in set(_path)]) # 중복카운트 방지 
                if cnt > mx:
                    mx = cnt 
                    path = _path

    for _x, _y in path:
        if tmpArr[_x][_y]:
            for fid in tmpArr[_x][_y]:
                del getFish[fid]
            tmpArr[_x][_y] = []
            Scent[_x][_y] = 3 
    sx, sy = path[-1]

def remove_scent():
    for i in range(4):
        for j in range(4):
            if Scent[i][j]:
                Scent[i][j] -= 1 

def copy_fishes():
    global tmpArr, A 
    # 움직이기 전의 상태가 카피됨.  
    for i,fid in enumerate(tmpFish.keys()):
        x,y,d = tmpFish[fid]
        getFish[mx+i] = (x,y,d) 
        tmpArr[x][y].append(mx+i)
    A = tmpArr 


D = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]
DS = [(-1,0), (0,-1), (1,0), (0,1)]

M,S = map(int, input().split())
A = [[[]  for _ in range(4)] for _ in range(4)]
getFish = dict() 
Scent = [[0] * 4 for _ in range(4)]
for i in range(1,M+1):
    fx, fy, d = map(int, input().split())
    A[fx-1][fy-1].append(i) 
    getFish[i] = (fx-1, fy-1, d-1)
sx, sy = map(int, input().split())
sx, sy = sx-1, sy-1 

for i in range(S):
    mx = max(getFish.keys())+1
    tmpFish = {**getFish}
    tmpArr = [[[] for _ in range(4)] for _ in range(4)]    
    move_fishes()
    move_shark()
    remove_scent()
    copy_fishes()
print(len(getFish.keys()))

    
