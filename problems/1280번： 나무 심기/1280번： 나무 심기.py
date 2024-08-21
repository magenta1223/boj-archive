#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1280                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1280                          #+#        #+#      #+#     #
#     Solved: 2024-08-15 03:27:57 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



# 트리네 
# 1. 거리 배열, 개수 배열을 만들고 나무를 추가
# 2. 추가할 나무 왼쪽의 합, 오른쪽의 합을 전부 구함
# 3. 리턴 

# 1. 좌표의 최댓값은 20만으로 정해짐. 
# 2. 원하는 것: 어떤 위치에 나무를 추가했을 때, 좌우로 존재하는 나무의 위치 및 개수 
# 누적합으로 구할 수 있을듯? 
# a,b,c,x 일때 
# x의 비용 = (x-a) + (x-b) + (x-c) = 3*x - (a+b+c)
# 즉, 어떤 위치에서의 누적합은 이전에 발생한 나무 위치의 모든 합 
# 이번엔 오른쪽을 해보자 
# x,a,b,c 
# x의 비용 = (a-x) + (b-x) + (c-x) = a+b+c - 3*x



input = open(0).readline 
MOD =  1_000_000_007
N = int(input())

class FenwickTree:
    def __init__(self):
        n = 200_000
        self.n = n
        self.tree = [0] * (n+1)
        self.cnts = [0] * (n+1)
        
    def update(self, x):
        delta = x 
        while x<=self.n:
            self.tree[x] += delta 
            self.cnts[x] += 1 
            x += x&-x 
    
    def query(self, x):
        res, cnt = 0,0 
        while x > 0:
            res += self.tree[x]
            cnt += self.cnts[x]
            x -= x&-x 
        return res, cnt  
    
    def range_query(self, a,b):
        res_b, cnt_b = self.query(b)
        res_a, cnt_a = self.query(a-1)
        return res_b-res_a, cnt_b-cnt_a
    
    def update_cost(self, x):
        lcost, lcnt = self.range_query(1,x-1)
        rcost, rcnt = self.range_query(x+1,self.n)
        self.update(x)
        return (x*lcnt - lcost) + (rcost - x*rcnt)
        
fwtree = FenwickTree()
ans = 1 
fwtree.update(int(input())+1)
for _ in range(1,N):
    ans *= fwtree.update_cost(int(input())+1)
    ans %= MOD

print(ans)
