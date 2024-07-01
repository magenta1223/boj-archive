#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2566                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2566                          #+#        #+#      #+#     #
#     Solved: 2023-10-17 15:47:21 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

max_value = 0
max_index = (-999, -999)
for i in range(9):
    line = list(map(int, input().split()))
    if max(line) >= max_value:
        max_value = max(line)
        max_index = (i + 1, line.index(max_value) + 1)
print(max_value)
print(max_index[0], max_index[1])