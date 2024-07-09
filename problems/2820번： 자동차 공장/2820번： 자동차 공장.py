#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2820                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2820                          #+#        #+#      #+#     #
#     Solved: 2024-07-09 06:15:38 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 트리구조 -> 선형으로 조작
# 상위 노드의 start, end가 하위 노드의 start, end를 전부 포함하도록 
# 그 다음엔 일반적인 펜윅트리 


input = open(0).readline 

def getStartEnd():
    start = [0] * (N + 1)
    end = [0] * (N + 1)
    node_idx = 0
    stack = [(1, 0)]  
    while stack:
        node, child_idx = stack.pop()
        if child_idx == 0: 
            node_idx += 1
            start[node] = node_idx
        if child_idx < len(C[node]):  
            stack.append((node, child_idx + 1))
            stack.append((C[node][child_idx], 0))  
        else:  
            end[node] = node_idx

    return start, end 


class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, idx, delta):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx
    
    def query(self, idx):
        sum_ = 0
        while idx > 0:
            sum_ += self.tree[idx]
            idx -= idx & -idx
        return sum_
    
    def range_update(self, l, r, delta):
        self.update(l, delta)
        self.update(r + 1, -delta)
    
    def point_query(self, idx):
        return self.query(idx)


N, M = map(int, input().split())

S = [0] * (N + 1) # salary
B = [0] * (N + 1) # boss 
C = [[] for _ in range(N + 1)] # child 

S[1] = int(input())
for i in range(2, N + 1):
    S[i], B[i] = map(int, input().split())
    C[B[i]].append(i)

start, end = getStartEnd()
fenwick_tree = FenwickTree(N)

for i in range(1, N + 1):
    fenwick_tree.range_update(start[i], start[i], S[i])

for _ in range(M):
    query = input().split()
    if query[0] == 'p':
        a = int(query[1])
        x = int(query[2])
        fenwick_tree.range_update(start[a]+1, end[a], x)
    elif query[0] == 'u':
        a = int(query[1])
        print(fenwick_tree.point_query(start[a]))

