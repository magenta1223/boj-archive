#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1300                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1300                          #+#        #+#      #+#     #
#     Solved: 2023-12-27 10:57:00 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
K=int(input())
start = 0
end = N*N
 
while start <= end:
    mid = (start + end) // 2
    below_mid = sum([min(mid // num_row, N) for num_row in range(1, N+1)])
 
    if below_mid >= K:
        end = mid - 1
    else:
        start = mid + 1
print(start)