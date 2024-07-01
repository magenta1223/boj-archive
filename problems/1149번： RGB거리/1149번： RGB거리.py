#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1149                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1149                          #+#        #+#      #+#     #
#     Solved: 2023-12-18 22:37:00 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
costs = []
for _ in range(N):
    costs.append(list(map(int, input().split())))
 
# 최소비용 구하기 
# 1번부터 칠하고 -> 이전것 과 다른 색 중 비용 작은걸로 고르기 
array = [[0 for _ in range(3)] for _ in range(N)]
array[0] = costs[0]
for i in range(1, N):
    R,G,B=costs[i]
    array[i][0] = min(array[i-1][1], array[i-1][2]) + R
    array[i][1] = min(array[i-1][0], array[i-1][2]) + G
    array[i][2] = min(array[i-1][0], array[i-1][1]) + B
    
print(min(array[-1]))