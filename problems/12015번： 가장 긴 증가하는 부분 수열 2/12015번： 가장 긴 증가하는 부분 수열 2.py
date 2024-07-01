#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 12015                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/12015                         #+#        #+#      #+#     #
#     Solved: 2023-12-26 17:04:42 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from bisect import bisect_left
import sys 
input = sys.stdin.readline
 
def length_of_lis(seq):
    if not seq:
        return 0
 
    lis = []
    for num in seq:
        pos = bisect_left(lis, num)
        if pos == len(lis):
            lis.append(num)
        else:
            lis[pos] = num
 
    return len(lis)
 
N = int(input())
l = list(map(int, input().split()))
print(length_of_lis(l))