#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1477                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1477                          #+#        #+#      #+#     #
#     Solved: 2024-07-29 04:01:49 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 휴게소가 N개 있는데 M개를 더 세운다 
# 휴게소는 고속도로 입구부터의 거리로 주어진다 

# 이미 있는 곳, 끝에 휴게소 세울 수 없고 정수 위치에만 가능
# 휴게소가 없는 구간의 길이를 최소화 하자 

# ex) 길이 1000, 휴게소 200, 701, 800 
# 구간은 0~200, 200~701, 701~800, 800~1000 
# 가장 긴 구간은 701 
# 새로운 휴게소를 200~701의 가운데인 451에 세우면 휴게소 사이의 구간이 251이 최대가 됨 


# N은 0일수도 있음. 

N,M,L = map(int, input().split())
A = list(map(int,input().split())) 
A = [0] + sorted(A) + [L]

Intervals = []
for i in range(N+1):
    Intervals.append((A[i+1] - A[i]))

def solve(maxDist):    
    cnt = M 
    for interval in Intervals:
        v = (interval-1)//maxDist
        if cnt >= v:
            cnt -= v 
        else:
            return False 
    return True  

s,e = 1,L 
ans = float("inf")
while s<=e:
    mid = (s+e)//2 
    if solve(mid):
        e = mid - 1
    else:
        s = mid + 1  
print(s)