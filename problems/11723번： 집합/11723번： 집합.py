#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11723                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11723                         #+#        #+#      #+#     #
#     Solved: 2024-03-05 00:29:52 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline
M=int(input())
S = set()
for _ in range(M):
    command = input().strip().split()
    if len(command) > 1:
        c, num = command
        if c == "add":
            S.add(num)
        elif c =="check":
            print(1 if num in S else 0)
            # ans.append(1 if num in S else 0)
        elif c == "remove":
            S.discard(num)
        elif c == "toggle":
            if num in S:
                S.discard(num)
            else:
                S.add(num)            
    else:
        command = command[0]
        if command == "all":
            S = set([str(i) for i in range(1,21)])
        else:
            S = set()