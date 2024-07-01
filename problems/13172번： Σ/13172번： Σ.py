#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 13172                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/13172                         #+#        #+#      #+#     #
#     Solved: 2024-04-04 12:27:40 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 
MOD = 1_000_000_007
 
def mod_inv(x, p):
    return pow(x, p-2, p)
 
M=int(input())
ans = 0 
for _ in range(M):
    n,s = map(int,input().split())
    x = (mod_inv(n, MOD) * s) % MOD  
    ans = (ans + x) % MOD  
 
print(ans)