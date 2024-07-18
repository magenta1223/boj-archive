#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1826                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1826                          #+#        #+#      #+#     #
#     Solved: 2024-07-18 08:24:52 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 1km에 1L씩 연료가 샌다.
# 수리를 위해서 L거리에 있는 마을에 가려고 한다. 
# 그 수직선상에 N개의 주유소가 있다. a는 그 위치, b는 기름의 양
# 최소 횟수만큼 정차해서 L까지 가려고 한다. 
# 초기 연료량은 P 

from heapq import heappop, heappush 

input = open(0).readline 
N = int(input())

GAS = []
for _ in range(N):
    a,b = map(int,input().split())
    GAS.append((a,b))
L, P = map(int,input().split())
GAS.append((L,0))
GAS.sort()

x = 0 
ans = 0 
heap = []

for a,b in GAS:
    while heap and a-x > P:
        ans += 1 
        P -= heappop(heap)
    if P>=a-x:
        P -= a-x
        x = a 
        heappush(heap, (-b)) 
    else:
        break 
else:
    print(ans)
    exit(0)

print(-1)

"""

4
4 4
5 2
11 5
15 10
25 4

"""