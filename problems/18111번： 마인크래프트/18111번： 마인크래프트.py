#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 18111                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/18111                         #+#        #+#      #+#     #
#     Solved: 2024-06-14 15:23:11 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M,B = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
 
from math import ceil, floor 
S = sum([sum(row) for row in A]) / (N*M)
 
ceilX = ceil(S)
floorX = floor(S)
 
# ceilX로 만들어보자. 
 
def get_ans(left, criterion):
    ans = 0
    left = B 
    for i in range(N):
        for j in range(M):
            if A[i][j] > criterion:
                n = A[i][j] - criterion
                ans += 2*n 
                left += n 
            elif A[i][j] < criterion:
                n = criterion-A[i][j]
                ans += n 
                left -= n 
    return ans if left >=0 else float("inf"), left
 
ans, ans_height = float("inf"), -1 
for i in range(257):
    res, left = get_ans(B, i)
    if res <= ans:
        ans = res 
        ans_height = i 
 
print(ans, ans_height)