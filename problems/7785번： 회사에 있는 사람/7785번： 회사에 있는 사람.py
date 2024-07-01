#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 7785                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/7785                          #+#        #+#      #+#     #
#     Solved: 2023-11-02 13:45:47 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
input = sys.stdin.readline
N = int(input())
s = set()
for _ in range(N):
    p, e = input().split()
    if e == "enter":
        s.add(p)
    else:
        s.remove(p)
print(*sorted(s, reverse= True), sep='\n')