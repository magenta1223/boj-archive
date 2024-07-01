#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1513                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1513                          #+#        #+#      #+#     #
#     Solved: 2024-03-26 19:33:01 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 씨발 진짜 ㅈㄴ시끄럽노 
MOD = 1_000_007
N,M,C=map(int,input().split())
COORDS = [list(map(int,input().split())) for _ in range(C)]
A = [[0] * M for _ in range(N)]
for i, (x, y) in enumerate(COORDS):
    A[x-1][y-1] = i+1
 
 
# 4차원 dp 
dp = [[[[0] * (C+1) for _ in range(C+1)] for _ in range(M)] for _ in range(N)]
 
# 첫 셀이 오락실일 경우 -> 초기화 
if A[0][0]:
    dp[0][0][A[0][0]][1] = 1 #
else:
    dp[0][0][0][0] = 1 #
 
for x in range(N):
    for y in range(M):
        if not x and not y:
            continue 
        if A[x][y]: # 오락실 
            # 번호 A[x][y]미만인 경우에만 추가 가능 -> 최대 갯수 역시 A[x][y] 
            for l in range(A[x][y]):
                for k in range(l+1):
                    dp[x][y][A[x][y]][k+1] += (dp[x-1][y][l][k] + dp[x][y-1][l][k])
                    dp[x][y][A[x][y]][k+1] %= MOD
 
        else: # 오락실 아님.  전부 가능 
            for l in range(C+1):
                for k in range(l+1):
                    dp[x][y][l][k] = (dp[x-1][y][l][k] + dp[x][y-1][l][k]) % MOD 
 
print(*[sum([ dp[-1][-1][n][c]   for n in range(C+1)]) % MOD for c in range(C+1) ])
 