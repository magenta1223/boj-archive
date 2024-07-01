#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2263                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2263                          #+#        #+#      #+#     #
#     Solved: 2024-03-25 16:42:52 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
sys.setrecursionlimit(10**5)
 
def dfs(si, ei, sp, ep):
    global postOrder
    if si > ei or sp > ep:
        return 
    
    root = postOrder[ep] #po_order.pop()
    print(root, end = ' ')
    root_index = pos[root]
    
    left = root_index - si 
    # root_index ep        
    dfs(si,root_index-1,sp,sp+left-1)
    dfs(root_index+1,ei,sp+left,ep-1)
    
N = int(input())
inOrder = list(map(int,input().split()))
postOrder = list(map(int,input().split()))
 
pos = [0] * (N+1)
for i in range(N):
    pos[inOrder[i]] = i
root = postOrder[-1]
dfs(0,N-1,0,N-1)