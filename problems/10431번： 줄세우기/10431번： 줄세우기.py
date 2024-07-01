#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10431                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10431                         #+#        #+#      #+#     #
#     Solved: 2024-05-09 11:43:04 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from bisect import bisect_left
 
for _ in range(int(input())):
    L = list(map(int,input().split()))
    T,L = L[0],L[1:]
    ans, l = 0, []
    for i in range(20):
        a = L[i] 
        idx = bisect_left(l, a)
        if idx != i:
            ans += i-idx
            l.insert(idx, a)
        else:
            l.append(a)    
    print(T, ans)