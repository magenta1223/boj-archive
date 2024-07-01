#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 5639                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/5639                          #+#        #+#      #+#     #
#     Solved: 2024-04-03 18:45:57 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
sys.setrecursionlimit(10**5)
 
preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break 
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root
 
def postorderTraversal(root, postorder):
    if root is not None:
        postorderTraversal(root.left, postorder)
        postorderTraversal(root.right, postorder)
        postorder.append(root.value)
 
root = None
for value in preorder:
    root = insert(root, value)
 
postorder = []
postorderTraversal(root, postorder)
print(*postorder, sep ='\n')
 