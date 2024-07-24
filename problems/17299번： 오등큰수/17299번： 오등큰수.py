#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17299                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17299                         #+#        #+#      #+#     #
#     Solved: 2024-07-24 06:47:28 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 오등큰수 NGF 
# F(A_i) = A_i가 A에서 등장한 횟수
# NGF_i = 오른쪽에 있으면서 F(x)가 F(A_i)보다 큰 수 중 가장 왼쪽에 있는 수 

from collections import Counter 

N = int(input())
A = list(map(int,input().split()))
C = Counter(A)
NGF = [-1] * N 

stack = []
for i in range(N):
    while stack and C[A[stack[-1]]] < C[A[i]]:
        NGF[stack.pop()] = A[i]
    stack.append(i)
print(*NGF)