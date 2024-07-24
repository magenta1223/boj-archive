#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 3015                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/3015                          #+#        #+#      #+#     #
#     Solved: 2024-07-24 07:13:22 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 서로 볼 수 있는 쌍의 수를 구하기 

# 자기가 볼 수 있는 사람의 수 
# A와 B가 볼 수 있다 = A와 B사이에 A or B보다 큰 사람이 없다.
# 
# 자기 왼쪽만 카운트하고
# stack을 내림차순으로 관리 

# from bisect import bisect_left 

# input = open(0).readline 

# N = int(input())
# A = [int(input()) for _ in range(N)]

# ans = 0 
# stack = []
# for i in range(N):
#     # 본인 왼쪽에 선 사람 중 볼 수 있는 사람 수 
#     idx = bisect_left(stack, -A[i])
#     if idx:
#         ans += 1 
#     ans += len(stack) - idx 
#     while stack and -stack[-1] < A[i]:
#         stack.pop()
#     stack.append(-A[i])
# print(ans)



# input=open(0).readline
# N = int(input())
# H = [int(input()) for _ in range(N)]


# stack = []
# ans = 0

# for h in H:
#     count = 1
#     # stack의 단조감소. 
#     while stack and stack[-1][0] <= h:
#         # 현재 높이보다 작은 경우 -> 볼 수 있음. 
#         # 해당 키의 사람 수를 전부 볼 수 있으므로 추가 
#         _h, _c = stack.pop()
#         ans +=_c
#         # 만약 같다면?
#         if _h == h:
#             # 현재 키인 사람 수를 갱신
#             count += _c

#     # 현재 사람보다 큰 사람만 남음. 여기에 현재 키 + 카운트 추가
#     if stack:
#         ans += 1
#     stack.append((h, count))
# print(ans)





"""
4
4
3
2
1




"""