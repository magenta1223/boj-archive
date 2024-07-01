#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11866                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11866                         #+#        #+#      #+#     #
#     Solved: 2023-11-22 14:56:50 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
N,K=map(int, input().split())
q=deque([i for i in range(1, N+1)])
s=""
l=[]
while q:
    for i in range(K-1):
        q.append(q.popleft())
    l.append(str(q.popleft()))
print(f'<{", ".join(l)}>')