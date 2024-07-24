#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2812                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2812                          #+#        #+#      #+#     #
#     Solved: 2024-07-23 12:43:21 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



def largest_number_after_removals(K, S):
    stack = []
    to_remove = K
    for digit in S:
        while to_remove and stack and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)
    
    while to_remove:
        stack.pop()
        to_remove -= 1
    
    result = ''.join(stack)
    return result

N, K = map(int, input().split())
S = input().strip()
print(largest_number_after_removals(N, K, S))
