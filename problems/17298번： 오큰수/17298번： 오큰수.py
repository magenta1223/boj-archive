#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17298                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17298                         #+#        #+#      #+#     #
#     Solved: 2023-12-29 14:46:25 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
l=list(map(int, input().split()))
l_r = l[::-1]
NGE = []
results = [0] * N
for i in range(N):
    while NGE and l[N-1-i] >= NGE[-1]:
        NGE.pop()
    if NGE:
        results[N-1-i] = NGE[-1]
    else:
        results[N-1-i] = -1
    NGE.append(l_r[i])
print(*results)