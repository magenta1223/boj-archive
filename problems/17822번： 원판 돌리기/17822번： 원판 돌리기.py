#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17822                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17822                         #+#        #+#      #+#     #
#     Solved: 2024-02-20 11:47:52 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
 
N,M,T=map(int,input().split())
BOARD = [list(map(int,input().split())) for _ in range(N)]
D = [(-1, 0), (1,0),(0,1), (0,-1)]
 
def adj(i,j):
    return [(i+di, (j+dj+M) % M)   for di, dj in D if 0<=i+di<N]
 
def rotate(board, x, d, k):
    for i in range(1, N//x+1):
        line = deque(board[x*i-1])
        if d:
            line.rotate(-k)
        else:
            line.rotate(k)
        board[x*i-1] = list(line)
    return board 
 
 
def change_avg():
    avg_count = 0
    all_sum = 0
    for i in range(N):
        for j in range(M):
            if BOARD[i][j] != 0:
                avg_count += 1
                all_sum += BOARD[i][j]
    if avg_count == 0:
        return False
    avg = all_sum / avg_count
    for i in range(N):
        for j in range(M):
            if BOARD[i][j] != 0:
                if BOARD[i][j] > avg:
                    BOARD[i][j] -= 1
                elif BOARD[i][j] < avg:
                    BOARD[i][j] += 1
    return True
 
def solve(x, y):
    q = deque()
    q.append((x, y))
    visited.add((x,y))
    value = BOARD[x][y]
    BOARD[x][y] = 0
    count = 0
    while q:
        x, y = q.popleft()
        for nx, ny in adj(x,y):
            # nx = x + dx[i]
            # ny = y + dy[i]
            # if 0 > ny or ny >= m:
            #     if y == 0:
            #         ny = m-1
            #     elif y == m-1:
            #         ny = 0
            if 0 <= nx < N:
                if (nx,ny) not in visited:
                    if BOARD[nx][ny] == value:
                        count += 1
                        BOARD[nx][ny] = 0
                        visited.add((nx, ny))
                        q.append((nx, ny))
    if count == 0:
        BOARD[x][y] = value
    return count
 
for _ in range(T):
    BOARD = rotate(BOARD, *map(int,input().split()))
    count = 0
    visited = set()  
 
    for i in range(N):
        for j in range(M):
            if (i,j) not in visited and BOARD[i][j]:
                count += solve(i,j)
    if count == 0:
        change_avg()
 
    # print(*BOARD, sep = '\n')
    # if not total:
    #     avg = [ BOARD[i][j] for i in range(N) for j in range(M) if BOARD[i][j]]
    #     if avg:
    #         avg = sum(avg) / len(avg)
    #         for i in range(N):
    #             for j in range(M):
    #                 if BOARD[i][j]:
    #                     if BOARD[i][j] > avg:
    #                         BOARD[i][j] -= 1
    #                     elif BOARD[i][j] < avg:
    #                         BOARD[i][j] += 1
        # print('-----------ADJUST------------')
        # print(*BOARD, sep = '\n')
 
print(sum([sum(BOARD[i]) for i in range(N)]))
 