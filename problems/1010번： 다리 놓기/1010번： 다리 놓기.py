#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1010                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1010                          #+#        #+#      #+#     #
#     Solved: 2023-11-22 16:50:13 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def factorial(N):
    if N > 1:
        return (N * factorial(N-1))
    else:
        return 1
 
T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    print (factorial(M) //  (factorial(M-N) * factorial(N)))