#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2470                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2470                          #+#        #+#      #+#     #
#     Solved: 2024-01-31 20:19:34 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input().strip())
l = list(map(int, input().split()))
l.sort()
a,b=0,N-1
best_mixed = abs(l[a] + l[b])
ans = sorted([l[a], l[b]])
while a<b:
    mixed = l[a] + l[b]
    if abs(mixed) < best_mixed:
        best_mixed=abs(mixed)
        ans = [l[a], l[b]]
    if mixed < 0:
        a+=1
    elif mixed > 0:
        b-=1 
    else:
        ans = [l[a], l[b]]
        break 
print(*ans)