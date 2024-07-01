#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1007                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1007                          #+#        #+#      #+#     #
#     Solved: 2024-06-11 11:36:54 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from math import sqrt 
 
def getDist(a,b):
    return sqrt(a**2 + b**2)
 
def dfs(bitmask, depth, idx):
    global ans 
    if depth == N//2:
        sx,sy,ex,ey = 0,0,0,0
        bitmask = bin(bitmask)[2:].zfill(N)
        for i in range(N):
            a,b = P[i]
            if bitmask[i] == "1":
                sx+=a 
                sy+=b 
            else:
                ex+=a
                ey+=b 
        ans = min(ans, getDist(ex-sx,ey-sy))
        return 
    
    for i in range(idx,N):
        if (1<<i) & bitmask:
            continue 
        dfs(bitmask|(1<<i), depth+1,i)
 
    
 
anss = []
 
for _ in range(int(input())):
 
    N = int(input())
    P = [list(map(int,input().split())) for _ in range(N)]
    FULL = (1<<N) - 1 
    ans = INF = float("inf")
    cnt = 0
    dfs(0,0,0)
    print(ans)