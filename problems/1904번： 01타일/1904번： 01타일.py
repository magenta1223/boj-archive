#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1904                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1904                          #+#        #+#      #+#     #
#     Solved: 2023-12-18 21:49:43 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
f = [0 for i in range(N+1)]
def fibonacci(n):
    global f
    f[0] = f[1] = 1
    for i in range(2, N+1):
        f[i] = (f[i-1] + f[i-2]) % 15746
    return f[n-1]
fibonacci(N)
print(f[-1] % 15746)