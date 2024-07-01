#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1655                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1655                          #+#        #+#      #+#     #
#     Solved: 2024-02-27 13:00:49 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from heapq import heappush, heappop
input = open(0).readline
N=int(input().strip())
l = [int(input().strip()) for _ in range(N)]
minheap = []
maxheap = []
 
for i in range(N):
    n = l[i]
    if len(minheap) == len(maxheap):
        heappush(maxheap, -n)
    else:
        heappush(minheap, n)
    if minheap:
        # print("루트", minheap[0])
        _min, _max = heappop(minheap), heappop(maxheap)
        # print("팝", _min)
        if - _max > _min:
            heappush(minheap, -_max)
            heappush(maxheap, -_min)
        else:
            heappush(minheap, _min)
            heappush(maxheap, _max)
        print(-maxheap[0])
    else:
        print(n)
 