#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 4354                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/4354                          #+#        #+#      #+#     #
#     Solved: 2024-04-15 15:10:47 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def kmp(string):
    M,j = len(string), 0
    pi = [0] * M
    M = len(string)
    for i in range(1,M):
        while j > 0 and string[i] != string[j]:
            j = pi[j-1]
        if string[i] == string[j]:
            j += 1 
            pi[i] = j 
    
    s,r = divmod(M, M-pi[-1])
    print(1 if r else s)
 
while True:
    S = input()
    if S == ".":
        break
    kmp(S)
 