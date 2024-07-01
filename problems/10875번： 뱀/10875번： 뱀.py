#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10875                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10875                         #+#        #+#      #+#     #
#     Solved: 2024-05-20 13:30:50 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def ccw(x1,y1,x2,y2,x3,y3,x4,y4,dx,dy):
    mx1,mx2,mx3,mx4 = min(x1,x2), max(x1,x2), min(x3,x4), max(x3,x4)
    my1,my2,my3,my4 = min(y1,y2), max(y1,y2), min(y3,y4), max(y3,y4)
    
    def _ccw(x1,y1,x2,y2,x3,y3):
        v=(x1-x2)*(y2-y3) - (x2-x3)*(y1-y2)
        return v//abs(v) if v else v
    
    ccw123= _ccw(x1,y1,x2,y2,x3,y3)
    ccw124= _ccw(x1,y1,x2,y2,x4,y4)
    ccw341= _ccw(x3,y3,x4,y4,x1,y1)
    ccw342= _ccw(x3,y3,x4,y4,x2,y2)
 
    if dx==1:
        t = mx3-x1 
    elif dx==-1:
        t = x1-mx4 
    elif dy==1:
        t = my3-y1 
    else:
        t = y1-my4 
 
    if ccw123*ccw124 < 0 and ccw341 * ccw342 < 0:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:        
            return 1, t 
    if not ccw123*ccw124 or not ccw341*ccw342:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            return 1, t
    return 0, t 
 
input = open(0).readline 
 
D = [(-1,0), (0,1), (1,0), (0,-1)]
L,N = int(input()), int(input())
L +=1 
COMMANDS = []
for _ in range(N):
    t,d = input().split()
    COMMANDS.append((int(t),d))
COMMANDS.append((3*L, "L"))
LINES = [(-L,-L,L,-L), (-L,-L,-L,L), (L,L,L,-L), (L,L,-L,L)]
 
ans, done = 0, False 
x,y,dx,dy = 0,0,1,0 
 
for t, d in COMMANDS:
    nx,ny = x+dx*t, y+dy*t 
    line = (x,y,nx,ny)
    # ccw 
    dur = float("inf")
    for existing_line in LINES:
        cross, _dur = ccw(*line, *existing_line,dx,dy)
        if cross:
            done = True 
            dur = min(dur, _dur) # 교차하는 최소시간 계산
    if done:
        ans += dur 
        break 
    else:
        ans += t 
        LINES.append((x,y,x+dx*(t-1), y+dy*(t-1) ))
        x,y = nx, ny
        dx, dy = (-dy,dx) if d == "L" else (dy,-dx)
    
print(ans)