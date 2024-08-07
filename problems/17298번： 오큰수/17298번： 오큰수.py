#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17298                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17298                         #+#        #+#      #+#     #
#     Solved: 2024-07-24 05:13:25 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 오큰수 = NGE 를 찾자 
# NGE(i) = i번째 보다 
# 1) 오른쪽이면서
# 2) A_i보다 큰 수 중 
# 3) 가장 왼쪽에 있는 수 

N = int(input())
A = list(map(int, input().split()))

# stack을 내림차순으로 관리 
NGE, stack = [-1] * N, []
for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        NGE[stack.pop()] = A[i]
    stack.append(i)
print(*NGE)