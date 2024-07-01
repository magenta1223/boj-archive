#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 7453                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/7453                          #+#        #+#      #+#     #
#     Solved: 2024-07-01 03:21:44 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


input = open(0).readline 

N = int(input())
A,B,C,D = zip(*[list(map(int, input().split())) for _ in range(N)])

counter = dict()
for i in range(N):
    for j in range(N):
        v = A[i]+B[j]
        if v in counter:
            counter[v] += 1 
        else:
            counter[v] = 1

ans = 0
for i in range(N):
    for j in range(N):
        v = C[i]+D[j]
        if -v in counter:
            ans += counter[-v]

print(ans)

