#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11025                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11025                         #+#        #+#      #+#     #
#     Solved: 2024-05-14 10:37:25 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,K=map(int,input().split())
ans = 1 
for i in range(2,N+1):
    ans = (ans+K-1) % i + 1
print(ans)