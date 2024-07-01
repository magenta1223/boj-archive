#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 9328                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/9328                          #+#        #+#      #+#     #
#     Solved: 2024-04-04 16:04:44 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
from string import ascii_lowercase, ascii_uppercase
 
input = open(0).readline
 
D = [(-1,0),(0,1),(1,0),(0,-1)]
 
def prep(arr):
    return [["."] * (W+2)] + [ ["."] + row + ["."] for row in arr] +  [["."] * (W+2)] 
 
def bfs(q:deque, visited:list, keys:str):
    find = 0 
    next_keys = keys 
    nq = deque([])
    while q:
        x,y = q.popleft()
        for dx, dy in D:
            nx,ny = x+dx, y+dy 
            if 0<=nx<H+2 and 0<=ny<W+2 and A[nx][ny] != "*" and not visited[nx][ny]:
                cell = A[nx][ny]
                # 빈칸
                if cell == ".":
                    visited[nx][ny] = True 
                    q.append((nx,ny))
                # 문서 
                elif cell == "$":
                    visited[nx][ny] = True 
                    q.append((nx,ny))
                    find += 1 
                # 문 
                elif cell in ascii_uppercase:
                    if cell.lower() in keys:
                        visited[nx][ny] = True 
                        q.append((nx,ny))
                    else:
                        nq.append((x,y))
                # 열쇠 
                elif cell in ascii_lowercase:
                    visited[nx][ny] = True 
                    q.append((nx,ny))
                    next_keys += cell
 
    return nq, visited, next_keys, find 
 
for _ in range(int(input())):
    H,W = map(int,input().split())
    A = prep([list(input().strip()) for _ in range(H)])
    keys = input().strip()
    visited = [[False] * (W+2) for _ in range(H+2)]
    q = deque([(0,0)])
    ans = 0
    while True:
        q, visited, next_keys, find = bfs(q,visited,keys)
        ans += find
        if next_keys == keys:
            break 
        keys = next_keys
    print(ans)
 
 