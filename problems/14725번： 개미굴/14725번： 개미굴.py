#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14725                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14725                         #+#        #+#      #+#     #
#     Solved: 2024-04-12 18:13:13 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def dfs(tree, left_nodes):
    if not left_nodes:
        return tree 
    next_node = left_nodes.pop()
    if next_node not in tree:
        tree[next_node] = dict()
 
    tree[next_node] = dfs(tree[next_node], left_nodes)
    return tree
 
def solve(tree, depth):
    if not tree:
        return 
    for k in sorted(tree.keys()):
        print("--" * depth + str(k))
        solve(tree[k], depth+1)
 
N = int(input())
Tree = dict()
for _ in range(N):
    l = input().split()[-1:0:-1]
    init_node = l.pop()
    if init_node not in Tree:
        Tree[init_node] = dict()
    Tree[init_node] = dfs(Tree[init_node], l)
solve(Tree, 0)