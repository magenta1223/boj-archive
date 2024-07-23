#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1422                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1422                          #+#        #+#      #+#     #
#     Solved: 2024-07-23 09:15:57 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



# A에서 N개를 뽑아서 이어붙이고
# 최소 1개씩은 사용 

def getValue(string):
    return int((string*12)[:11])

input  = open(0).readline 
K,N = map(int, input().split())
A = [ (n, getValue(n), len(n)) for n in [input().strip() for _ in range(K)]]
A.sort(reverse= True, key=lambda x: (x[2], x[1]))
A += [A[0]] * (N-K)
A.sort(reverse= True, key = lambda x:x[1])
print(int("".join([n for n,v,l in A])))



"""
3 4
1
10
100


2 2
998
9989



7 8
92
91
9
78
7
888
76

정답 : 99291 88888878776 (9/92/91/888/888/78/7/76)
9929188888878776
99291 88878776888
"""
