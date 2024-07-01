#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1018                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1018                          #+#        #+#      #+#     #
#     Solved: 2024-04-01 15:37:39 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M = map(int,input().split())
B = [input().strip() for _ in range(N)]
rows = ['BWBWBWBW', 'WBWBWBWB']
def calc(i,j):
    res = sum([sum([ B[row][m] != rows[row%2][m-j] for m in range(j, j+8)]) for row in range(i,i+8)])
    return min(res, 64-res)
 
ans = N*M
for i in range(N-7):
    for j in range(M-7):
        ans = min(calc(i,j), ans)
print(ans)