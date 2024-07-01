#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10810                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10810                         #+#        #+#      #+#     #
#     Solved: 2023-10-17 14:37:37 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N, M = map(int, input().split())
array = ["0" for _ in range(N)]
 
for idx in range(M):
    i, j, k = map(int, input().split())
    array[i-1:j] = [str(k)] * (j+1 - i)
    
print(" ".join(array))