#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10026                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10026                         #+#        #+#      #+#     #
#     Solved: 2024-03-29 18:36:46 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
D = [(-1,0), (0,1), (1,0), (0,-1)]
 
N = int(input())
A = [list(input()) for _ in range(N)]
B = [[A[i][j] if A[i][j] == 'B' else "R" for j in range(N)] for i in range(N)]
 
def n_sector(board):
    visited = [[False] * N for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            ans += 1
            q = deque([(i,j)])
            cell = board[i][j]
            while q:
                x,y = q.popleft()
                for dx, dy in D:
                    nx, ny = x+dx, y+dy 
                    if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and cell == board[nx][ny]:
                        visited[nx][ny] = True 
                        q.append((nx, ny))
    return ans 
 
print(n_sector(A), n_sector(B))