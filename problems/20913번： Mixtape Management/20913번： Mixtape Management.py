#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 20913                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/20913                         #+#        #+#      #+#     #
#     Solved: 2024-06-17 11:34:30 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
A = list(map(int,input().split()))
ANS = [0] * N 
 
idx = A.index(1)
ANS[idx] = idx+1 
 
 
for i in range(N):
    ANS[i] = int("1" + str(i).zfill(100) + "0"*A[i]) 
print(*ANS)