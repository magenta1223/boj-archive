#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1193                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1193                          #+#        #+#      #+#     #
#     Solved: 2023-10-26 13:59:26 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

X = int(input())
 
i = 0
a = 0
while True:
    a += 1
    i += a
    if i >= X:
        break 
if a % 2:
    print(f"{i-X+1}/{X-i+a}")
else:
    print(f"{X-i+a}/{i-X+1}")