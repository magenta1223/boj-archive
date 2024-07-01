#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11689                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11689                         #+#        #+#      #+#     #
#     Solved: 2024-05-07 20:49:15 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from math import sqrt 
 
N = int(input())
M = int(sqrt(N))+1
prime = [True] * M
 
for i in range(2,M):
    if not prime[i]:
        continue 
    for j in range(i*2,M,i):
        prime[j] = False 
prime_numbers = [i for i in range(M-1,1,-1) if prime[i]]
 
ans = 1 
while N > 1 and prime_numbers:
    p,c = prime_numbers.pop(), 0
    while not N % p:
        N //= p 
        c += 1 
    if c:
        ans *= (p ** (c-1))*(p-1)
 
if N > 1:
    ans *= (N-1)
print(ans)