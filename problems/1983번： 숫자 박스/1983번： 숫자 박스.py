#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1983                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1983                          #+#        #+#      #+#     #
#     Solved: 2024-03-27 19:23:31 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
A = [el for el in list(map(int,input().split())) if el]
B = [el for el in list(map(int,input().split())) if el]
ZA = N-len(A)+1 # 0의 개수 
ZB = N-len(B)+1 # 0의 개수 
LA, LB = len(A), len(B)
dp = [[0]*ZB for _ in range(ZA)]
 
for i in range(N): # 모든 자릿수에 대해 
    for r in range(ZA-1, -1, -1): # A의 0 개수
        for c in range(ZB-1, -1, -1): # B의 0개수 
            if 0 <= i-r < LA and 0 <= i-c < LB:
                tmp = [dp[r][c] + A[i-r]*B[i-c]]
                if r: # 0을 1개 이상 썼으면 
                    tmp.append(dp[r-1][c])
                if c:
                    tmp.append(dp[r][c-1])
                dp[r][c] = max(tmp)
 
print(max(max(row) for row in dp))