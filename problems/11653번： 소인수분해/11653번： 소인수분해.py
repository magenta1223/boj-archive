#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11653                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11653                         #+#        #+#      #+#     #
#     Solved: 2023-10-26 14:46:10 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
if N > 1:
    while True:
        for i in range(2, N+1):
            if N % i == 0:
                print(i)
                break 
        N //= i
        isPrime = True
        for j in range(2, N):
            if N % j == 0:
                isPrime = False
                break 
        if isPrime and N > 1:
            print(N)
            break 
        if N == 1:
            break