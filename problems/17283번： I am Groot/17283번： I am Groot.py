#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17283                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17283                         #+#        #+#      #+#     #
#     Solved: 2024-07-19 02:59:14 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

L, R = int(input()), int(input())
ans = -L
n = 1 
while L > 5:
    ans += n*L 
    n*=2 
    L = int(L*R/100)
print(ans)