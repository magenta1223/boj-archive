#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 23291                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/23291                         #+#        #+#      #+#     #
#     Solved: 2024-02-26 13:30:37 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
 
def add(l):
    _min = min(l)
    for i in range(N):
        if l[i] == _min:
            l[i] += 1
    arr = LtoA(l)
    return arr
    
def LtoA(l):
    return [ [l[i]] + [0] * (N-1)   for i in range(N)]
def AtoL(arr):
    l = []
    for i in range(N):
        if arr[i][0]:
            if 0 in arr[i]:
                l.extend(arr[i][:arr[i].index(0)])
            else:
                l.extend(arr[i])
    return l
 
def rotate(arr):
    n,m = len(arr), len(arr[0])
    tmp = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            tmp[j][n-i-1] = arr[i][j]
    return tmp
 
def adjust(arr):
    tmp = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            f = arr[x][y]
            for dx, dy in D:
                nx,ny=x+dx,y+dy 
                if 0<=nx<N and 0<=ny<N and arr[nx][ny] and arr[nx][ny] < f:
                    d = (f-arr[nx][ny]) // 5
                    tmp[nx][ny] += d
                    tmp[x][y] -= d
    for i in range(N):
        for j in range(N):
            arr[i][j] += tmp[i][j]
    return arr 
 
def _roll(arr,x,y,idx,angle = 90):
    target_arr = [[ arr[_i][_j] for _j in range(y)] for _i in range(idx, idx+x)]
    for i in range(angle // 90):
        target_arr = rotate(target_arr)
    for _i in range(idx, idx+x):
        for _j in range(y):
            arr[_i][_j] = 0
    idx += x
    for i,row in enumerate(target_arr):
        j = arr[idx+i].index(0)
        arr[idx+i][j:j+len(row)] = row
    if x == y:
        y+=1
    else:
        x+=1
    return arr,x,y,idx
 
def roll(arr, x,y,idx):
    while N-x-idx >= y:
        arr,x,y,idx = _roll(arr,x,y,idx)
    return arr
 
D = [(-1,0),(0,1),(1,0),(0,-1)]
N,K=map(int,input().split())
L=list(map(int,input().split()))
 
t = 0
while max(L) - min(L) > K:
    A = add(L)
    x,y,idx = 1,1,0
    A = roll(A,x,y,idx)
    A = adjust(A)
    L = AtoL(A)
    A = LtoA(L)
    A,x,y,idx = _roll(A,N//2,1,0, 180)
    A,x,y,idx = _roll(A,N//4,2,idx, 180)
    A = adjust(A)
    L = AtoL(A)
 
    t += 1
 
# print(L)
print(t, sep ='\n')