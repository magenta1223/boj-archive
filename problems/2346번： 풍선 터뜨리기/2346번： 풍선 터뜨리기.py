#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2346                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2346                          #+#        #+#      #+#     #
#     Solved: 2023-11-22 16:10:12 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
N=int(input())
q=deque([ (i+1, x) for i, x in enumerate(list(map(int, input().split())))])
 
result = []
while len(q) > 1:
    i, x = q.popleft()
    if x > 0:
        for _ in range(x-1):
            q.append(q.popleft())
    else:
        for _ in range(abs(x)):
            q.appendleft(q.pop())
    result.append(str(i))
result.append(str(q[0][0]))
print(" ".join(result))
    