#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2217                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2217                          #+#        #+#      #+#     #
#     Solved: 2024-05-23 12:31:35 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 
N=int(input())
A=[int(input()) for _ in range(N)]
A.sort()
 
ans = 0
for i in range(N):
    ans = max(ans, A[i] * (N-i))
print(ans)