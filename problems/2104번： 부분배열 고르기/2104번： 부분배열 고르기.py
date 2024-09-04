#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2104                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2104                          #+#        #+#      #+#     #
#     Solved: 2024-09-02 04:11:27 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
A = list(map(int, input().split()))

S = [0] * (N+1)
for i in range(1,N+1):
    S[i] = S[i-1] + A[i-1]

ans = 0
stack = []

for i in range(N):
    while stack and A[stack[-1]] >= A[i]:
        height = A[stack.pop()]
        ans = max(ans, height * (S[i] - S[stack[-1] + 1 if stack else 0]))
    stack.append(i)

while stack:
    height = A[stack.pop()]
    ans = max(ans, height * (S[N] - S[stack[-1] + 1 if stack else 0]))

print(ans)
