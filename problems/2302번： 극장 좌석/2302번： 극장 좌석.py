#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2302                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2302                          #+#        #+#      #+#     #
#     Solved: 2024-03-18 15:06:08 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M=int(input()), int(input())
VIP = [int(input()) for _ in range(M)] + [N+1]
fib = [1] * (N+1) 
fib[1] = 1
for i in range(2,N+1):
    fib[i] = fib[i-2] + fib[i-1]
 
ans, prev_vip = 1, 1
for vip in VIP:
    ans *= fib[vip-prev_vip]
    prev_vip = vip+1 
print(ans)