#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2805                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2805                          #+#        #+#      #+#     #
#     Solved: 2023-12-26 14:11:16 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M=map(int, input().split())
l=list(map(int, input().split()))
start,end = 1, max(l)
while start <= end:
    mid = (start + end) // 2
    v = sum([max(el - mid, 0) for el in l])    
    if v == M: 
        end = mid
        break 
    elif v > M:
        start = mid + 1
    else:
        end = mid - 1
print(end)