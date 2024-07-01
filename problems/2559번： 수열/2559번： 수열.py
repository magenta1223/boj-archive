#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2559                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2559                          #+#        #+#      #+#     #
#     Solved: 2023-12-20 15:12:07 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,K=map(int, input().split())
l=list(map(int, input().split()))
ksum=[0] * (N-K+1)
ksum[0] = sum(l[:K])
for i in range(K, N):
    ksum[i-K+1] = ksum[i-K] - l[i-K] + l[i]
print(max(ksum))