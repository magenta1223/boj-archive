#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 6549                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/6549                          #+#        #+#      #+#     #
#     Solved: 2024-04-24 16:36:22 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def solve(lst):
    lst.append(0)
    N, lst = lst[0], lst[1:]
    ans, stack = 0, []
    for i in range(N+1):
        # stack에는 index가 들어가고, 그 index의 bar 높이는 단조증가로 관리
        while stack and lst[stack[-1]] > lst[i]:
            height = lst[stack.pop()]
            width =  i-stack[-1]-1 if stack else i # 
            ans = max(ans, height*width)
        stack.append(i)
    print(ans)
 
while True:
    l = input().strip()
    if l == "0":
        break
    l = list(map(int, l.split()))
    solve(l)