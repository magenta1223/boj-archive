#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14238                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14238                         #+#        #+#      #+#     #
#     Solved: 2024-05-14 11:15:30 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import Counter 
 
S = input().strip()
N = len(S)
C = Counter(S)
 
lasts= ['', 'A', 'AA', 'AAA', 'AAB', 'AAC', 'AB', 'ABA', 'ABC', 'AC', 'ACA', 'ACB', 'B', 'BA', 'BAA', 'BAB', 'BAC', 'BC', 'BCA', 'BCB', 'C', 'CA', 'CAA', 'CAB', 'CB', 'CBA']
 
dp = {l : [[[False] * (C['C']+1)  for _ in range(C['B']+1)] for _ in range(C['A']+1)] for l in lasts}
 
# 일단 시작 -> 
def dfs(s,d):
    if d == N:
        print(s)
        exit(0)
    
    if dp[s[-3:]][C['A']][C['B']][C['C']]:
        return 
    
    dp[s[-3:]][C['A']][C['B']][C['C']] = True 
 
    if C["A"] > 0:
        C['A'] -= 1 
        dfs(s+"A", d+1)
        C['A'] += 1
 
    if C["B"] and "B" not in s[-1:]:
            C['B'] -= 1 
            dfs(s+"B", d+1)
            C['B'] += 1
 
    if C["C"] and "C" not in s[-2:]:
            C['C'] -= 1 
            dfs(s+"C", d+1)
            C['C'] += 1
 
 
dfs("",0)
print(-1)