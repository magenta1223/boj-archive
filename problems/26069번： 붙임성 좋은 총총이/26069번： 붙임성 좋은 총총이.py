#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 26069                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/26069                         #+#        #+#      #+#     #
#     Solved: 2023-11-22 17:16:44 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
d=dict(ChongChong=True)
for _ in range(N):
    a,b=input().split()
    if a not in d:
        d[a] = False
    if b not in d:
        d[b] = False
    if d[a] or d[b]:
        d[a], d[b] = True, True
print(sum(d.values()))