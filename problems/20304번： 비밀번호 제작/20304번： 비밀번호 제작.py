#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 20304                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/20304                         #+#        #+#      #+#     #
#     Solved: 2024-11-14 00:08:31 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

"""
0이상 N "이하"의 정수 중 하나를 사용 

두 비밀번호의 안전거리 = bin(a xor b).count("1") 

안전도 = 지금까지 사용된 비밀번호와의 안전거리 중 "최솟값"
ex) 
3,4를 이미 사용했고, 새로운 비밀번호가 8
이때 3과의 안전거리는 3, 4와의 안전거리는 2
=> 8의 안전도는 2 

안전도가 가장 높게끔 비밀번호를 바꾸고 싶다. 
그 비밀번호의 안전도를 구하자 

일단! 전부 이진수로 나타내보자. 

3 4 -> 011 100

이진표현, 안전거리 3과 4를 각각 표시 
5: 101, 2, 1 -> 1 
6: 110, 2, 1 -> 1
7: 111, 1, 2 -> 1 
8: 1000,3, 2 -> 2
9: 1001,2, 2 -> 2 
10: 1010,2, 3 -> 2 

=> 최대 안전도는 2! 

즉, 안전도 = 기존 비밀번호와 유사 정도가 낮을수록 높음. 

-> 각 자릿수별로 cnt를 구하고 

최대 자릿수에서 cnt가 존재하는 영역까지 전부 1로 채우고,
그 다음부터는 아래 규칙에 따라 채운다. 
1. 전체가 같은 값이라면 -> 반대 값으로 채우고, 안전도+1 
2. 아니라면 -> 뭘 채워도 안전도는 그대로임. 


할 일
1. 주어진 비밀번호를 전부 이진수로 만들고
2. 각 자릿수의 cnt를 저장하는 dict하나 만들어서 저장
3. N을 이진수로 만들고, 현재 최대자릿수 다음부터 bin(N)까지 1로 채운다. 
3-1) bin(N)의 최대자릿수까지 꽉 차있을 경우 -> 걍 빈곳만 채우셈
4. 각 자릿수에 대해, P의 모든 암호의 해당 자리 숫자가 동일할 경우, 반대 숫자로 채우고 안전도+1 
5. 아니라면, 아무거나 채우고 안전도는 그대로. 

이건 최소 안전도임. 

그냥 bfs + bitmask? 
"""


from collections import deque

input=open(0).readline 

N = int(input())
M = int(input())
P = list(map(int,input().split()))
safety=[21 for _ in range(N+1)]
q=deque()
for pw in P: 
    safety[pw]=0
    q.append(pw)
    
while q:
    cur=q.popleft()
    for i in range(20):
        # 현재 비밀번호와 i번째 자릿수만 있는 비밀번호의 xor = 해당 자릿수만 바꾸기 
        # 그 safety는 한 자리만 바뀌었으므로, safety[cur]+1
        # 이것보다 크다면 -> 방문해서 변경. 
        x = (1<<i) ^ cur
        if x<=N  and safety[cur]+1<safety[x]:
            safety[x]=safety[cur]+1
            q.append(x)
print(max(safety))