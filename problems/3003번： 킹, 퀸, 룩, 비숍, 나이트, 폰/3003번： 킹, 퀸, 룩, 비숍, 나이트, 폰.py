#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 3003                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/3003                          #+#        #+#      #+#     #
#     Solved: 2023-10-17 14:47:26 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

n_obj = list(map(int, input().split(" ")))
target = [1, 1, 2, 2, 2, 8]
print(" ".join(  [  str(t-n) for n, t in zip(n_obj, target)   ]   ))