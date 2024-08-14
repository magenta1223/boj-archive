#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2468                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2468                          #+#        #+#      #+#     #
#     Solved: 2024-08-14 00:38:44 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


from collections import deque 


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
D = [(-1,0),(0,1),(1,0),(0,-1)]

MaxHeight = max([max(row) for row in A])

def nSatetyZone(height):
    def bfs(i,j):
        visited[i][j] = True 
        q = deque([(i,j)])
        while q:
            x,y = q.popleft()
            for dx, dy in D:
                nx,ny = x+dx, y+dy 
                if 0<=nx<N and 0<=ny<N and A[nx][ny] > height and not visited[nx][ny]:
                    visited[nx][ny] = True 
                    q.append((nx,ny))
        return 1 

    res = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] > height and not visited[i][j]:
                res += bfs(i,j)
    
    return res 

# MaxHeight가 1인 경우 
print(max([nSatetyZone(i) for i in range(1,MaxHeight)]))