#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10986                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10986                         #+#        #+#      #+#     #
#     Solved: 2023-12-20 16:26:14 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M=map(int, input().split())
l=list(map(int, input().split()))
csum=0
numRemainder = [0] * M
for el in l:
    csum += el
    numRemainder[csum%M] += 1
count = numRemainder[0]
for i in numRemainder:
    count += i * (i-1) // 2
print(count)