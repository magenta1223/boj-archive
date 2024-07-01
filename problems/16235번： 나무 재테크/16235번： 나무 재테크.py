#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 16235                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/16235                         #+#        #+#      #+#     #
#     Solved: 2024-02-15 16:37:27 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M,K=map(int, input().split())
A = [ list(map(int, input().split())) for _ in range(N)]
Trees = [list(map(int, input().split())) for _ in range(M)]
 
NUTRITION = [[5] * N for _ in range(N)]
TREES = [[[] for _ in range(N)] for _ in range(N)]
D = [(1,0), (1,1), (0,1), (-1, 1), (-1,0), (-1, -1), (0, -1),(1, -1)]
 
for x, y, z in Trees:
    TREES[x-1][y-1].append(z)
    
for _ in range(K):
    # 봄 여름
    for i in range(N):
        for j in range(N):
            TREES[i][j] = sorted(TREES[i][j])
            next_t = []
            k = 0    
            while k < len(TREES[i][j]):
                t = TREES[i][j][k]
                if NUTRITION[i][j] >= t:
                    NUTRITION[i][j] -= t
                    next_t.append(t+1)
                    k += 1
                else:
                    break           
            for h in range(k, len(TREES[i][j])):
                NUTRITION[i][j] += TREES[i][j][h] // 2                
            TREES[i][j]=next_t
            
    # 가을 겨울  
    for i in range(N):
        for j in range(N):
            for t in TREES[i][j]:
                if not t % 5:
                    for dx, dy in D:
                        if 0<=i+dx<N and 0<=j+dy<N:
                            TREES[i+dx][j+dy].append(1)
            NUTRITION[i][j] += A[i][j]
 
ans = 0
for i in range(N):
    for j in range(N):
        ans += len(TREES[i][j])
        
print(ans)