#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17371                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17371                         #+#        #+#      #+#     #
#     Solved: 2024-08-23 05:02:09 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



# CVS 중 가장 가까운 점과 가장 먼 점의 거리의 평균 = 합이 가장 작은 지점을 찾아보자. 
# \min_max_{i=1}^{N} Dist(X,CVS_i)의 합이 가장 작은 x,y를 하나 뽑자. 
# N개 중 2개를 뽑는다. 
# 두 점을 잇는 일차함수를 구하고
# 그 위의 점 중 하나임.
 

from math import sqrt 

N = int(input())
CVS = [list(map(int, input().split())) for _ in range(N)]


def getDist(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


# 그냥 가장 먼 점이 가장 짧은 점

mean = float("inf")
for i in range(N):
    maxD = max([getDist(*CVS[i], *CVS[j]) for j in range(N)])
    if mean > maxD:
        mean = maxD 
        ans = CVS[i]

print(*ans)