---
layout: post
title:  "알고리즘 문제 유형별 풀이"
date:   2019-09-01 00:59:09 +0000
categories: python pip algorithm
---

## 알고리즘 문제 풀이
[백준 Online Judge](https://www.acmicpc.net/)

[백준 - 분류별 태그](https://www.acmicpc.net/problem/tags)

----

## 유형별 정리

### 시작 단계

#### [출력](https://www.acmicpc.net/problem/tag/%EC%B6%9C%EB%A0%A5)

콘솔 입/출력(stdin/stdout)에 대해 다룬다.

단순히 특정 글 또는 로고 출력만이 필요할 경우 (문제에 입력이 없고, 정답이 항상 동일한 경우) 코드 제출 단계에서 언어를 `Text`로 지정하면 소스 코드가 아닌 답 자체를 제출할 수 있다.

다량의 입/출력 과정에서 발생할 수 있는 시간 초과에는 다음과 같이 대응한다.

**🧭 파이썬 예제**  
[python3 - input()과 sys.stdin.readline 성능 비교](https://stackoverflow.com/questions/22623528/sys-stdin-readline-and-input-which-one-is-faster-when-reading-lines-of-inpu)
```
sys.stdin.readline().strip() # readline()은 줄 개행 문제를 포함합니다.
```

**🧭 자바 예제**
```
// java.io.Scanner => ... 작성 중

```


----

### 기본 단계

#### [수학](https://www.acmicpc.net/problem/tag/%EC%B6%9C%EB%A0%A5)

|-|설명|
|---|-----|
|방정식|N일때의 값 K, K가 되는 N 구하기.|
|수열|등차수열, 등비수열, 계차수열 - N에서 값,합|
|순열과 조합|조합 가능한 경우의 수. 순열 / 조합으로 별도 분류|

#### [시뮬레이션](https://www.acmicpc.net/problem/tag/%EC%8B%9C%EB%AE%AC%EB%A0%88%EC%9D%B4%EC%85%98)

다양한 상황이 주어지면 순차적으로 실행하면서 특정 상황이 되는 경우를 찾는다.  
`수학` 유형과 달리 n번쨰 상황에서의 결과값을 수식으로 정의하지 못하는 경우 카운터 변수를 두고 상황을 단계별로 시뮬레이션한다.


#### [정렬](https://www.acmicpc.net/problem/tag/%EC%A0%95%EB%A0%AC)



\#1. 정렬 알고리즘을 구현하거나, 상황에 맞게 변형하여 사용한다.

\#2. 정수, 문자열의 정렬(아스키 코드 기준)을 다룬다.  
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

#### [다이나믹 프로그래밍](https://www.acmicpc.net/problem/tag/%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)




----

### 고급 단계
정답률이 낮거나, 상대적으로 답안 제출이 낮은 유형 위주로 정리하였음.
