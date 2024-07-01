#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1725                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1725                          #+#        #+#      #+#     #
#     Solved: 2023-12-29 15:17:48 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input= open(0, "rb").readline
 
N=int(input())
heights=[int(input()) for _ in range(N)]
 
if len(heights) == 1:
    print(heights[0])
else:
    heights.append(0)  # 끝 처리를 위한 0 추가
    # i번째 loop에서 stack의 원소들 : heights[i]보다 낮은 구간의 index를 저장. = 그 이후부터는 현재 높이보다 반드시 높다. 
    stack = []
    area = 0
    for i in range(N + 1):
        # 쌓인 막대가 존재하고,
        # 그 높이가 현재 높이보다 높을 때 
        while stack and heights[stack[-1]] > heights[i]:
            # 기존높이
            h = heights[stack.pop()]
            # 너비. 
            # stack이 없음 = 현재 높이보다 낮은 구간이 없다 = 현재 높이가 최저임. 
            # stack이 존재 = 현재 높이보다 낮아지는 구간의 index = stack[-1]. 거기까지만 높이가 h인 직사각형을 만들 수 있음.
            width = i if not stack else i - stack[-1] - 1
            area = max(area, h * width)
        stack.append(i)
    print(area)