#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2835                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2835                          #+#        #+#      #+#     #
#     Solved: 2024-07-10 02:49:05 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



# 1. 하루를 초 단위로 나눈다
# 2. 시청시간을 가지고 range update를 수행
# 3. 역시 range query를 수행 


class FenwickTree:
    def __init__(self) -> None:
        n = 60*60*24  
        self.n = n 
        self.tree1 = [0] * (n+1)
        self.tree2 = [0] * (n+1)

    def _update(self, tree, x, delta):
        while x <= self.n:
            tree[x] += delta 
            x += x&-x

    def _rangeUpdate(self, a, b):
        self._update(self.tree1, a, 1)
        self._update(self.tree1, b+1, -1)
        self._update(self.tree2, a, a-1)
        self._update(self.tree2, b+1, -b)
    
    def rangeUpdate(self, a, b):
        if a<=b:
            self._rangeUpdate(a, b)
        else:
            self._rangeUpdate(a, self.n)
            self._rangeUpdate(1, b)

    def _query(self, tree, x):
        _sum = 0
        while x > 0:
            _sum += tree[x]
            x -= x&-x
        return _sum 
    
    def query(self, x):
        return self._query(self.tree1, x) * x - self._query(self.tree2, x)
    
    def _rangeQuery(self, a,b):
        return self.query(b) - self.query(a-1)
        
    def rangeQuery(self, a, b):
        # a<b면 그냥하고
        # b<a면 구간 나눠서 
        if a<=b:
            return self._rangeQuery(a,b) / (b-a+1)
        else:
            return (self._rangeQuery(a,self.n) + self._rangeQuery(1,b)) / (b+self.n-a+1)

def transform(hms:str):
    h,m,s = [int(n) for n in hms.split(":")]
    return h*3600 + m*60 + s + 1  

input = open(0).readline 
N = int(input())
fwtree = FenwickTree()
for _ in range(N):
    a, b=  input().split(" - ")
    a, b = transform(a), transform(b)
    fwtree.rangeUpdate(a,b)

for _ in range(int(input())):
    a,b = input().split(" - ")
    a, b = transform(a), transform(b)
    print(fwtree.rangeQuery(a,b))

