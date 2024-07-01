#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11000                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11000                         #+#        #+#      #+#     #
#     Solved: 2024-05-23 17:45:14 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from heapq import heappop, heappush
input = open(0).readline 
 
N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
A.sort()
 
heap = []
heappush(heap, A[0][1])  
for i in range(1, N):
    a, b = A[i]
    # 가장 빨리 비는 회의실의 종료 시간과 비교
    if heap[0] <= a:
        heappop(heap)  # 기존 회의실을 사용하므로 종료 시간을 제거
    heappush(heap, b)  # 새로운 회의의 종료 시간을 추가
print(len(heap))