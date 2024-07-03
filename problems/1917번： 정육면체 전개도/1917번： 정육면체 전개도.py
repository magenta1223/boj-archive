#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1917                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1917                          #+#        #+#      #+#     #
#     Solved: 2024-07-03 08:15:50 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# A가 전개도인지 아닌지 

# 가장 왼쪽 위 칸을 Up으로 설정하고 시작 
# 그리고 인접한 칸을 찾는다. 

# 이전에 온 곳과 그 방향에 따라 인접한 곳의 위치가 달라짐
# U-D, L-R, F-B로 구성

# U-R에서
# 직진: D
# 우회전:F
# 좌회전:B 

# 각 사이드의 직전 방향, 현재 방향을 알면 회전 여부를 알 수 있고 
# 그에 따라서 다음 칸도 알 수 있다. 

def calc(dx1, dy1, dx2, dy2):
    if dx1 == dx2 and dy1 == dy2:
        return "forward"
    elif dx1:
        return "left" if dx1==dy2 else "right" 
    elif dy1:
        return "right" if dy1==dx2 else "left" 

pairs = {
    "U" : "D",
    "D" : "U",
    "L" : "R",
    "R" : "L",
    "F" : "B",
    "B" : "F"
}

nextCell = {
    "U" : {
        "L" : {"forward":"R","left":"B","right":"F"},
        "F" : {"forward":"B","left":"L","right":"R"},
    },
    "F" :{
        "U" : {"forward":"D","left":"R","right":"L"},
        "L" : {"forward":"R","left":"U","right":"D"},
    }, 
    "L" :{
        "U" : {"forward":"D","left":"F","right":"B"},
        "F" : {"forward":"B","left":"D","right":"U"},
    },
    # "R" : {
    #     "U" : {"forward":"D","left":"B","right":"F"},
    #     "D" : {"forward":"U","left":"F","right":"B"},
    #     "F" : {"forward":"B","left":"U","right":"D"},
    #     "B" : {"forward":"F","left":"D","right":"U"},
    # },
}

allSides = set(pairs.keys())
for k in ["U", "F", "L"]:
    pair = pairs[k]
    targets = allSides - set([k, pair])
    for t in targets:
        if t not in nextCell[k]:
            pairT = pairs[t]
            nextCell[k][t] = {
                "forward" : pairT,
                "left" : nextCell[k][pairT]['right'], 
                "right" :nextCell[k][pairT]['left']
            }

for k in ['D', "B", "R"]:
    pair = pairs[k]
    targets = allSides - set([k, pair])
    # pair를 가져와서 lr만 바꾸면 됨 
    nextCell[k] = {t : {} for t in targets}
    for t in targets:
        nextCell[k][t]['forward'] = nextCell[pair][t]['forward']
        nextCell[k][t]['left'] = nextCell[pair][t]['right']
        nextCell[k][t]['right'] = nextCell[pair][t]['left']

from collections import deque 

def solve(arr):
    # 2. 인접셀을 찾고, 아래면 D, 오른쪽이면 R로 설정
    # 3. 칸 위치, 현재 칸 이름 (U), 이동방향을 함께 넘긴다. 
    cells = {k : 0 for k in pairs.keys()}
    
    visited = [[False] * 6 for _ in range(6)]

    # 1. top-left cell을 찾아서 U로 설정한다. 
    find = False 
    for i in range(6):
        for j in range(6):
            if arr[i][j]:
                x,y = i,j 
                visited[x][y] = True 
                cells["U"] = 1 
                find = True 
                break 
        if find:
            break 
    # 2. 인접셀을 찾고, 아래면 D, 오른쪽이면 R로 설정
    q = deque([])
    if arr[x+1][y]:
        # 3. 칸 위치, 현재 칸 이름 (U), 이동방향을 함께 넘긴다. 
        visited[x+1][y] = True 
        cells['F'] = 1
        q.append((x+1,y,"U","F",1,0))
    if y+1 < 6 and arr[x][y+1]:
        visited[x][y+1] = True 
        cells['R'] = 1
        q.append((x,y+1,"U","R",0,1))

    # 큐 시작
    # 1. 인접 칸을 찾고
    # 2. 이전 이동방향과 현재 이동방향을 고려, 방향 회전을 알아냄
    # 3. 현재 칸 이름, 이전 칸 이름, 회전 여부를 고려해 다음 칸을 알아낸다. 
    # 4. 중복이라면 실패처리
    # 5. 다 차지 않았다면 실패처리
    while q:
        x,y,prev,now,pdx,pdy = q.popleft()
        # print(x,y,now)
        for dx, dy in D:
            nx,ny = x+dx, y+dy 
            direction = calc(pdx,pdy,dx,dy)
            if not 0<=nx<6 or not 0<=ny<6:
                continue 

            if arr[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                # nx,ny가 해당하는 면의 이름 
                next = nextCell[now][prev][direction]
                cells[next] += 1 
                # print("--",next, nx,ny, direction)
                q.append((nx,ny,now,next,dx,dy))

    # print(cells)
    ans = "yes"  if all([v == 1 for v in cells.values()]) else "no"
    return ans

D = [(-1,0),(0,1),(1,0),(0,-1)]

for _ in range(3):
    A = [list(map(int,input().split())) for _ in range(6)]
    print(solve(A))
