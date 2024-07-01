#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1014                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1014                          #+#        #+#      #+#     #
#     Solved: 2024-05-31 12:10:16 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 
 
 
def solve():
    dp = [[0] * (1<<M) for _ in range(N)]
    # 1. 첫 줄을 배치 해보자. 
    x_mask = 0 
    for i in range(M):
        if A[0][i] == "x":
            x_mask |= (1<<i) 
    
    for bitmask in range(1<<M):
        # x인 부분에는 앉을 수 없다구~
        if bitmask & x_mask:
            continue 
        # 이게 유효한지 확인 = 인접한 위치에 값이 없는가 = 하나씩 미루고 당기면 됨 
        l_shift = bitmask << 1
        r_shift = bitmask >> 1 
        if (not bitmask & l_shift) and (not bitmask & r_shift):
            # 겹치는게 없다면~ 가능 
            dp[0][bitmask] = bin(bitmask).count("1")
 
    # 마지막 줄까지 ㄱㄱ 
    for row in range(1, N):
        x_mask = 0 
        for i in range(M):
            if A[row][i] == "x":
                x_mask |= 1<<i 
        for bitmask in range(1<<M):
            # x인 부분에는 앉을 수 없다구~
            if bitmask & x_mask:
                continue 
        
            l_shift = bitmask << 1
            r_shift = bitmask >> 1
            if (not bitmask & l_shift) and (not bitmask & r_shift):
                res = 0
                for _bitmask in range(1<<M):
                    if (not _bitmask & l_shift) and (not _bitmask & r_shift):
                        res = max(res, dp[row-1][_bitmask])
                dp[row][bitmask] = bin(bitmask).count("1") + res 
    # print("ANS", max(dp[-1]))
    # for row in range(N):
    #     print("ROW", row)
    #     for bitmask in range(1<<M):
    #         if dp[row][bitmask]:
    #             print(bin(bitmask)[2:], dp[row][bitmask])
    return max(dp[-1])
 
 
ans = []
for _ in range(int(input())):
    N,M=map(int,input().split())
    A = [list(input().strip()) for _ in range(N)]
    ans.append(solve())
print(*ans, sep = '\n')