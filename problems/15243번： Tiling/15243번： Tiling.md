# 15243번： Tiling - <img src="https://static.solved.ac/tier_small/11.svg" style="height:20px" />Gold V


| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 512 MB | 190 | 128 | 122 | 68.927% |


## 문제


Domino tiles (or dominoes) are rectangular pieces of size 2x1. Each square contains a number from 1 to 6. These pieces are used to play a game but in this problem we are going to use them for something different.

We can build rectangles of certain width W and height 3 using dominoes. We are wondering how many ways of creating such rectangles are possible.

Below you can see the three possible ways of creating a rectangle of width 2 and height 3.


As you see there are many ways of tiling the rectangle. For example this is a possible solution with width 12:


Your task is to write a program that computes the number of possible ways of tiling a rectangle of width W and height 3.




## 입력


A single line with an integer W. The width of the rectangle.

The value of W will be between 1 and 1000.




## 출력


A single line with the number of possible ways. The numbers can be large so print the solution modulo 1000000007 (10+ 7).



## 제한




## 예제 입력 1


<pre>2
</pre>


## 예제 출력 1


<pre>3
</pre>




## 예제 입력 2


<pre>8
</pre>


## 예제 출력 2


<pre>153
</pre>




## 예제 입력 3


<pre>30
</pre>


## 예제 출력 3


<pre>299303201
</pre>




## 예제 입력 4


<pre>3
</pre>


## 예제 출력 4


<pre>0
</pre>




## 예제 입력 5


<pre>56
</pre>


## 예제 출력 5


<pre>485646032
</pre>




## 힌트


In the last test case, the actual result is 8155103542731753 by we have to print it modulo 10+ 7.




## 출처


[Olympiad](/category/2)> [All-Ireland Programming Olympiad](/category/356)> [2017 AIPO National Finals](/category/detail/1805)6번



