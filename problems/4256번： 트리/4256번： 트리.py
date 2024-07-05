#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 4256                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/4256                          #+#        #+#      #+#     #
#     Solved: 2024-07-02 19:05:29 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline
 
def getPostOrder(preOrder, inOrder):
    if len(preOrder) <= 1:
        return preOrder
    idx = inOrder.index(preOrder[0])
    preLeft, preRight = preOrder[1:idx+1], preOrder[idx+1:]
    inLeft, inRight = inOrder[:idx], inOrder[idx+1:]
    return getPostOrder(preLeft, inLeft) + getPostOrder(preRight, inRight) + [preOrder[0]]
 
for _ in range(int(input())):
    N = int(input())
    PRE = list(map(int,input().split()))
    IN = list(map(int,input().split()))
    print(*getPostOrder(PRE, IN))