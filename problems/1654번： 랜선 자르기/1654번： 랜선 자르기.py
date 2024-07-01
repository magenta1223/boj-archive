#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1654                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1654                          #+#        #+#      #+#     #
#     Solved: 2023-12-26 13:22:25 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
input = sys.stdin.readline
K,N=map(int, input().split())
l = [ int(input()) for _ in range(K)]
start = 1
end = max(l)
while start <= end:
    mid = (start + end) // 2
    num_pieces = sum([ el // mid for el in l])
    if num_pieces >= N: 
        start = mid + 1
    else :
        end = mid - 1
print(end)