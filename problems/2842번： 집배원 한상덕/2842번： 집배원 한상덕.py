#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2842                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2842                          #+#        #+#      #+#     #
#     Solved: 2024-08-20 03:09:46 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



# 피로도 = 모든 집을 방문하는 경로에서 최저 고도와 최대 고도의 차이 
# 최소 피로도를 구해보자 

# 1. 제한 피로도를 두고, 이를 수행 가능한지 확인
# 2. 이분탐색 

# 조건
# 1. 이동은 상하좌우대각선 인접으로 가능
# 2. 모든 집을 방문해야 함. 

# 구현
# 1. 제한피로도를 설정
# 2. P에서 시작. bfs를 수행
# 3. 이동하면서 최소고도, 최대고도를 기록. 피로도를 log
# 4. 제한피로도를 넘기면 -> 하지 말고
# 5. 모든 집을 방문 가능하면 -> 수행 완료. 


from collections import deque

INF = 1_000_000
D = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
N = int(input())
A = [list(input()) for _ in range(N)]
B = [list(map(int,input().split())) for _ in range(N)]
costs = []
for i in range(N):
    costs += B[i]
costs.sort()
MAX = costs[-1]

Houses = [ ]
for i in range(N):
    for j in range(N):
        if A[i][j] == "P":
            P = i,j 
        elif A[i][j] == "K":
            Houses.append((i,j))

def check(a,b):
    x,y = P 
    if not a<=B[x][y]<=b:
        return False 
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True 
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for dx,dy in D:
            nx,ny = x+dx, y+dy 
            if 0<=nx<N and 0<=ny<N and a<=B[nx][ny]<=b and not visited[nx][ny]:
                visited[nx][ny] = True 
                q.append((nx,ny))
    return all([visited[x][y] for x,y in Houses])       



ans = INF 
x,y = P 
S = N**2
for i in range(S):
    s,e = i,S-1 
    while s<=e:
        mid = (s+e)//2 
        if check(costs[i], costs[mid]):
            e = mid-1 
            ans = min(ans, costs[mid]-costs[i])
        else:
            s = mid+1 
print(ans)




