#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1069                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1069                          #+#        #+#      #+#     #
#     Solved: 2024-07-05 05:05:12 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# x,y에서 0,0까지 가려고 한다
# 걷기: 1초에 1칸
# 뛰기: T초에 D칸 

# 매턴 비교
# 걷거나 뛴다
# 뛰는 속도가 더 빠르고 남은 거리가 줄어든다면 -> 뛴다 
# 거리가 줄지 않는다면 -> 걍 걸어서 긑낸다 

# from math import sqrt 

# X,Y,D,T = map(int,input().split())

# leftDistance = sqrt(X**2 + Y**2)




import sys

x, y, d, t = map(int, sys.stdin.readline().split())
distance = (x ** 2 + y ** 2) ** 0.5
if distance >= d:
    # 점프하다 남은거리 걷기, 점프거리 2배 이하로 남기고 2번점프, 그냥 걷기 
    ans = min(t*(distance//d) + distance%d, t*(distance//d+1), distance)
else:
    # 한번 점프하고 되돌아가기, 두번 점프, 그냥 걷기 
    ans = min(t + (d - distance), 2 * t, distance)
print(ans)