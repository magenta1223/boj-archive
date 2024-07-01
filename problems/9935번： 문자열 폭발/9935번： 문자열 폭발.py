#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 9935                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/9935                          #+#        #+#      #+#     #
#     Solved: 2023-12-29 13:54:16 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

S=input().strip()
Bomb=input().strip()
stack = []
len_Bomb = len(Bomb)
for s in S:
    stack.append(s)
    while len(stack) >= len_Bomb and "".join(stack[-len_Bomb:]) == Bomb:
        for _ in range(len_Bomb):
            stack.pop()
print("".join(stack) if stack else "FRULA")