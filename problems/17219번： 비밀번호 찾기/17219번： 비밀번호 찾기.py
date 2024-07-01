#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17219                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17219                         #+#        #+#      #+#     #
#     Solved: 2024-03-29 19:02:02 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline
N,M = map(int,input().split())
pswd = {}
for _ in range(N):
    x = input().split()
    pswd[x[0]] = x[1]
 
for _ in range(M):
    print(pswd[input().strip()])