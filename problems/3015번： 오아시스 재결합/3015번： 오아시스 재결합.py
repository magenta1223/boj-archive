#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 3015                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/3015                          #+#        #+#      #+#     #
#     Solved: 2024-05-17 17:52:16 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input=open(0, "rb").readline
N = int(input())
heights = [int(input()) for _ in range(N)]
stack = []
result = 0
for height in heights:
    count = 1
    # stack의 단조감소. 
    while stack and stack[-1][0] <= height:
        # 현재 높이보다 작은 경우 -> 볼 수 있음. 
        # 해당 키의 사람 수를 전부 볼 수 있으므로 추가 
        result += stack[-1][1]
        # 만약 같다면?
        if stack[-1][0] == height:
            # 현재 키인 사람 수를 갱신
            count += stack[-1][1]
        # stack에서 제거
        stack.pop()
    # 현재 사람보다 큰 사람만 남음. 여기에 현재 키 + 카운트 추가
    if stack:
        result += 1
    stack.append((height, count))
print(result)