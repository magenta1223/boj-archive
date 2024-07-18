#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2668                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2668                          #+#        #+#      #+#     #
#     Solved: 2024-07-18 06:12:00 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


input = open(0).readline 


# N미만의 index의 집합 S에 대해
# set([A[i] for i in S]) == S 
# 인 S의 최대를 골라보자 

# N <= 100 
# 사이클이 생겨야 함. 
# 모든 사이클을 찾고, 사이클에 포함되는 노드의 개수 총합 


N = int(input())
A = [int(input()) -1 for _ in range(N)]

ans = []

for i in range(N):    
    num = i 
    visited = [False] * N 
    while not visited[num]:
        visited[num] = True 
        num = A[num]
    if num == i:
        ans.append(i+1) 

print(len(ans))
print(*ans, sep = '\n')