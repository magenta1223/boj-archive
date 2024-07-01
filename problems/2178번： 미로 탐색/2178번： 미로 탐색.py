#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2178                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2178                          #+#        #+#      #+#     #
#     Solved: 2024-01-11 11:14:57 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N, M = map(int, input().split())
array = [[int(el) for el in input().strip()] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
costs = [[float("inf") for _ in range(M)] for _ in range(N)]
DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
 
queue = [(0, 0, 0)]  # (x, y, depth)
 
while queue:
    x, y, depth = queue.pop(0)
    if x == N - 1 and y == M - 1:
        break
    adjs = []
    for dx, dy in DIRS:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < N and 0 <= new_y < M and array[new_x][new_y] and not visited[new_x][new_y]:
            adjs.append((new_x, new_y))
    for _x, _y in adjs:
        if costs[_x][_y] > depth + 1:
            costs[_x][_y] = depth + 1
            visited[_x][_y] = True
            queue.append((_x, _y, depth + 1))
 
print(costs[N - 1][M - 1] + 1)
 