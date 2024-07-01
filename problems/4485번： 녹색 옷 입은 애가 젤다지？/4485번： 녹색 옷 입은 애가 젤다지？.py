#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 4485                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/4485                          #+#        #+#      #+#     #
#     Solved: 2024-05-08 18:27:23 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from heapq import heappop, heappush
 
D = [(-1,0), (0,1), (1,0), (0,-1)]
INF = float("inf")
 
def bfs():
    hq = [(A[0][0],0,0)]
    costs = [[INF] * N for _ in range(N)]
 
    while hq:
        cur_cost, x,y = heappop(hq)
 
        if cur_cost > costs[x][y]:
            continue 
 
        for dx, dy in D:
            nx, ny= x+dx, y+dy 
            if 0<=nx<N and 0<=ny<N and costs[nx][ny] > cur_cost + A[nx][ny]:
                next_cost = cur_cost + A[nx][ny]
                heappush(hq, (next_cost, nx, ny))
                costs[nx][ny] = next_cost
 
    return costs[-1][-1]
 
 
i = 1
while True:
    N = int(input())
    if not N:
        break 
    A = [list(map(int,input().split())) for _ in range(N)]
    print(f"Problem {i}: {bfs()}" )
    i += 1 