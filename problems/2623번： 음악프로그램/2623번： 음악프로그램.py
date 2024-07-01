#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2623                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2623                          #+#        #+#      #+#     #
#     Solved: 2024-04-08 16:08:23 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
 
N,M = map(int,input().split())
 
connect = {i : [] for i in range(1,N+1)}
count =  {i : 0 for i in range(1,N+1)}
 
for _ in range(M):
    L = list(map(int,input().split()))
    n,L = L[0], L[1:]
    for i in range(n-1):
        a, b = L[i], L[i+1]
        count[b] += 1 
        connect[a].append(b)
 
q = deque([i for i in range(1,N+1) if not count[i]])
ans = []
while q:
    singer = q.popleft()
    ans.append(singer)
    for next_singer in connect[singer]:
        count[next_singer] -= 1
        if not count[next_singer]:
            q.append(next_singer)
 
# 불가능한 경우 
print(*ans if len(ans) == N else [0], sep = '\n')