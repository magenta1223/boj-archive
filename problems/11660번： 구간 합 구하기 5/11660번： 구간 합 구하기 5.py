#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11660                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11660                         #+#        #+#      #+#     #
#     Solved: 2023-12-20 17:16:31 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import os, io, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
N,M=map(int, input().split())
arr = [ list(map(int, input().split())) for _ in range(N)]
 
cumsum = [[0 for _ in range(N+1)] for _ in range(N+1)]  
for i in range(1,N+1):
    for j in range(1,N+1):
        cumsum[i][j] = cumsum[i-1][j] + cumsum[i][j-1] - cumsum[i-1][j-1] + arr[i-1][j-1]
 
ans = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans.append(cumsum[x2][y2] - cumsum[x2][y1-1] - cumsum[x1-1][y2] + cumsum[x1-1][y1-1])
    
sys.stdout.write('\n'.join(map(str, ans)))
 