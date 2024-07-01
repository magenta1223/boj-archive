#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11054                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11054                         #+#        #+#      #+#     #
#     Solved: 2023-12-19 23:45:00 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
l=list(map(int, input().split()))
dp_inc = [1] * N 
dp_dec = [1] * N 
for i in range(N):
    for j in range(i):
        if l[i] != l[j]:
            if l[i] > l[j]:
                dp_inc[i] = max(dp_inc[i], dp_inc[j]+1)
            else:
                dp_dec[i] = max(dp_dec[i], dp_inc[j] + 1, dp_dec[j] + 1)
print(max(dp_inc + dp_dec))