#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 12919                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/12919                         #+#        #+#      #+#     #
#     Solved: 2024-05-09 12:27:52 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

S, T = input(), input()
dp = set()
def dfs(t):
    if t == S:
        print(1)
        exit(0)
    if len(t) <= len(S):
        dp.add(t)
        return 
    if t in dp:
        return
    dp.add(t)
    if t[-1] == "A":
        dfs(t[:-1])
    if t[0] == "B":
        dfs(t[1:][::-1])
 
dfs(T)
print(0)