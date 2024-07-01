#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10828                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10828                         #+#        #+#      #+#     #
#     Solved: 2024-04-04 14:34:11 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 
stack = []
for _ in range(int(input())):
    cmd = input().strip().split()
    if len(cmd) > 1:
        stack.append(cmd[1])
        continue 
    cmd = cmd[0]
    if cmd=="pop":
        print(stack.pop() if stack else -1) 
    elif cmd == "size":
        print(len(stack)) 
    elif cmd == "empty":
        print(0 if stack else 1) 
    else:
        print(stack[-1] if stack else -1)