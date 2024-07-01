#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1786                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1786                          #+#        #+#      #+#     #
#     Solved: 2024-04-14 14:19:50 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def getPi(p):
    pi = [0] * M
    j = 0  
    # pi[i]
    # substr = p[:i]
    # substr[:j] == substr[-j:]인 j의 최댓값 
 
    for i in range(1,M):            
        while j>0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            j += 1 
            pi[i] = j
    return pi 
 
def kmp(s, p):
    ans = []
    pi = getPi(p)
    j = 0 
    for i in range(N):
        while j>0 and s[i] != p[j]:
            j = pi[j-1]
        if s[i] == p[j]:
            if j == M-1:
                ans.append(i-M+2)
                j = pi[j]
            else:
                j += 1 
    return ans 
    
 
T = input()
P = input()
N = len(T)
M = len(P)
 
matched = kmp(T,P)
print(len(matched))
print(*matched, sep = '\n')