#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1039                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1039                          #+#        #+#      #+#     #
#     Solved: 2024-02-28 22:33:18 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
from itertools import combinations
N,K=map(int,input().split())
L = [s for s in str(N)]
 
queue = deque([(str(N), 0)])
comb = [c for c in combinations(range(len(str(N))), 2)]
ans = 0
# 연산횟수별로 visited가 필요. 
visited = [set() for _ in range(K)]
while queue:
    n, k = queue.popleft()
    if k == K:
        ans = max(ans, n)
        continue
    s = list(str(n))
    for i, j in comb:
        if not (i == 0 and s[j] == "0"):
            s[i], s[j] = s[j], s[i]
            next_n = int("".join(s))
            if next_n not in visited[k]:
                queue.append((next_n, k+1)) 
                visited[k].add(next_n)
            s[i], s[j] = s[j], s[i]
 
print(ans if ans else -1)