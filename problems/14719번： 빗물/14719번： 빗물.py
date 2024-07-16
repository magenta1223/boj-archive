#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14719                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14719                         #+#        #+#      #+#     #
#     Solved: 2024-07-16 02:06:44 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 고이는 빗물의 총량 구하기 

# 왼쪽부터 순회
# 현재 높이가 stack의 마지막 높이보다 크다면 -> pop 
# stack의 마지막 값과 현재 높이의 차이만큼 물이 고임
# stack에 현재 높이 추가 


input = open(0).readline 
H,W = map(int,input().split())
Heights = list(map(int,input().split()))

stack = []
ans = 0 
for i in range(W):        
    start = stack[0] if stack else None 
    while stack and Heights[stack[-1]] < Heights[i]:
        stack.pop()
    if not stack and start is not None:
        h = Heights[start]
        ans += sum([ h - Heights[idx] for idx in range(start, i)])
    stack.append(i)



while stack and len(stack) > 1:
    now = stack.pop()
    h = Heights[now]
    ans += sum([h - Heights[i] for i in range(stack[-1]+1, now)])
    

print(ans)

"""
3 5
3 0 2 0 1 
ans: 3 
"""