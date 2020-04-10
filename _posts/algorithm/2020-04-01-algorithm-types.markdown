---
layout: post
title:  "유형별 알고리즘 문제풀이"
date:   2020-04-01 00:00:00 +0900
categories: python pip algorithm
---

## 유형별 알고리즘 문제풀이
[백준 Online Judge](https://www.acmicpc.net/)  
[백준 - 단계별 태그](https://www.acmicpc.net/step)  
[백준 - 분류별 태그](https://www.acmicpc.net/problem/tags)

[TheLordOfBOJ - 백준 문제풀이 코드 모음](https://github.com/live2skull/TheLordOfBOJ)

----

## 문제풀이를 시작하기 전에...
\#1. 한 문제를 1시간 이상 풀이하지 않는다. 문제 풀이 시간을 초과한다면 우선 재쳐두고 다른 문제의 유형을 접해 본다.   
\#2. 사소한 실수 (마무리 단계 - 출력, 등수 조정, 정렬 등)으로 인해 전체 풀이를 잘못한 것으로 오인할 수 있다. 이러한 실수를 하지 않도록 주의한다.  
\#3. 돌파구가 보이지 않는 문제가 밥을 먹거나 샤워하는 도중 아이디어가 생각나는 경우도 있다. 본인이 풀지 못하는 문제를 너무 어렵게 생각하지 않는다.

## 유형별 정리

### 시작 단계

#### [출력](https://www.acmicpc.net/problem/tag/%EC%B6%9C%EB%A0%A5)

콘솔 입/출력(stdin/stdout)에 대해 다룬다.

단순히 특정 글 또는 로고 출력만이 필요할 경우 (문제에 입력이 없고, 정답이 항상 동일한 경우) 코드 제출 단계에서 언어를 `Text`로 지정하면 소스 코드가 아닌 답 자체를 제출할 수 있다.

다량의 데이터 입/출력 과정에서 발생할 수 있는 시간 초과에는 다음과 같이 대응한다.

**🧭 파이썬 예제**  
[python3 - input()과 sys.stdin.readline 성능 비교](https://stackoverflow.com/questions/22623528/sys-stdin-readline-and-input-which-one-is-faster-when-reading-lines-of-inpu)
```
sys.stdin.readline().strip() # readline()은 줄 개행 문제를 포함합니다.
```

**🧭 자바 예제**
```
import java.io.*;
// throws java.io.IOException

// Read
BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
String s = bf.readLine();
bf.close();

StringTokenizer st = new StringTokenizer(s); // 공백 단위의 데이터 가공
int a = Integer.parseInt(st.nextToken()); // BufferedReader - nextInt() 지원하지 않음

// Write
BufferedWriter bw = new BufferedWriter(new InputStreamWriter(System.out));
bw.write("MyString" + "\n");
bw.flush(); bw.write();
```


----

### 기본 단계

#### [수학](https://www.acmicpc.net/problem/tag/%EC%B6%9C%EB%A0%A5)

상황이 주어지되, `시뮬레이션` 유형과 달리 방정식, 수열의 성질을 이용해 수식을 작성하여 풀 수 있다.  
`시뮬레이션` 유형으로 풀이하였으나 시간 초과 / 메모리 초과로 풀이가 제한될 경우 수식을 이용한 풀이를 시도해 본다.

|-|설명|
|---|-----|
|방정식|N일때의 값 K, K가 되는 N 구하기.|
|수열|등차수열, 등비수열, 계차수열 - N에서 값,합|
|순열과 조합|조합 가능한 경우의 수. 순열 / 조합으로 별도 분류|

----

#### [시뮬레이션](https://www.acmicpc.net/problem/tag/%EC%8B%9C%EB%AE%AC%EB%A0%88%EC%9D%B4%EC%85%98)

상황이 주어지면 순차적으로 실행하면서 특정 상황이 되는 경우를 찾는다.  
`수학` 유형과 달리 n번쨰 상황에서의 결과값을 수식으로 정의하지 못하는 경우 카운터 변수를 두고 상황을 단계별로 시뮬레이션한다.

----

#### [브루트 포스](https://www.acmicpc.net/problem/tag/%EB%B8%8C%EB%A3%A8%ED%8A%B8%20%ED%8F%AC%EC%8A%A4)

상황이 주어지면 순차적으로 실행하면서 특정 상황이 되는 경우를 찾는다. 시뮬레이션과 비슷하지만, 순차적으로 특정 순차까지 실행하는 시뮬레이션과 다르게 브루트포스는 주어진 경우의 수 또는 객체들과 전체 비교, 판단하는 느낌의 유형이다.

**- 순열과 조합**  
주로 선택할 수 있는 경우의 수 (선택 가능한 갯수) N개가 주어지고, `순열(선택은 같으나 순서가 다르면 다른 선택)` 또는 `조합(선택이 같으면 순서가 달라도 같은 선택)` 으로 생성 가능한 전체 순열/조합을 전부 문제에서 요구하는 조건과 성립하는지 확인한다.  

**🧭 파이썬 예제**
```
# 조합 - 전체를 비교
data = [1, 2, 3, 4, 5, 6, 7]
for i in range(0, len(data)):
  for j in range(i + 1, len(data)):
    print(i, j, end=' | ')

# 1,2 | 1,3 | 1,4 ...
```


**- 우위 판별**  
각 객체들의 순위(우위)를 판별하는데, 정렬 문제와 같이 모든 객체들이 서로 비교 가능한 것이 아닌, 일부 객체들끼리만 우위 판별이 가능한 경우.

**- 기타**  
주어진 N의 범위에서 전체 데이터(N 또는 N으로 정해지는 값)에서 요구하는 조건을 성립/근접하는 결과를 판별한다. (예제 참고)


예제)
- 순열과 조합 : [블랙잭](https://www.acmicpc.net/problem/2798)
- 우위 판별 : [덩치](https://www.acmicpc.net/problem/7568)
- 기타 : [분해합](https://www.acmicpc.net/problem/2231)
----

#### [정렬](https://www.acmicpc.net/problem/tag/%EC%A0%95%EB%A0%AC)



\- 정렬 알고리즘을 구현하거나, 상황에 맞게 변형하여 사용한다.

\- 정수, 문자열의 정렬(아스키 코드 기준)을 다룬다.  
특정 데이터셋이 주어지고, 정렬 순위에 우선순위를 부여하여 여러개의 정렬 조건을 제시할 수 있다.

**🧭 파이썬 예제**
```
# 이름, 나이, 점수의 데이터셋
dset = [
  ('live2skull', 24, 100),
  ('Gap', 20, 82),
  ('eul', 20, 92)
]

# 나이 순 오름차순 정렬.
dset.sort(key=lambda x: x[1])

# 이름 오름차순, 점수 오름차순, 나이 내림차순 정렬. 정수의 부호를 변경하여 대소관계가 변경된다.
dset.sort(key=lambda x: (x[0], x[2], -x[1]))
```

**🧭 자바 예제**
```
작성중입니다. 😅
```

----

#### 트리

알고리즘보다 자료구조에 가까우며, 특정 상황에 주로 사용되는 트리 종류에 대해 설명한다.

|-|설명|
|---|-----|
|이진 트리|...|
|||
|||


----

#### DFS와 BFS
트리, 이차원 배열로 구성한 지도 데이터 등을 탐색한다.  

**\- DFS**  



**\- BFS**  

----

#### [동적 프로그래밍](https://www.acmicpc.net/problem/tag/%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)

|레벨|설명|
|---|-----|
|1|D[N] = D[N+X] + ...|
|2|1번과 동일하나, 재귀함수로 구현하였을 경우 Bottom-up으로 재구현하여야함|
|3|상황에 따라 값을 최대, 최소 등 선택. 경우에 따라 선택값 하나만 저장하는 상황을 여러값 저장으로 혼동의 여지가 있음|
|4|D[N]의 값이 연관되어있으며, 이전 선택지에 따라 현재 선택지가 제한을 받음|
|5|다양한 제약조건 추가|

|유형|설명|예제|
|---|-----|-----|
|수열|N번째의 값이 D[N] = D[N+x].. 같이 조합 갯수|[정수 삼각형](https://www.acmicpc.net/problem/1932)|

**\- 메모이제이션(Top-down)**  
특정 문제를 가장 큰 단위의 문제부터 시작하여 가장 작은 단계로 내려간 후 풀이한다. 큰 단위의 계산이 작은 단위의 데이터를 필요로 하며, 이를 위해 한번 계산한 결과를 저장하고, 동일한 연산을 수행할 때 불러와 사용하는 기법을 `메모이제이션` 이라고 한다.

주로 재귀 함수 형태로 구현하며, N값이 함수의 재귀가 반복되며 감소되고, 작업이 여러 갈래로 분할된다.  
재귀 함수의 특성항 상향식 계산법보다 대개 성능이 떨어지지만, 문제 유형에 따라 메모이제이션으로 구현해야 하는 경우도 있다. (...)


**\- 상향식 계산법(Bottom-up)**  
특정 ㅇ N의 결과를 도출하기 위해 가장 작은 단위부터 상황 N까지 올라가며, 작은 단위의 계산값을 저장, 큰 단위로 올라가며 작은 단위의 데이터를 필요로 한다.


**\- dp[] 에 저장하는 데이터 구조**  
**1. dp[viewpoint / count / n / selection] = value / cost**  
N의 값이 N-X값을 참조하나, N-X에 의해 제한되지 않는다.


**2. dp[viewpoint / n][selection / option] = value / cost**  
N의 값이 N-X값을 참조한다.  
N의 선택 가능한 조합이 N-X에 의해 제한되는 경우, 이전 선택지를 같이 저장하여아 한다.


예제)
- 조합 가능한 수: [2xn 타일링](https://www.acmicpc.net/problem/11726)
- 최대, 최소비용 계산: [피보나치 수열](https://www.acmicpc.net/problem/1003), [막대기](https://www.acmicpc.net/problem/1094)

💡 상향식 풀이의 N번째 판단에서는 N-X에 대해서만 제약조건을 판단한다. 반대로 하향식 풀이의 N번째 판단에서는 N+X에 대해서만 제약조건을 판단한다. (진행 방향의 반대방향에 대해서만 제약조건을 판단함)  
**진행 방향에서의 제약조건 판단이 원할하지 않으면 반대 방향에서의 풀이를 유도해 본다.**

----

#### [탐욕 알고리즘](https://www.acmicpc.net/problem/tag/%EA%B7%B8%EB%A6%AC%EB%94%94%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)

길 찾기, 최적의 방법 찾기 상황에서 현재 상황에 일치하는 최대 가능성을 따라간다. 이전 선택지에서 결정한 최상의 선택지(또는 값)을 저장해 이후의 선택지에 참조하는 것을 메모이제이션으로 구현하여, `다이나믹 프로그래밍`과도 관련이 있다.

**\- 탐욕스러운 선택 조건 (greedy choice property)**
앞의 선택이 이후의 선택에 영향을 주지 않는다. 즉 N-X번의 선택이 N선택에서 제한되지 않는 경우이다.

**\- 최적 부분 구조 조건 (optimal substructure)**
문제에 대한 해결 방법이 부문 문제에 대해서도 최적의 문제 해결 방법이여야 한다.

----

#### [분할 정복](https://www.acmicpc.net/step/20)


----

### 고급 단계
정답률이 낮거나, 상대적으로 답안 제출이 낮은 유형 위주로 정리하였음.
