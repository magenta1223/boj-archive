#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 8895                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/8895                          #+#        #+#      #+#     #
#     Solved: 2024-06-04 18:43:38 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def solve(n,l,r):
    l,r = l, r 
    dp = [[[0] * (n+1) for _ in range(n+1)] for _ in range(n+1)]
    
    # 큰 것 부터 배치
    # 1개 배치. 좌우에서 1개씩 보임 
    dp[1][1][1] = 1 
    
    for k in range(2,n+1):
        # for i in range(1,k+1):
        #     for j in range(1,k+1):
        for i in range(1,min(k,l)+1):
            for j in range(1,min(k,r)+1):
                # 현재 배치한 막대는 가장 작으므로, 가장 왼쪽 or 오른쪽이 아니면 보이지 않음. 
                if i == j == 1:
                    continue
                # L:i, R:j를 만드는 방법
                # 지금까지 배치한 k-1개의 막대에 대해  
                # 1) L:i-1, R:j의 가장 왼쪽에 추가 
                # 2) L:i, R:j+1의 가장 오른쪽에 추가 
                # 3) L:i, R:j의 가장 왼쪽/오른쪽 제외, 아무데나 추가 
                dp[k][i][j] = dp[k-1][i-1][j] + dp[k-1][i][j-1] + dp[k-1][i][j] * (k-2)
    return dp[-1][l][r]
 
ans = []
for _ in range(int(input())):
    n,l,r = map(int,input().split())
    ans.append(solve(n,l,r))
 
print(*ans,sep='\n')
 