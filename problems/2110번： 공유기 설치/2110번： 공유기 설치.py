#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2110                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2110                          #+#        #+#      #+#     #
#     Solved: 2023-12-26 14:49:58 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,C=map(int, input().split())
X=sorted([int(input()) for _ in range(N)])
 
start, end = 1, max(X)
while start <= end:
    mid = (start + end) // 2
    c = 0 
    prev = -mid
    for i in range(N):
        x = X[i]
        if x >= prev + mid:
            prev = x
            c += 1
    if C > c: 
        end = mid-1
    else: 
        start = mid + 1 
print(end)