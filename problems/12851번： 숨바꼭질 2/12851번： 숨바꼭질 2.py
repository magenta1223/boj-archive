#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 12851                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/12851                         #+#        #+#      #+#     #
#     Solved: 2024-04-04 12:11:52 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
INF = float("inf") 
N,K=map(int,input().split())
q = deque([(N,0)])
visited = [INF] * 100_001 
visited[N] = 0 
cnt = 0 
while q:
    x,t = q.popleft()
    if x == K and visited[x] == t:
        cnt += 1
 
    for nx in [x-1,x+1,2*x]:
        if 0>nx or 100_000<nx or visited[nx] < t+1:
            continue 
        visited[nx] = t+1 
        q.append((nx, t+1))
print(visited[K])
print(cnt)