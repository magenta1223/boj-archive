#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1016                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1016                          #+#        #+#      #+#     #
#     Solved: 2024-06-10 11:18:43 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from math import sqrt 
 
MIN,MAX = map(int,input().split())
 
N = int(sqrt(MAX))+1
prime_numbers = [True] * N
for i in range(2,N):
    for j in range(2,N//i):
        prime_numbers[i*j] = False 
S = [i**2 for i in range(2,N) if prime_numbers[i]]
M = len(S)
 
X = [True] * (MAX+1-MIN)
for i in range(M):
    s = S[i]
    # MIN 이상 MAX 이하 s의 배수를 전부 지워버리면 됨. 
    start, r = divmod(MIN, s)
    if r:
        start += 1 
    end, r = divmod(MAX, s)
    for j in range(start, end+1):
        x = s*j - MIN
        X[x] = False 
 
print(sum(X))