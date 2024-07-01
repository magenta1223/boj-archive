#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11401                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11401                         #+#        #+#      #+#     #
#     Solved: 2023-12-21 18:43:54 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

MOD = 1000000007
 
def mod_inv(a, p=MOD):
    return pow(a, p-2, p)
 
def binomial_coefficient(n, k, p=MOD):
    if k < 0 or k > n:
        return 0
 
    numerator = 1
    for i in range(n, n-k, -1):
        numerator = (numerator * i) % p
 
    denominator = 1
    for i in range(1, k+1):
        denominator = (denominator * i) % p
 
    return (numerator * mod_inv(denominator)) % p
 
N, K = map(int, input().split())
print(binomial_coefficient(N, K))
 