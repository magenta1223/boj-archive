#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2252                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2252                          #+#        #+#      #+#     #
#     Solved: 2024-04-05 15:21:38 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
 
input = open(0).readline 
 
N,M = map(int, input().split())
 
queue = deque([])
 
cnt = {i : 0 for i in range(1,N+1)} # i앞에 오는 사람 수
connect = {i : [] for i in range(1,N+1)} # i뒤에 오는 사람들 
 
for _ in range(M):
    A, B = map(int, input().split())
    cnt[B] += 1
    connect[A].append(B)
 
for i in range(1, N + 1):
    if cnt[i] == 0:
        queue.append(i) # 앞에 아무도 없다면 -> 맨 앞이겠죠 
 
answer = []
 
while queue:
    node = queue.popleft()
    answer.append(node)
    
    # node 뒤에 오는 사람들 
    for next in connect[node]:
        # node가 빠졌으니 -1 
        cnt[next] -= 1
        # 맨 앞이면 그 다음 ㄱㄱ 
        if cnt[next] == 0:
            queue.append(next)
 
print(' '.join(map(str, answer)))