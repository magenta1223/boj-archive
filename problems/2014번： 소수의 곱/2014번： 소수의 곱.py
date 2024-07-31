#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2014                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2014                          #+#        #+#      #+#     #
#     Solved: 2024-07-31 05:02:06 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# K개의 소수가 주어지고 
# 이들을 곱해서 만들 수 있는 수 중 N번째 수를 구하세용 
# A, B, C가 주어지면 -> 모든 A^a * B^b * C^c 중 N번째 수를 구하기 


# 1. 일단 PrimeNumbers로 시작
# 2. heap에 넣는다
# 3. 가장 작은 수를 pop
# 4. stack에 추가 
# 5. pop한 수를 Primenumbers랑 곱해서 heap에 추가 
# N번 반복 


from heapq import heappop, heappush 

INF = 2147483648
K, N = map(int, input().split())
PrimeNumbers = list(map(int, input().split()))
q = []

for p in PrimeNumbers:
    heappush(q, p)

cnt, prev = 0, 0
while cnt < N:
    num = heappop(q)
    if prev == num:
        continue
    for p in PrimeNumbers:
        nextNum = num*p
        if nextNum <= INF:
            heappush(q, nextNum)
        else:
            break 
    prev = num
    cnt += 1 

print(num)