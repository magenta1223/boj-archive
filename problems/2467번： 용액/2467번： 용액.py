#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2467                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2467                          #+#        #+#      #+#     #
#     Solved: 2024-04-05 16:23:12 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
L = list(map(int,input().split()))
L.sort()
s, e = 0, N-1 
best = abs(L[s] + L[e])
ans = L[s], L[e]
while s < e:
    mixed = L[s] + L[e]
    if abs(mixed) < best:
        best = abs(mixed)
        ans = L[s], L[e]
    if mixed < 0:
        s += 1 
    else:
        e -= 1
print(*ans)