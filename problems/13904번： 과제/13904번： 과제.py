#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 13904                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/13904                         #+#        #+#      #+#     #
#     Solved: 2024-07-29 03:48:27 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



# 하루에 과제 한개
# 과제마다 마감일이 존재
# 과제마다 얻을 수 있는 점수가 존재
# 점수를 최대한 땡겨보자 

from heapq import heappop, heappush 
input = open(0).readline 
N = int(input())
HW = [list(map(int, input().split())) for _ in range(N)]
HW.sort()

h = []
for d,w in HW:
    heappush(h, w) 
    while h and len(h) > d:
        heappop(h)
print(sum(h))