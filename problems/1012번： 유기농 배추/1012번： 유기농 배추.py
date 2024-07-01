#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1012                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1012                          #+#        #+#      #+#     #
#     Solved: 2024-01-05 12:04:48 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

T=int(input())
def solve():
    M,N,K=map(int, input().split())
    MAP = [[0 for _ in range(N)] for _ in range(M)]
    for _ in range(K):
        x,y = map(int, input().split())
        MAP[x][y] = 1
        
    visited = [[False] * N for _ in range(M)]
    stack = [[0,0]]
    results = []
    c = 0
    while stack:
        x, y=stack.pop()
        if not visited[x][y]:
            visited[x][y] = True 
            if MAP[x][y]:
                c += 1
                for _x, _y in [[x-1, y],[x+1, y],[x, y-1],[x, y+1]]:
                    if 0 <= _x < M and 0 <= _y < N and MAP[_x][_y] and not visited[_x][_y]:
                        stack.append([_x, _y])
        if not stack:
            if c:
                results.append(c)
                c = 0
            new = False 
            for i in range(M):
                for j in range(N):
                    if not visited[i][j]:
                        stack.append([i,j])
                        new = True
                        break 
                if new:
                    break 
    print(len(results))
    
for _ in range(T):
    solve()