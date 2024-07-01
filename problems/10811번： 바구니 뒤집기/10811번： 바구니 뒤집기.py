#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10811                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10811                         #+#        #+#      #+#     #
#     Solved: 2023-10-17 14:42:33 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N, M = map(int, input().split())
array = [str(i+1) for i in range(N)]
 
for idx in range(M):
    i, j = map(int, input().split())
    array[i-1:j] = array[i-1:j][::-1]
    
print(" ".join(array))