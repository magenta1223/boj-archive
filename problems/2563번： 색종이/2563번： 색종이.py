#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2563                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2563                          #+#        #+#      #+#     #
#     Solved: 2023-10-17 16:16:26 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
xs, ys = [], []
for _ in range(N):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
array = [ [0 for _ in range(max(ys) + 10)]  for _ in range(max(xs) + 10)]
for x, y in zip(xs, ys):
    for i in range(x, x+ 10):
        for j in range(y, y+10):
            array[i][j] = 1            
print(sum([sum(l) for l in array]))