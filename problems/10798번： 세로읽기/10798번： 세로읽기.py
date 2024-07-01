#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10798                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10798                         #+#        #+#      #+#     #
#     Solved: 2023-10-17 16:06:23 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

max_len = 0
d = []
for _ in range(5):
    x = input()
    if len(x) > max_len:
        max_len = len(x)
    d.append(x)
    
d = [ line + " " * (max_len - len(line)) if len(line) < max_len else line  for line in d]    
ss = "".join(["".join(d)[i::max_len] for i in range(max_len)]).replace(" ", "")
print(ss)