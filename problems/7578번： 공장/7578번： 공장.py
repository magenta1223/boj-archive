#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 7578                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/7578                          #+#        #+#      #+#     #
#     Solved: 2024-07-09 04:45:50 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



# 교차하는 쌍의 개수 = mergeSort에서 발생하는 inv뭐시기 그거아닌가

# 세그먼트 트리  
# from math import log2, ceil 
# input = open(0).readline 
# N = int(input())
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))

# B_index = {value: index for index, value in enumerate(B)}


# A = [(B_index[A[i]] , i) for i in range(N)] # 아마도 이것 때문에.. 
# A.sort()
# TREE = [0] * (1<<( ceil(log2(N))+1))

# def update(idx, s, e):
#     if not s<= target <= e:
#         return TREE[idx]

#     if s == e:
#         TREE[idx] = 1 
#         return TREE[idx]
#     mid = (s+e)//2
#     TREE[idx] = update(idx*2, s, mid) + update(idx*2+1, mid+1, e)
#     return TREE[idx]

# def get(idx, s, e):
#     if e < frm or to < s:
#         return 0

#     if frm <= s and e <= to:
#         return TREE[idx]

#     if s == e:
#         return TREE[idx]
#     mid = (s+e)//2
#     return get(idx*2, s, mid) + get(idx*2+1, mid+1, e)

# ans = 0 
# for _, target in A:
#     frm, to = target+1, N-1 
#     ans += get(1, 0, N-1)
#     update(1, 0, N-1)
# print(ans)



# fenwick tree

input = open(0).readline 

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

B_index = {value: index for index, value in enumerate(B)}
A = [(B_index[A[i]] , i) for i in range(N)] # 아마도 이것 때문에.. 
A.sort()

class FenwickTree:
    def __init__(self, n) -> None:
        self.n = n 
        self.tree = [0] * (n+1)

    def update(self, x):
        i = x
        while i<=self.n:
            self.tree[i] += 1 
            i += i&-i 
    def query(self, frm, to):
        return self._query(to) - self._query(frm-1)
    
    def _query(self, x):
        _sum = 0 
        i = x
        while i > 0:
            _sum += self.tree[i]
            i -= i&-i 
        return _sum 

fwtree = FenwickTree(N)
ans = 0 
for _, target in A:
    frm, to = target+1, N
    ans += fwtree.query(frm,to)
    fwtree.update(frm)
print(ans)