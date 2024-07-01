#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1915                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1915                          #+#        #+#      #+#     #
#     Solved: 2024-06-10 12:27:55 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 
 
N,M = map(int,input().split())
A = [list(map(int,list(input().strip()))) for _ in range(N)]
 
# cumsum 
CS = [[0] * (M+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,M+1):
        CS[i][j] = A[i-1][j-1] + CS[i][j-1] + CS[i-1][j] - CS[i-1][j-1]
 
 
maxlen = 0
for i in range(1,N+1):
    for j in range(1,M+1):
        if not A[i-1][j-1]:
            continue
        res = maxlen 
        # 현재 i,j에서 가능한 길이 
        for l in range(maxlen, min(N+2-i, M+2-j)):
            # 그 길이로 만들어지는 정사각형에 들어있는 1의 개수 
            s = CS[i+l-1][j+l-1] - CS[i-1][j+l-1] - CS[i+l-1][j-1] + CS[i-1][j-1]
            if s == l**2:
                res = l 
            else:
                break 
        
        maxlen = res 
 
print(maxlen**2)