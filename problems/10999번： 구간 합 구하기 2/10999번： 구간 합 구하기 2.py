#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10999                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10999                         #+#        #+#      #+#     #
#     Solved: 2024-07-09 02:28:33 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 1. 세그트리
# 2. 펜윅트리 <- 이게 편하..긴한데 기억이 안남 



input = open(0).readline 
N,M,K = map(int,input().split())
A = [int(input()) for _ in range(N)]

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree1 = [0] * (n+1) # Ax
        self.tree2 = [0] * (n+1) # Zx
    
    def _update(self, tree, i, delta):
        while i <= self.n:
            tree[i] += delta
            i += i & -i
    
    def update(self, frm, to, delta):
        """
        https://nahwasa.com/entry/%ED%8E%9C%EC%9C%85-%ED%8A%B8%EB%A6%ACFenwick-tree-BIT-%EA%B8%B0%EB%B3%B8-2D-lazy-propagationrange-update-point-query-range-update-range-query#%EC%9D%91%EC%9A%A9_2_:_%EA%B5%AC%EA%B0%84_%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8,_%EB%8B%A8%EC%9D%BC_%EA%B0%92_%ED%9A%8D%EB%93%9D
        
        원본 배열 A 
        누적합 P 

        1. P`을 [a,b]를 기준으로 나눠서 구한다
        2. A`을 [a,b]를 기준으로 나눠서 구한다
        3. 1을 2의 결과를 통해 표현. A`x 이외의 항을 Z`x로 표현
        => P`x를 A`x와 Z`x를 통해 표현 가능. = Px도 마찬가지 
        각각 point update, point query가 가능
        
        A에 대한 range update -> Ax와 Zx에 대한 point update로 변환
        A에 대한 range query -> Ax와 Zx에 대한 point query로 변환. 값을 구한다. 

        """

        
        # 일반적인 fenwick tree 
        self._update(self.tree1, frm, delta)
        self._update(self.tree1, to + 1, -delta)

        # Zx 
        self._update(self.tree2, frm, delta * (frm - 1))
        self._update(self.tree2, to + 1, -delta * to)
    
    def _query(self, tree, i):
        sum_ = 0
        while i > 0:
            sum_ += tree[i]
            i -= i & -i
        return sum_

    def query(self, x):
        return self._query(self.tree1, x) * x - self._query(self.tree2, x)

    def range_query(self, frm, to):
        return self.query(to) - self.query(frm - 1)


fwtree = FenwickTree(N)

for i in range(N):
    fwtree.update(i + 1, i + 1, A[i])


for _ in range(M + K):
    query = list(map(int, input().split()))
    if query[0] == 1:
        frm, to, value = query[1:]
        fwtree.update(frm, to, value)
    else:
        frm, to = query[1:]
        print(fwtree.range_query(frm, to))