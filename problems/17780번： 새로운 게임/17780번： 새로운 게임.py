#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17780                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17780                         #+#        #+#      #+#     #
#     Solved: 2024-05-07 14:18:23 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

D = [(0,1), (0,-1), (-1,0), (1,0)]
N,K = map(int,input().split())
A = [[2] * (N+2)] + [[2] + list(map(int,input().split())) + [2] for _ in range(N)] + [[2] * (N+2)]
B = [[[] for _ in range(N+2)] for _ in range(N+2)]
 
PIECES = dict()
for k in range(1,K+1):
    x,y,d = map(int,input().split())
    dx, dy = D[d-1]
    PIECES[k] = (x,y,dx,dy)
    B[x][y].append(k)
 
def update(num,x,y,dx,dy):
    nx,ny = x+dx, y+dy 
    for k in B[x][y]:
        _,_,_dx,_dy = PIECES[k]
        PIECES[k] = nx,ny,_dx,_dy
    PIECES[num] = nx,ny,dx,dy
 
def move(num):
    x,y,dx,dy = PIECES[num] 
    # k번 말이 가장 바닥인가? 
    if B[x][y][0] != num:
        return False 
    # 움직이기 
    nx,ny = x+dx, y+dy 
    color = A[nx][ny]
    if color == 0:        
        update(num,x,y,dx,dy)
        B[nx][ny], B[x][y] = B[nx][ny]+B[x][y], []
    elif color == 1:
        update(num,x,y,dx,dy)
        B[nx][ny], B[x][y] = B[nx][ny]+B[x][y][::-1], []    
    else:
        dx,dy = -dx, -dy
        nx,ny = x+dx, y+dy
        color = A[nx][ny]
        if color == 0:        
            update(num,x,y,dx,dy)            
            B[nx][ny], B[x][y] = B[nx][ny]+B[x][y], []
        elif color == 1:
            update(num,x,y,dx,dy)
            B[nx][ny], B[x][y] = B[nx][ny]+B[x][y][::-1], []
        else:
            # 이동 x 
            nx,ny = x,y
            update(num,x,y,0,0)
            PIECES[num] = nx,ny,dx,dy
            
    # 4개 이상?
    if len(B[nx][ny]) >= 4:
        return True 
    else:
        return False 
 
T,done = 0, False 
while T < 1001 and not done:
    T += 1 
    for k in range(1,K+1):
        done = move(k)
        if done:
            break 
print(-1 if T > 1000 else T)
 