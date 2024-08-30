#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 9426                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/9426                          #+#        #+#      #+#     #
#     Solved: 2024-08-28 06:32:41 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



# N개의 수로 구성된 배열 A
# K길이의 연속부분수열의 중앙값을 순서대로 출력  
# 누적합 ?



input = open(0).readline 

N,K = map(int,input().split())
A = [int(input())+1 for _ in range(N)] # 0~65535 -> 1~65536


class FenwickTree:
    def __init__(self, n) -> None:
        self.n = n 
        self.tree = [0] * (n+1)

    def update(self, x, delta):
        while x <= self.n:
            self.tree[x] += delta 
            x += x&-x

    def query(self, x):
        res = 0 
        while x > 0:
            res += self.tree[x]
            x -= x& -x
        return res 
    
    def search_median(self):
        # 누적합이 (K+1)//2가 되는 최소 지점을 찾기 
        target = (K+1)//2
        s,e = 1, self.n 
        while s<=e:
            mid = (s+e)//2 
            if self.query(mid) >= target:
                e = mid-1
            else:
                s = mid+1 
        return s-1

fwtree = FenwickTree(65536)
ans = 0 
for i in range(N):
    fwtree.update(A[i], 1)
    if i >= K-1:
        ans += fwtree.search_median()
        fwtree.update(A[i-K+1], -1)
print(ans)

