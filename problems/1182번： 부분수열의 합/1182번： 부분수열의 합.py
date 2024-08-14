#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1182                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1182                          #+#        #+#      #+#     #
#     Solved: 2024-08-14 01:05:20 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


from collections import defaultdict

N,S = map(int,input().split())
A = list(map(int, input().split()))

# 원소의 합이 S가 되는 경우의 수를 구하기 
# 개수가 적으니 전부 찾기. 최대 2^20
# 1. i번째에서 끝나는 부분수열에서 발생하는 모든 값을 저장. 

counter = defaultdict(int)
counter[A[0]] = 1 

for i in range(1,N):
    tmp = defaultdict(int)
    tmp[A[i]] = 1 
    for k, v in counter.items():
        tmp[k+A[i]] += v 
    for k, v in tmp.items():
        counter[k] += v  

print(counter[S])