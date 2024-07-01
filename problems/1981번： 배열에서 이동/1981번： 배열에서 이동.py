#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1981                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1981                          #+#        #+#      #+#     #
#     Solved: 2024-03-04 18:17:05 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
 
N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
 
target = (N-1, N-1)
D = [(-1,0), (0,1),(1,0), (0,-1)]
 
def check(mid):
    for i in range(201-mid):
        # 값이 i~i+mid 사이에 존재하는 경로를 만들 수 있는지
        done, path = bfs(i, i+mid)
        if done:
            return True 
    return False  
 
def bfs(a, b):
    # a~b 사이에 값이 존재하는 경로를 만들 수 있는지? 
    if not a<= A[0][0] <= b or not a<= A[-1][-1] <= b:
        return False, []
    
    queue = deque([(0,0,[A[0][0]])])
    visited = [[False] * N for _ in range(N)]
    done = False 
    while queue and not done:
        x,y,path = queue.popleft()
        for dx, dy in D:
            nx,ny = x+dx, y+dy 
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and a<=A[nx][ny]<=b:
                visited[nx][ny] = True
                queue.append((nx,ny,path+[A[nx][ny]]))
                if (nx,ny) == target:
                    done = True 
                    break 
 
    return visited[-1][-1], path 
 
start, end = 0, 200 
 
while start <= end:
    mid = (start + end) // 2
    # check 
    if check(mid):
        # mid 차이의 path를 만들 수 있다. 
        end = mid - 1
    else:
        start = mid + 1
        
print(start)