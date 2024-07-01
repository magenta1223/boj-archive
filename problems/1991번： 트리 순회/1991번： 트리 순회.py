#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1991                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1991                          #+#        #+#      #+#     #
#     Solved: 2024-03-30 00:14:08 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
G = dict()
t = lambda s:  s.replace(".", "") 
 
for _ in range(N):
    a,b,c = input().split()
    b, c = t(b), t(c)
    G[a] = [b,c]
 
def dfs(node):
    if not node:
        return "", "", ""
    left, right = G[node]
    L_pre, L_in, L_po = dfs(left)
    R_pre, R_in, R_po = dfs(right)
    return node + L_pre + R_pre, L_in + node + R_in, L_po + R_po + node 
 
print(*dfs("A"), sep ='\n')