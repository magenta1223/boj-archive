#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10775                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10775                         #+#        #+#      #+#     #
#     Solved: 2024-03-04 16:43:33 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
sys.setrecursionlimit(10**6)
input = open(0).readline
G = int(input())
P = int(input())
 
GATES = [i for i in range(G+1)]
PARKED = [False for _ in range(G)]
 
def find(gate):
    # 빈자리인가? 
    if GATES[gate] == gate:
        return gate 
    GATES[gate] = find(GATES[gate])
    return GATES[gate]
 
def parkable(gate):
    leading_gate = find(gate)
    if leading_gate == 0:
        return False 
    else:
        GATES[leading_gate] = leading_gate - 1
        return True 
 
        
ans = None
for i in range(P):
    gi = int(input())
    if ans is not None:
        continue
    if not parkable(gi):
        ans = i 
print(ans if ans is not None else i+1)