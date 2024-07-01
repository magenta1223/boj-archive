#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1978                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1978                          #+#        #+#      #+#     #
#     Solved: 2023-10-26 14:31:28 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
numbers = list(map(int, input().split()))
nPrime = sum(1 for n in numbers if n > 1 and all(n % i != 0 for i in range(2, n)))
print(nPrime)
 