#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2075                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2075                          #+#        #+#      #+#     #
#     Solved: 2024-05-09 12:14:15 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
A = [list(map(int,input().split())) for _ in range(N)]
A = [list(row) for row in zip(*A)]
idx = 0
while idx < N:
    _max = - float("inf")
    for i in range(N):
        if A[i][-1] > _max:
            _max = A[i][-1]
            col_idx = i 
    ans = A[col_idx].pop()
    idx += 1 
print(ans)
 