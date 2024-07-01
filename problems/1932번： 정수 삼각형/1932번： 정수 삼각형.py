#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1932                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1932                          #+#        #+#      #+#     #
#     Solved: 2023-12-18 23:03:18 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
array = []
for i in range(N):
    array.append( list(map(int, input().split())) + [0] * (N-i-1) )
for i in range(1, N):
    for j in range(i+1):
        array[i][j] += max(array[i-1][j-1], array[i-1][j])
print(max(array[-1]))