#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 15824                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/15824                         #+#        #+#      #+#     #
#     Solved: 2024-09-26 08:16:57 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


input = open(0).readline 
MOD = 1_000_000_007 
N = int(input())
A = sorted(list(map(int, input().split())))

# 2*i를 미리 구하자 
squares = [1]
for i in range(1,N):
    squares.append((squares[i-1] * 2)%MOD)
ans = 0 
for i in range(N):
    ans += ((squares[i] - squares[N-i-1]) * A[i])%MOD  
    ans %= MOD 
print(ans)
