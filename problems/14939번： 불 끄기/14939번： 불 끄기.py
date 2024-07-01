#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14939                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14939                         #+#        #+#      #+#     #
#     Solved: 2024-04-11 22:14:11 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

T = {"#" : "O", "O" : "#"}
D = [(-1,0), (0,1),(1,0),(0,-1),(0,0)]
ADJS = dict()
for i in range(10):
    for j in range(10):
        ADJS[(i,j)] = []
        for di, dj in D:
            ni, nj = i+di, j+dj 
            if 0<=ni<10 and 0<=nj<10:
                ADJS[(i,j)].append((ni,nj))
 
def push(i,j):
    global arr, cnt
    cnt += 1
    for x,y in ADJS[(i,j)]:
        arr[x][y] = T[arr[x][y]]
    
A = [list(input().strip()) for _ in range(10)]
 
ans = 101 
 
for i in range(1<<10):
    # init  
    arr, cnt = [[A[_i][_j] for _j in range(10)] for _i in range(10)], 0
    # init 1st row 
    for j in range(10):
        if i & (1<<j):
            push(0, j)
    
    for j in range(1, 10):
        for k in range(10):
            if arr[j-1][k] == "O": # 현재 셀 윗줄은 현재 줄에서 반드시 제거해야 함. 
                push(j, k)
        if "".join(arr[j-1]) != "#"*10:
            break 
    if "".join(arr[-1]) == "#"*10:
        ans = min(ans, cnt)     
print(ans if ans < 101 else -1)