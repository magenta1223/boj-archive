#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 19238                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/19238                         #+#        #+#      #+#     #
#     Solved: 2024-02-20 22:12:29 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M,F = map(int, input().split())
B = [list(map(int,input().split())) for _ in range(N)]
x,y = map(int, input().split())
taxi = x-1,y-1
passengers = [[], []]
for _ in range(M):
    a,b,c,d = map(int,input().split())
    passengers[0].append((a-1,b-1))
    passengers[1].append((c-1,d-1))
D = [(1,0),(-1,0),(0,1),(0,-1)]
 
from collections import deque
 
def find_nearest(taxi, passengers):
    if taxi in passengers[0]:
        return 0, *taxi, passengers[0].index(taxi)
    
    queue = deque([[*taxi, 0]])
    visited = [[False] * N for _ in range(N)]
    nearest = []
    prev_t = 0
    while queue:
        x,y,t = queue.popleft()
        if prev_t != t and nearest:
            break
        for dx, dy in D:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and not B[nx][ny] and not visited[nx][ny]:
                queue.append((nx,ny,t+1))
                visited[nx][ny] = True
                if (nx,ny) in passengers[0]:
                    nearest.append((nx,ny,passengers[0].index((nx,ny))))
        prev_t = t
    if nearest:
        nearest = sorted(nearest, key= lambda x: (x[0], x[1]))
        return t, *nearest[0]
    else:
        return None
 
def to_goal(taxi, goal):
    queue = deque([[*taxi, 0]])
    visited = [[False] * N for _ in range(N)]
    done = False
    while queue:
        x,y,t = queue.popleft()
        for dx, dy in D:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and not B[nx][ny] and not visited[nx][ny]:
                queue.append((nx,ny,t+1))
                visited[nx][ny] = True
                if (nx,ny) == goal:
                    done = True
                    break 
        if done:
            break 
    return done, t+1 if done else 0
    
done = True
for _ in range(M):
    res = find_nearest(taxi, passengers)
    if res is None:
        done = False
        break
    d,x,y,index = res
    if F < d:
        done = False
        break
    F -= d
    start = passengers[0].pop(index)
    goal = passengers[1].pop(index)
    
    reachable, d = to_goal(start, goal)
    if not reachable or F < d:
        done = False
        break 
    F += d
    taxi = goal
        
print(F if done else -1)