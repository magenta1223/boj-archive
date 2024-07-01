#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1764                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1764                          #+#        #+#      #+#     #
#     Solved: 2023-11-02 14:46:36 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
input = sys.stdin.readline
 
N, M = map(int, input().split())
s0 = { input().strip() for _ in range(N)}
s1 = { input().strip() for _ in range(M)}
inter = sorted(list(s0 & s1))
print(len(inter))
# print(*inter, sep = "\n")
for i in inter:
    print(i)