#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10266                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10266                         #+#        #+#      #+#     #
#     Solved: 2024-04-15 19:17:07 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
A,B = [0] * 360_000, [0] * 360_000 
 
for a in list(map(int,input().split())):
    A[a] = 1 
 
for b in list(map(int,input().split())):
    B[b] = 1 
 
def failure(p):
    pi, j = [0] * 360_000, 0
    for i in range(1, 360_000):
        while j > 0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j 
    return pi 
 
def kmp(a,b):
    pi, j = failure(b), 0
 
    for i in range(len(a)):
        while j > 0 and a[i] != b[j]:
            j = pi[j-1]
        if a[i] == b[j]:
            if j == 359_999:
                print("possible")
                exit(0)
            else:
                j += 1 
    print("impossible")
kmp(A+A, B)