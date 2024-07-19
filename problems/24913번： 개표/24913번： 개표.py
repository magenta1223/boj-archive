#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 24913                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/24913                         #+#        #+#      #+#     #
#     Solved: 2024-07-19 03:17:03 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


from math import ceil 

input = open(0).readline 

N,Q = map(int, input().split())
votes = [0] * (N+1)
total, mx = 0, 0 
for _ in range(Q):
    q,x,y = map(int,input().split())
    if q == 1:
        votes[y-1] += x
        if y <= N:
            total += x 
            mx = max(mx, votes[y-1])
    else:
        if votes[-1]+x > mx and ceil((total+y)/N) < votes[-1]+x:
            print("YES")
        else:
            print("NO")
            

