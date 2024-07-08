#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10800                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10800                         #+#        #+#      #+#     #
#     Solved: 2024-07-08 06:16:58 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #




from collections import defaultdict
input = open(0).readline 

N = int(input())
Sizes = {i : defaultdict(int) for i in range(1,2001)}
Users = {i : [] for i in range(1,2001)}

for i in range(N):
    c,s = map(int,input().split())
    Users[s].append((i,c))
    Sizes[s][c] += 1


CUMSUM = [0] * (N+1)
ANS = [0] * N
S = 0

for s in sorted(Sizes.keys()):
    for user, userColor in Users[s]:
        ANS[user] = S - CUMSUM[userColor]
    for c,v in Sizes[s].items():
        CUMSUM[c] += s*v
    S += s * len(Users[s])
print(*ANS, sep = '\n')