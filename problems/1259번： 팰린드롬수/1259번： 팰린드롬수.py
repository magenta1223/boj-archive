#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1259                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1259                          #+#        #+#      #+#     #
#     Solved: 2024-04-04 14:22:13 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

while True:
    N = input().strip()
    if N == "0":
        break 
    print("yes" if N == N[::-1] else "no")