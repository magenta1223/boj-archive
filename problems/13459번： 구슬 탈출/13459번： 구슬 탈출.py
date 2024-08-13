#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 13459                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/13459                         #+#        #+#      #+#     #
#     Solved: 2024-08-13 02:11:58 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 빨간구슬을 넣고
# 파란구슬은 넣으면 안됨
# 이게 10step안에 가능하냐? 

# 일단 시뮬레이션을 돌려볼까용 
# 구슬의 위치
# 구슬의 이동 

from collections import deque

input = open(0).readline 
D = [(-1,0), (0,1), (1,0), (0,-1)]
N,M = map(int, input().split())
A = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if A[i][j] == "B":
            bx,by = i,j
            A[i][j] = '.'
        elif A[i][j] == "R":
            rx,ry = i,j
            A[i][j] = '.'
        elif A[i][j] == "O":
            H = i,j

def _move(x,y,dx,dy):
    while A[x+dx][y+dy] != "#" and A[x][y] != "O":
        x+=dx 
        y+=dy 
    return x,y 

def move(bx,by,rx,ry,dx,dy):
    nbx,nby = _move(bx,by,dx,dy)
    nrx,nry = _move(rx,ry,dx,dy)
    
    # 다르면 상관 없음 
    if (nbx,nby) != (nrx,nry):
        return nbx, nby, nrx, nry
    
    # 같은데 구멍에 빠짐 -> 밖에서 불가 처리
    if (nbx,nby) == H:
        return nbx, nby, nrx, nry
    
    # 같은데 구멍이 아님. 진행방향에서 먼 구슬을 나중에 움직인 형태가 되도록 처리 
    if dx:
        if bx*dx>rx*dx:
            nrx -= dx 
        else:
            nbx -= dx  
    else:
        if by*dy>ry*dy:
            nry -= dy 
        else:
            nby -= dy  
    return nbx, nby, nrx, nry

visited = [[False] * (N*M) for _ in range(N*M)] 
visited[bx*M+by][rx*M+ry] = True 
t, done = 0, False  
q = deque([(bx,by,rx,ry,t)])

while q and t < 10 and not done:
    bx,by,rx,ry,t = q.popleft()
    
    for dx, dy in D:
        nbx, nby, nrx, nry = move(bx,by,rx,ry,dx,dy) 

        if (nbx,nby) == H:
            continue 
    
        if not visited[nbx*M+nby][nrx*M+nry]:
            visited[nbx*M+nby][nrx*M+nry] = True 
            q.append((nbx, nby, nrx, nry, t+1))
            if (nrx,nry) == H:
                done = True

print(1 if done else 0)

