#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11403                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11403                         #+#        #+#      #+#     #
#     Solved: 2024-03-29 18:43:27 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 모든 정점에서 정점 사이의 도달 여부를 체크 = 플로이드 와샬 
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
 
for k in range(N):
    # 라운드 
    for i in range(N):
        for j in range(N):
            # i에서 j로 k를 거쳐서 갈 수 있는지 
            if A[i][k] and A[k][j]:
                A[i][j] = 1 
for row in A:
    print(*row)