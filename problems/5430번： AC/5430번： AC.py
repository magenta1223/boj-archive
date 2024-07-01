#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 5430                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/5430                          #+#        #+#      #+#     #
#     Solved: 2024-03-05 00:00:10 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
T = int(input())
for _ in range(T):
    P = input().strip()
    n = int(input())
    if n:
        L = [s for s in input().strip()[1:-1].split(',')]
    else:
        input()
        L = []
    s, e, i = 0, n, 0
    
    reverse = False
    L, P = deque(L), deque([p for p in P]) 
    while L and P:
        p = P.popleft()
        if p == "R":
            reverse = not reverse 
            i += 1
        elif reverse:
            L.pop()
        else:
            L.popleft()
    
    # L이 남아 있으면 -> 출력
    if L:
        L = list(L) 
        if reverse:
            L.reverse()
        print(f"[{ ','.join(L)}]")
    # L이 없는데 P에 D가 있으면 에러 
    elif "D" in P:
        print("error")
    else:
        print("[]")