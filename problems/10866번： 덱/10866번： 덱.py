#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10866                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10866                         #+#        #+#      #+#     #
#     Solved: 2024-04-04 14:39:56 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
 
input = open(0).readline 
deq = deque([])
for _ in range(int(input())):
    cmd = input().strip().split()
    if len(cmd) > 1:
        if cmd[0] == "push_front":
            deq.appendleft(cmd[1])
        else:
            deq.append(cmd[1])
        continue 
    cmd = cmd[0]
    if cmd=="pop_front":
        print(deq.popleft() if deq else -1) 
    elif cmd=="pop_back":
        print(deq.pop() if deq else -1) 
    elif cmd == "size":
        print(len(deq)) 
    elif cmd == "empty":
        print(0 if deq else 1) 
    elif cmd == "front":
        print(deq[0] if deq else -1)
    else:
        print(deq[-1] if deq else -1)