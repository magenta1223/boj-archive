#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1071                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1071                          #+#        #+#      #+#     #
#     Solved: 2024-06-14 11:04:11 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import Counter 
 
N = int(input())
A = list(map(int,input().split()))
A = Counter(A)
 
def dfs(di:dict, res:list, d):
    if d == N:
        print(*res[1:])
        exit(0)
    # array로 다넘기니까 중복이 너무 심함. dict로 넘기자 
    for k in sorted(di.keys()):
        if not di[k] or k == res[-1]+1:
            continue 
        di[k] -= 1
        dfs(di, res+[k], d+1)
        di[k] += 1 
 
dfs(A, [-2], 0)