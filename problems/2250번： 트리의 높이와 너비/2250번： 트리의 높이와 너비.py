#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2250                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2250                          #+#        #+#      #+#     #
#     Solved: 2024-08-02 09:16:46 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# inorder 스타일로 트리를 그린다.
# 자식은 부모 아랫줄에
# 그러면 루트기준으로 레벨이 정해짐.
# 각 레벨의 너비를 측정하고, 가장 너비가 넓은 레벨과 그 너비를 출력 

# 1. dfs로 죽죽 내려가면서 중위표기식을 만든다. 
# 2. 동시에 그 길이 알 수 있나? 알 수 있다.
# 1) left먼저 계산, right 나중에 계산 
# 2) 위에서 받는 것은 현재 노드의 왼쪽에 있는 노드의 개수. 
# 3) left subtree 계산 시, 그 값을 더해서 column을 계산 
# 4) right subtree 계산 시, 그 값에 leftsubtree + 1 (현재 노드)를 더해서 넘겨줌. 
# 5) 현재 노드의 값과 레벨을 가지고 현재 레벨의 l,r 값을 갱신함. 
# 이진트리이므로, 레벨의 최댓값은 N
# 너비는 N 

input = open(0).readline 
N = int(input())
L = [[N,0] for _ in range(N+1)]

G = {i:[-1,-1] for i in range(1,N+1)}
root = set(list(range(1,N+1)) + [-1])
children = set()

for _ in range(N):
    node, left, right = map(int, input().split())
    G[node][0] = left
    G[node][1] = right 
    children.add(left)
    children.add(right)

root = list(root - children)[0]

def dfs(node, level, lowerBound):
    left, right = G[node]
    nLeft = dfs(left, level+1, lowerBound) if left != -1 else 0 
    nRight = dfs(right, level+1, lowerBound+nLeft+1) if right != -1 else 0 
    L[level] = [min(L[level][0], lowerBound+nLeft+1), max(L[level][1], lowerBound+nLeft+1)]
    return nLeft+nRight+1  # 현재 서브트리에 속한 노드 갯수를 리턴 

dfs(root, 1, 0)
widths = []
for i in range(1,N+1):
    if L[i] == [N,0]:
        break 
    widths.append((i, L[i][1] - L[i][0] +1))
widths.sort(key= lambda x: (x[1], -x[0]), reverse= True)
print(*widths[0])