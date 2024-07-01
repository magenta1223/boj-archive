#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10845                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10845                         #+#        #+#      #+#     #
#     Solved: 2024-04-04 14:36:57 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
 
input = open(0).readline 
q = deque([])
for _ in range(int(input())):
    cmd = input().strip().split()
    if len(cmd) > 1:
        q.append(cmd[1])
        continue 
    cmd = cmd[0]
    if cmd=="pop":
        print(q.popleft() if q else -1) 
    elif cmd == "size":
        print(len(q)) 
    elif cmd == "empty":
        print(0 if q else 1) 
    elif cmd == "front":
        print(q[0] if q else -1)
    else:
        print(q[-1] if q else -1)
 