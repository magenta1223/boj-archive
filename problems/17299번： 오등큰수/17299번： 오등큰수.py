#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17299                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17299                         #+#        #+#      #+#     #
#     Solved: 2023-12-29 14:59:38 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import Counter
 
N=int(input())
l=list(map(int, input().split()))
 
c = Counter(l)
 
l_c = [ c[el] for el in l]
l_r = l_c[::-1]
NGF = []
results = [0] * N
for i in range(N):
    while NGF and l_c[N-1-i] >= NGF[-1][0]:
        NGF.pop()
    if NGF:
        results[N-1-i] = NGF[-1][1]
    else:
        results[N-1-i] = -1
    NGF.append([l_r[i], l[N-i-1]])
print(*results)