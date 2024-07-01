#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1102                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1102                          #+#        #+#      #+#     #
#     Solved: 2024-05-28 12:49:20 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline
INF = float("inf")
 
N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]
STATUS = input()
P = int(input())
 
init_mask, count = 0, STATUS.count("Y")
for i in range(N):
    if STATUS[i]=="Y":
        init_mask |= (1<<i)
        
if P-count <=0 :
    print(0)
    quit()
elif count == 0:
    print(-1)
    quit()
 
dp = [[INF  for _ in range(2**N) ] for _ in range(P-count+1)]
dp[0][init_mask] = 0
 
for bitmask in range(init_mask, 1<<N):
    for p in range(1,P-count+1):    
        if dp[p-1][bitmask] == INF:
            continue
        for frm in range(N) :
            if bitmask & (1<<frm): 
                for to in range(N):
                    if frm==to or bitmask & (1<<to):
                        continue
                    next_bitmask = bitmask | (1<<to)
                    dp[p][next_bitmask] = min(dp[p][next_bitmask], dp[p-1][bitmask] + C[frm][to])
 
print(min(dp[P-count]))