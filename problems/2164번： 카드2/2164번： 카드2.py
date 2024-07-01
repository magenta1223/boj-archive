#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2164                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2164                          #+#        #+#      #+#     #
#     Solved: 2023-11-22 14:31:13 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
l=deque([i for i in range(1, int(input())+1)])
while len(l)>2:
    l.popleft()
    l.append(l.popleft())
print(l[-1])