#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11003                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11003                         #+#        #+#      #+#     #
#     Solved: 2024-07-30 00:51:26 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



# D_i = A_{max(i-L+1, 1)}~A_i 중 최솟값 
# D를 출력 


from collections import deque
import sys 

input = open(0).readline 
N, L = map(int,input().split())
A = list(map(int, input().split()))
q = deque([])
for i in range(N):
    if q and q[0][0] <= i-L:
        q.popleft()
    while q and A[i] < q[-1][1]:
        q.pop()
    q.append((i, A[i]))
    sys.stdout.write(f"{q[0][1]} ")

