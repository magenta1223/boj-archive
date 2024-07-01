#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 25682                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/25682                         #+#        #+#      #+#     #
#     Solved: 2023-12-20 18:13:08 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M,K=map(int, input().split())
B = [input() for _ in range(N)]
tile = "BW"
board_B = [[ tile[(i+j)%2] for i in range(M)] for j in range(N)]
V_B = [[0 for _ in range(M+1)] for _ in range(N+1)]  
 
for i in range(1, N+1):
    for j in range(1, M+1):
        # board의 값이 board_B와 다르면
        V_B[i][j] = V_B[i-1][j] + V_B[i][j-1] - V_B[i-1][j-1] + (B[i-1][j-1] != board_B[i-1][j-1]) # B로 시작하는 보드와 다름. +1
 
min_changes = float('inf')
for i in range(N-K+1):
    for j in range(M-K+1):
        x1, y1 = i,j
        x2, y2 = i+K, j+K        
        change_B = V_B[x2][y2] - V_B[x2][y1] - V_B[x1][y2] + V_B[x1][y1]
        min_changes = min(min_changes, change_B, K**2 - change_B)
print(min_changes)
 