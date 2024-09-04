#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14868                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14868                         #+#        #+#      #+#     #
#     Solved: 2024-09-03 07:55:18 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #




import sys 
input = sys.stdin.readline 

def find(a):
    if a == PARENT[a]:
        return a     
    PARENT[a] = find(PARENT[a])
    return PARENT[a]

def _merge(a, b):
    a, b = find(a), find(b)
    if a != b:
        a,b = (a,b) if (COUNT[a]<COUNT[b]) else (b,a)
        PARENT[b] = a
        COUNT[b] += COUNT[a] 

def merge_cvz(q):
    for x,y in q:
        for dx, dy in D:
            nx,ny= x+dx, y+dy 
            if 0<=nx<N and 0<=ny<N and VISITED[nx][ny] != -1 and VISITED[nx][ny] != VISITED[x][y]:
                _merge(VISITED[nx][ny], VISITED[x][y])

def bfs(q):
    nq = []
    for x,y in q:
        for dx, dy in D:
            nx,ny= x+dx, y+dy 
            if 0<=nx<N and 0<=ny<N and VISITED[nx][ny] == -1:
                VISITED[nx][ny] = VISITED[x][y] 
                nq.append((nx,ny))
    return nq 

D= [(-1,0), (0,1), (1,0), (0,-1)]
N,K = map(int, input().split())
VISITED = [[-1] * N for _ in range(N)]
PARENT = [i for i in range(K)]
COUNT = [1] * K  

q = []
for i in range(K):
    x,y = map(int, input().split())
    x,y = x-1, y-1 
    q.append((x,y))
    VISITED[x][y] = i 

t = 0 
merge_cvz(q)
while COUNT[0] != K: 
    q  = bfs(q)
    merge_cvz(q)
    t+=1 
print(t)
