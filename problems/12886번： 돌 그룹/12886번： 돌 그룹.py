#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 12886                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/12886                         #+#        #+#      #+#     #
#     Solved: 2024-02-29 00:23:56 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque  
A,B,C = map(int, input().split())
 
# bfs같은데 ? 메모리초과
# 아마도 크게 만들면서 ㅈ된듯 
N = A+B+C
queue = deque([[A,B,C]])
# visited = [[[False] * N for _ in range(N)]  for _ in range(N)]
visited = set()
done = False
while queue:
    l = queue.popleft()
    if l[0] == l[1] == l[2]:
        done = True
        break 
    # 선택하는 방법
    for i,j,k in [(0,1,2), (1,2,0), (0,2,1)]:
        if l[i] == l[j]:
            continue
        i,j = (i,j) if l[i] > l[j] else (j,i)
        xi, xj = l[i], l[j]
        _l = sorted([xi - xj, xj + xj, l[k]])
        a,b,c= _l
        if (a,b,c) not in visited:
            visited.add((a,b,c))
            queue.append(_l)
print(1 if done else 0)