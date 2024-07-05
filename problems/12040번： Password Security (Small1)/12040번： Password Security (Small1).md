# 12040번： Password Security (Small1) - <img src="https://static.solved.ac/tier_small/8.svg" style="height:20px" />Silver III


| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 5 초 | 512 MB | 64 | 42 | 31 | 77.500% |


## 문제


You just bought your young nephew Andrey a complete set of 26 English wooden alphabet letters from A to Z. Because the letters come in a long, linear package, they appear to spell out a 26-letter message.

You use different passwords to log into your various online accounts, and you are concerned that this message might coincidentally include one or more of them. Can you find any arrangement of the 26 letters, such that no password appears in the message as a continuous substring?



## 입력


The first line of the input gives the number of test cases, . test cases follow. Each consists of one line with an integer , and then another line with different strings of uppercase English letters P<sub>1</sub>
, P<sub>2</sub>
, ..., P<sub>N</sub>
, which are the passwords.
### Limits

- 1 ≤ ≤ 100.
- 1 ≤ length of P<sub>i</sub>
≤ 26, for all i. (Each password is between 1 and 26 letters long.)
- P<sub>i</sub>
≠ P<sub>j</sub>
for all i ≠ j. (All passwords are different.
- = 1.




## 출력


For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code>is the test case number (starting from 1) and <code>y</code>is a permutation of the entire uppercase English alphabet that contains no password as a continuous substring, or the word <code>IMPOSSIBLE</code>if there is no such permutation.



## 제한




## 예제 입력 1


<pre>7
1
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1
X
1
QQ
5
XYZ GCJ OMG LMAO JK
3
AB YZ NM
6
C PYTHON GO PERL RUBY JS
2
SUBDERMATOGLYPHIC UNCOPYRIGHTABLES
</pre>


## 예제 출력 1


<pre>Case #1: QWERTYUIOPASDFGHJKLZXCVBNM
Case #2: IMPOSSIBLE
Case #3: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Case #4: ABCDEFGHIKLMNOPQRSTUVWXYJZ
Case #5: ZYXWVUTSRQPOMNLKJIHGFEDCBA
Case #6: IMPOSSIBLE
Case #7: THEQUICKBROWNFXJMPSVLAZYDG
</pre>




## 힌트


For each of the non-<code>IMPOSSIBLE</code>cases, the sample output shows only one possible answer. There are many valid answers for these inputs.
Note that only sample cases #1, #2, and #3 would appear in Small dataset 1. Any of the sample cases could appear in Small dataset 2.





## 출처


[Contest](/category/45)> [Google](/category/621)> [Code Jam to I/O for Women](/category/622)> [Code Jam to I/O for Women 2016](/category/371)> [Code Jam to I/O for Women 2016](/category/detail/1615)D1번


## 채점 및 기타 정보


- 예제는 채점하지 않는다.





