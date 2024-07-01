#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1717                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1717                          #+#        #+#      #+#     #
#     Solved: 2024-03-04 15:16:12 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
sys.setrecursionlimit(10**6)
 
input = open(0).readline 
N,M = map(int,input().split())
sets = [i for i in range(N+1)]
 
def find(a):
    if sets[a] == a:
        return a 
    sets[a] = find(sets[a])
    return sets[a]
 
def union(a, b):
    a, b = find(a), find(b)
    a,b = (a, b) if a<b else (b, a)
    sets[b] = a  
    
def inSameSet(a,b):
    a, b = find(a), find(b)
    print("yes" if a==b else "no")
 
FUNCS = {0 : union, 1: inSameSet}
 
for _ in range(M):
    func, a, b = map(int,input().split())
    FUNCS[func](a, b)
 
 
 