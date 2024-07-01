#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2473                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2473                          #+#        #+#      #+#     #
#     Solved: 2024-04-08 15:52:32 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
L = list(map(int,input().split()))
L.sort()
 
best_mixed = abs(L[0] + L[1] + L[-1])
ans = L[0], L[1], L[-1] 
for b in range(1,N-1):
    a,c = 0,N-1 
    while a<b<c:
        mix = L[a]+L[b]+L[c]
        if abs(mix) < best_mixed:
            best_mixed = abs(mix)
            ans = L[a], L[b], L[c]
        if mix < 0:
            a += 1
        else:
            c -= 1 
print(*ans)