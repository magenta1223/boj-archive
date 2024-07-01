#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1107                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1107                          #+#        #+#      #+#     #
#     Solved: 2024-03-04 22:35:39 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
M = int(input())
if M:
    broken_buttons = set(list(map(int, input().split())))
else:
    broken_buttons = set()
 
buttons = set([0,1,2,3,4,5,6,7,8,9]) - broken_buttons 
buttons = list(map(str, buttons))
 
# 1. +- 눌러서 가기
ans = abs(N-100)
# 2. 숫자를 눌러서 접근 
# 전부다 누를 수 있는지? 누를 수 있다면 누르고, +-로 target에 접근 
for i in range(1_000_000):
    stri = str(i)
    if all([s in buttons for s in stri]):
        ans = min(ans, len(stri) + abs(N-i))
print(ans)
 