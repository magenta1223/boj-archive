#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1541                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1541                          #+#        #+#      #+#     #
#     Solved: 2023-12-21 16:19:10 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

S=input()
prev_i = -1
ans = 0
add=True
for i in range(len(S)):
    if S[i] in ['+', '-']:    
        n = int(S[prev_i+1:i])
        if add:
            ans+=n
        else:
            ans-=n
        if S[i] == "-":
            add=False
        prev_i = i
        
n =int(S[prev_i+1:])
if add:
    ans+=n
else:
    ans-=n
 
print(ans)