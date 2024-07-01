#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 25501                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/25501                         #+#        #+#      #+#     #
#     Solved: 2023-11-24 15:36:40 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def recursion(s, l, r):
    global c
    c+=1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)
def isPalindrome(s):
    return recursion(s, 0, len(s)-1)
T=int(input())
for _ in range(T):
    c=0
    print(isPalindrome(input().rstrip()), c)