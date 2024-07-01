#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1028                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1028                          #+#        #+#      #+#     #
#     Solved: 2024-04-27 12:36:04 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M = map(int, input().split())
A = [[0] + list(map(int, list(input().strip()))) + [0] for _ in range(N)]
A = [[0] * (M+2)] + A + [[0] * (M+2)]
 
ld = [[0] * (M+2) for _ in range(N+2)] # 현재 셀에서 left down 방향으로 연속인 1의 개수 저장 
rd = [[0] * (M+2) for _ in range(N+2)]
lu = [[0] * (M+2) for _ in range(N+2)]
ru = [[0] * (M+2) for _ in range(N+2)]
 
for i in range(N, 0, -1):
    for j in range(1, M+1):
        if A[i][j] == 1:
            ld[i][j] = ld[i+1][j-1] + 1
            rd[i][j] = rd[i+1][j+1] + 1
 
for i in range(1, N+1):
    for j in range(1, M+1):
        if A[i][j] == 1:
            lu[i][j] = lu[i-1][j-1] + 1
            ru[i][j] = ru[i-1][j+1] + 1
 
ans = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        # 기존 값보다 크면서, left down, right down 중 작은 값 = 최대 크기의 다이아몬드까지 진행 
        maxlen = min(ld[i][j], rd[i][j])
        if ans >= maxlen:
            continue
        for k in range(ans, maxlen+1):
            bottom = i + (k-1)*2 
            if bottom > N+1: # 범위초과 
                break
            # 맨 아래에서 k개만큼 좌/우로 올라갈 수 있는지 
            if A[bottom][j] and lu[bottom][j] >= k and ru[bottom][j] >=k:
                ans = k
print(ans)