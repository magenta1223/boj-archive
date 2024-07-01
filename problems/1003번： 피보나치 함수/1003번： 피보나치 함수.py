#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1003                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1003                          #+#        #+#      #+#     #
#     Solved: 2024-03-04 20:25:59 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

T = int(input())
fib = [0] * 42
fib[0] = 1
for i in range(2,42):
    fib[i] = fib[i-1] + fib[i-2]
 
for _ in range(T):
    n = int(input())
    print(fib[n], fib[n+1])