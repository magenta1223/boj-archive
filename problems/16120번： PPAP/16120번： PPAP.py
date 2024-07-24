#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 16120                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/16120                         #+#        #+#      #+#     #
#     Solved: 2024-07-24 07:04:02 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 시간초과 
# S = input()
# N = len(S)
# while 'PPAP' in S:
#     S = S.replace('PPAP', 'P')
# print('PPAP' if S == "P" else 'NP')


S = input()
N = len(S)

if S == 'P':
    print('PPAP')
    exit(0)

PPAP = list('PPAP')
stack = []
for i in range(N):
    while len(stack) >= 4 and stack[-4:] == PPAP:
        stack.pop()
        stack.pop()
        stack.pop()
    stack.append(S[i])

print('PPAP' if stack == PPAP else 'NP')