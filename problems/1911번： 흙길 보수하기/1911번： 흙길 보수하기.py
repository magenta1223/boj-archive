#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1911                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1911                          #+#        #+#      #+#     #
#     Solved: 2024-07-18 08:01:35 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


from heapq import heappop, heappush 
input = open(0).readline 

N,L = map(int,input().split())
heap = []
for _ in range(N):
    a,b = map(int,input().split())
    heappush(heap, (-b,a))
    
covered = float("inf")
ans = 0 
while heap:
    b,a = heappop(heap)
    b  = -b
    if covered <= a:
        continue 

    if covered >= b:
        covered = b
        
    while covered > a:
        covered -= L 
        ans += 1 

print(ans)
