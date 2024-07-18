# 5525번： IOIOI - <img src="https://static.solved.ac/tier_small/10.svg" style="height:20px" />Silver I


| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 256 MB | 42489 | 11921 | 9690 | 29.749% |


## 문제


N+1개의 <code>I</code>와 N개의 <code>O</code>로 이루어져 있으면, <code>I</code>와 <code>O</code>이 교대로 나오는 문자열을 P<sub>N</sub>이라고 한다.
- P<sub>1</sub><code>IOI</code>
- P<sub>2</sub><code>IOIOI</code>
- P<sub>3</sub><code>IOIOIOI</code>
- P<sub>N</sub><code>IOIOI...OI</code>(<code>O</code>가 N개)

<code>I</code>와 <code>O</code>로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 P<sub>N</sub>이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.



## 입력


첫째 줄에 N이 주어진다. 둘째 줄에는 S의 길이 M이 주어지며, 셋째 줄에 S가 주어진다.




## 출력


S에 P<sub>N</sub>이 몇 군데 포함되어 있는지 출력한다.



## 제한


- 1 ≤ N ≤ 1,000,000

- 2N+1 ≤ M ≤ 1,000,000

- S는 <code>I</code>와 <code>O</code>로만 이루어져 있다.




## 서브태스크


| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 256 MB | 42489 | 11921 | 9690 | 29.749% |




## 예제 입력 1


<pre>1
13
OOIOIOIOIIOII
</pre>


## 예제 출력 1


<pre>4
</pre>


- OOOIOIIOII

- OOIOOIIOII

- OOIOIOIOII

- OOIOIOIOII







## 예제 입력 2


<pre>2
13
OOIOIOIOIIOII
</pre>


## 예제 출력 2


<pre>2
</pre>


- OOOIIOII

- OOIOIOII









## 출처




[Olympiad](/category/2)> [Japanese Olympiad in Informatics](/category/100)> [JOI 2012/2013](/category/detail/542)P4번
[Olympiad](/category/2)> [Japanese Olympiad in Informatics](/category/100)> [JOI 2008/2009](/category/detail/550)1번
[Olympiad](/category/2)> [Japanese Olympiad in Informatics](/category/100)> [JOI 2013/2014](/category/detail/1249)P4번
- 문제를 번역한 사람: [baekjoon](/user/baekjoon)
- 데이터를 추가한 사람: [eric00513](/user/eric00513), [ngchaneok](/user/ngchaneok)
- 문제의 오타를 찾은 사람: [hist0613](/user/hist0613)



## 채점 및 기타 정보


- 예제는 채점하지 않는다.





