#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 5086                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/5086                          #+#        #+#      #+#     #
#     Solved: 2023-10-26 14:50:28 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

while True:
    a, b = map(int, input().split())
    if not (a+b):
        break 
    if b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")