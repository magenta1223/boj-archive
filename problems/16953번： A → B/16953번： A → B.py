#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 16953                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/16953                         #+#        #+#      #+#     #
#     Solved: 2024-04-04 13:21:30 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
def add1(x):
    return int(str(x) + "1")
A,B=map(int,input().split())
if A==B:
    print(1)
    exit(0)
q = deque([(A,0)])
# visited = [False] * (B+1)
# visited[A] = True 
visited = set()
while q:
    x,n =q.popleft()
    for nx in [x*2, add1(x)]:
        # if nx <= B and not visited[nx]:
        if nx <= B and nx not in visited:
            if nx == B:
                print(n+2)
                exit(0)
            # visited[nx] = True 
            visited.add(nx)
            q.append((nx,n+1))
print(-1)