#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 16234                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/16234                         #+#        #+#      #+#     #
#     Solved: 2024-02-15 15:57:36 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

D = [(1,0), (0,1), (-1, 0), (0, -1)]
N,L,R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
 
from collections import deque
 
def move(arr):
    arr = [[arr[i][j] for j in range(N)] for i in range(N)]
    visited = [[False] * N for _ in range(N)]
    UNIONS = []
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            union = []
            queue = deque([(i, j)])
            while queue:
                x,y = queue.popleft()
                p = arr[x][y]
                for dx, dy in D:
                    new_x, new_y = x+dx, y+dy
                    if 0<=new_x<N and 0<=new_y<N and  L<=abs(arr[new_x][new_y] - p)<=R and not visited[new_x][new_y]:
                        union.append((new_x, new_y))
                        queue.append((new_x, new_y))
                        visited[new_x][new_y] = True
            if len(union):
                UNIONS.append(union)
            
    for union in UNIONS:
        new_p = int(sum([ arr[i][j] for i, j in union]) / len(union))
        for i, j in union:
            arr[i][j] = new_p
    return arr
 
ans = 0
while True:
    new_A = move(A)
    if all([ A[i][j] == new_A[i][j] for i in range(N) for j in range(N)]):
        break 
    else:
        A = new_A
        ans += 1
print(ans)