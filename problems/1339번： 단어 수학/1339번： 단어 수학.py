#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1339                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1339                          #+#        #+#      #+#     #
#     Solved: 2024-07-23 06:42:29 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# W에는 알파벳대문자로 구성된 단어가 있고
# 각 알파벳 대문자를 0~9사이의 숫자로 바꾼후 그 합이 최대가 되도록 해보자 
# 최대 10개의 알파벳만 나옴

# 1. 알파벳별 자릿수 갯수를 전부 세고, 그 합을 저장 
# 2. 그 합이 큰 순으로 숫자를 위에서부터 할당 


N = int(input())
W = [input().strip() for _ in range(N)]
S = list(set(list(''.join(W))))
C = {s: 0 for s in S}
for w in W:
    for i, s in enumerate(w[::-1]):
        C[s] += 10**i 
D = dict()
for i in range(9,-1,-1):
    if not C:
        break 
    res = 0
    target=  sorted([(k,v) for k, v in C.items()], key=lambda x: x[1])[-1][0]
    D[target] = str(i) 
    del C[target]
print(sum([int( "".join([ D[s] for s in w])) for w in W]))
    
