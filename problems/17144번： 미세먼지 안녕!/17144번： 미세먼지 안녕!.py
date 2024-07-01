#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17144                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17144                         #+#        #+#      #+#     #
#     Solved: 2024-02-18 15:07:42 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

R,C,T=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(R)]
D = [(1, 0), (-1 ,0), (0, 1), (0, -1)]
 
Purifier = None
for i in range(R):
    if A[i][0] == -1:
        Purifier = [(i,0), (i+1, 0)]
        A[i][0]= 0
        A[i+1][0] = 0
        break 
    if Purifier is not None:
        break 
 
def dust_diffusion(array):
    diff_array = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            dust = array[i][j]
            if dust:
                for dx, dy in D:
                    diff_x, diff_y = i+dx, j+dy
                    if 0<=diff_x<R and 0<=diff_y<C and (diff_x, diff_y) not in Purifier:
                        diff_array[diff_x][diff_y] += dust // 5
                        array[i][j] -= dust // 5
    for i in range(R):
        for j in range(C):
            array[i][j] += diff_array[i][j]
    return array
 
def purify(array):
    initD = [(-1,0), (1,0)]
    rot_func = [lambda dx, dy: (dy, -dx), lambda dx, dy: (-dy, dx)]
    rRange = [(0, Purifier[0][0]+1), (Purifier[1][0], R)]
    for (px, py), (dx, dy), (rmin, rmax), rot  in zip(Purifier, initD, rRange, rot_func):
        x, y = px, py
        while True:
            array[x][y] = array[x+dx][y+dy]
            if (x,y) == (px, py):
                array[x][y] = 0
            x,y=x+dx, y+dy
            if not rmin<=x+dx<rmax or not 0<=y+dy<C:
                dx ,dy = rot(dx, dy)                
            if (x,y) == (px, py):
                break        
    return array
for _ in range(T):
    A = dust_diffusion(A)
    A = purify(A)
print( sum([  sum(A[i])  for i in range(R)]) )