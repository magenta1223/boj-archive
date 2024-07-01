#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1799                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1799                          #+#        #+#      #+#     #
#     Solved: 2024-04-09 13:42:55 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

D = [(1,1), (1,-1), (-1,1), (-1,-1)]
 
def dfs(prev_idx, depth):
    global ans 
    if prev_idx == M-1 or not sum([sum(row) for row in A]):
        ans = max(ans, depth)
        return 
 
    for i in range(prev_idx + 1, M):
        x,y = CANDIDATES[i]
        if not A[x][y]:
            continue
        attacked = []
        for bx, by in CONSTRAINTS[x][y]:
            if A[bx][by]: 
                A[bx][by] = 0
                attacked.append((bx,by))
        dfs(i, depth + 1)
        for bx, by in attacked:
            A[bx][by] = 1
 
 
 
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B, W = [], []
for i in range(N):
    for j in range(N):
        if A[i][j]:
            if (i+j) % 2:
                W.append((i,j))
            else:
                B.append((i,j))
CONSTRAINTS = [[[(i,j)] for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        if not A[i][j]:
            CONSTRAINTS[i][j] = []
            continue
        for dx, dy in D:
            x, y = i,j
            while 0<=x+dx<N and 0<=y+dy<N:
                x+=dx 
                y+=dy 
                CONSTRAINTS[i][j].append((x,y))
 
final_ans = 0 
for CANDIDATES in [B,W]:
    M = len(CANDIDATES)
    ans = 0 
    dfs(-1, 0)
    final_ans += ans 
print(final_ans)