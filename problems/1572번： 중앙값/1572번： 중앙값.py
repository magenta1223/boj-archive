#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1572                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1572                          #+#        #+#      #+#     #
#     Solved: 2024-09-20 06:56:04 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



input = open(0).readline 
N,K = map(int, input().split())
A = [int(input()) for _ in range(N)]

class FenwickTree:
    def __init__(self, n, k):
        self.n = n 
        self.med = (k+1)//2  
        self.tree = [0] * (n+1)
    def update(self, x, delta):
        while x <= self.n:
            self.tree[x] += delta 
            x += x&-x 
    def query(self, x):
        res = 0 
        while x > 0:
            res += self.tree[x]
            x -= x&-x 
        return res 
    
    def find_median(self):
        # 1. 합이 (K+1)//2가 되는 가장 작은 지점을 찾기 
        s,e = 1,self.n 
        while s<=e:
            mid = (s+e)//2 
            if self.query(mid) >= self.med:
                e = mid-1 
            else:
                s = mid+1 
        return e
    
# 0~65536 -> 1~65537 
fwtree = FenwickTree(65537, K)

# K-1개를 넣고 시작
for i in range(K-1): 
    fwtree.update(A[i]+1, 1)

ans = 0 
for i in range(K-1,N):
    fwtree.update(A[i]+1, 1)
    ans += fwtree.find_median()
    fwtree.update(A[i-K+1]+1, -1)
print(ans)