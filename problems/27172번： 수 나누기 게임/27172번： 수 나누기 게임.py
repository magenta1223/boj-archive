#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 27172                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/27172                         #+#        #+#      #+#     #
#     Solved: 2024-03-05 16:32:19 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 
N=int(input())
L=list(map(int,input().split()))
maxL = max(L)
ANS = [0] * (maxL + 1)
CARDS = [0] * (maxL + 1)
for num in L:
    CARDS[num] = 1
 
for i in range(N):
    x = L[i]
    c = 0
    for m in range(2,(maxL // x)+1):
        if CARDS[m*x]:
            ANS[m*x] -= 1
            c += 1
    ANS[x] += c 
print(*[ANS[l] for l in L])