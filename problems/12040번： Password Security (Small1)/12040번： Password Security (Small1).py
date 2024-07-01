#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 12040                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/12040                         #+#        #+#      #+#     #
#     Solved: 2024-06-17 15:03:21 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import random
from string import ascii_uppercase
 
for t in range(1, int(input())+1):
    N = int(input())
    P = input().split()
    
    exist = False 
    
    for r in range(25000):
        u = []
        w = [False] * 26
        
        while len(u) < 26:
            x = random.randint(0, 25)
            if not w[x]:
                u.append(x)
                w[x] = True
                
        str_list = []
        
        for idx in u:
            str_list.append(ascii_uppercase[idx])
        
        _str = ''.join(str_list)
        for word in P:
            if _str.find(word) != -1:
                exist = True 
                break
        
        if not exist:
            break 
 
 
    if not exist:
        print(f"Case #{t}: {_str}")
    else:
        print(f"Case #{t}: IMPOSSIBLE")