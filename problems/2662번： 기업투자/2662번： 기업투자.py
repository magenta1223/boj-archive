#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2662                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2662                          #+#        #+#      #+#     #
#     Solved: 2024-08-13 02:57:02 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 그리디하게는 불가능. dp

# 기업 번호 순서대로 투자 액수를 결정
# 총 N만큼 투자. 
# 투자를 얼마나 할지 결정 -> 넘겨~ 


N,M = map(int,input().split())    
A = [[0]*M] + [list(map(int,input().split()))[1:] for _ in range(N)]

dp = [[-1] * (N+1) for _ in range(M)]
backtrack = [[-1] * (N+1) for _ in range(M)]


def dfs(left, i):
    if i ==  M:
        return 0 
    
    if dp[i][left] != -1:
        return dp[i][left]
    
    res = -1 
    bt = 0 
    for invest in range(left+1):
        _res = dfs(left-invest, i+1) + A[invest][i]
        if res < _res:
            res = _res 
            bt = invest

    dp[i][left] = res 
    backtrack[i][left] = bt 
    return dp[i][left]


ans = dfs(N,0)
investments = []
idx, left = 0,N
while idx < M and backtrack[idx][left] != -1:
    invest = backtrack[idx][left]
    idx += 1
    left -= invest 
    investments.append(invest)

print(ans)
print(*investments)



"""
4 3
1 5 1 3
2 6 5 5
3 7 9 7
4 10 12 10

"""