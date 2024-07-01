#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2667                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2667                          #+#        #+#      #+#     #
#     Solved: 2024-01-05 11:55:52 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
MAP=[ [int(el) for el in list(input().strip())] for _ in range(N)]
visited = [[False] * N for _ in range(N)]
stack = [[0,0]]
clip = lambda x: min(max(x, 0), N-1)
possible = lambda x: True if 0 <= x < N else False 
 
results = []
c = 0
while stack:
    x, y=stack.pop()
    if not visited[x][y]:
        visited[x][y] = True 
        if MAP[x][y]:
            c += 1
            for _x, _y in [[x-1, y],[x+1, y],[x, y-1],[x, y+1]]:
                if possible(_x) and possible(_y) and MAP[_x][_y] and not visited[_x][_y]:
                    stack.append([_x, _y])
    if not stack:
        if c:
            results.append(c)
            c = 0
        new = False 
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    stack.append([i,j])
                    new = True
                    break 
            if new:
                break 
 
print(len(results))
print(*sorted(results), sep ='\n')