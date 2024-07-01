#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1011                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1011                          #+#        #+#      #+#     #
#     Solved: 2024-07-01 02:03:45 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 이전 이동거리가 k일때 k-1~k+1만큼만 이동할 수 있다. 
# x에서 y로 이동하는 최소 횟수
# 처음 시작 및 y도착 시 속도는 반드시 1 

from math import sqrt 

T = int(input())
INF = float("inf")


for _ in range(T):
    x,y = map(int,input().split())
    x,y = 0,y-x

    n = int(sqrt(y))
    ans = 2*n-1
    y -= n**2 
    for i in range(n,0,-1):
        if not y:
            break 
        if y >= i:
            move, y = divmod(y, i)
            ans += move 
    print(ans)
        



"""
4
0 3
1 5
45 50
0 2147483648

"""