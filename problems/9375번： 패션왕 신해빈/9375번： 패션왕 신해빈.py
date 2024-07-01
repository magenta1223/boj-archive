#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 9375                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/9375                          #+#        #+#      #+#     #
#     Solved: 2024-03-29 18:29:59 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import Counter 
 
for _ in range(int(input())):
    N = int(input())
    
    c = Counter([input().split()[1] for _ in range(N)])
    ans = 1
    for v in c.values():
        ans *= (v+1)
    print(ans -1)