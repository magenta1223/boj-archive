#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2305                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2305                          #+#        #+#      #+#     #
#     Solved: 2024-04-23 16:47:29 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def sit(idx, p2, p1, occ):
    # occ : occupied 
 
    # 0: 제자리
    # 1: 자유석이 아닌 왼쪽자리
    # 2: 자유석이 아닌 오른쪽자리
    # 3: 자유석 
    if idx == N-1: # 모두 앉음  
        return 1
 
    if dp[idx][p2][p1][occ] != -1:
        return dp[idx][p2][p1][occ]
    
    dp[idx][p2][p1][occ] = 0
    left, right = seats[idx]-1, seats[idx]+1
 
    # 제자리에 앉을 수 있는 경우
    if p1 != 2:
        dp[idx][p2][p1][occ] += sit(idx+1, p1, 0, occ)
 
    # 왼쪽 좌석이 자유석이 아니고 앉을 수 있는 경우
    if p1 != 0 and p2 != 2:
        if left >= 1 and not isFree[left]:
            dp[idx][p2][p1][occ] += sit(idx+1, p1, 1, occ)
 
    # 오른쪽 좌석이 자유석이 아니고 앉을 수 있는 경우
    if right <= N and not isFree[right]:
        dp[idx][p2][p1][occ] += sit(idx+1, p1, 2, occ)
 
    # 자유석이 비어있는 경우
    if not occ:
        dp[idx][p2][p1][occ] += sit(idx+1, p1, 3, 1)
 
    return dp[idx][p2][p1][occ]
 
N,K = int(input()), int(input())
isFree = {i : True if i == K else False for i in range(1,N+1)}
seats = list(range(1,N+1))
seats.remove(K)
dp = [[[[-1] * 2 for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
print(sit(0, -1, -1, 0))