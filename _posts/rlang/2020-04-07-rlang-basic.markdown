---
layout: post
title:  "R언어 기본 문법 및 함수"
date:   2020-04-07 16:00:00 +0900
categories: rlang
---

R언어의 기본 문법 및 built-in 함수에 대해 정리함.

#### 연산자

**값 대입** `a <- 30`  
**나머지 연산** `b <- 8 %% 5 # 3`  
**빠른 문자열 확인** `cat` `b <- cat('1',123,'b',456) # '1 123 b 456'`  
**사용자 입력값 받기** `n <- readline(prompt='값을 입력하세요')`

----

#### 벡터
1차원 데이터를 저장하기 위한 자료 구조를 R에서 벡터(vector)라고 하며, 수학적 의미와 동일하다.  
벡터는 변수와 달리, 연속된 값을 저장할 수 있다.

일반적인 언어와는 다르게 벡터의 시작 요소의 인덱스가 **0** 이 아닌 **1** 에서 시작한다.

**1차원 벡터(정수, 실수형)**  
`v <- 100:200` 시작값과 끝값을 연속된 숫자 값으로 저장.  
`v <- seq(100, 200, 2) # by=2 : 100, 102, ...` step 설정

**1차원 데이터 벡터(문자열)**  
`v <- c(1, 3, 5) # 1, 3, 5 | num[1:3]`  
`v <- c('a', 'b', 3) # 'a', 'b' , '3' | chr[1:3]`  
데이터 벡터는 문자, 숫자 중 한가지 타입만을 가질 수 있다. (문자, 숫자 두 타입을 동시에 가질 수 없다.)  
벡터 선언 시 문자를 포함하고 있는 벡터에 숫자 타입을 입력할 경우 문자 타입으로 변환된다.

**2차원 데이터 벡터(key:value)**  
데이터 벡터의 구성 값에 이름을 부여함으로써 key:value 관계를 가진 사전형으로 사용할 수 있다.  
#1. 벡터를 생성하고, key와 value를 하나씩 연결.
```
data <- c() # NULL(empty)
data['KIM'] <- 3
print(data) # KIM \n 3
```

#2. 키 벡터와 값 벡터를 연결. 다량의 데이터 대응에 적합.
```
grade <- c(3, 1, 2)
names <- c('KANG', 'SON', 'YANG')
names(grade) # MAP_DICT(VALUES)

print(score) # KANG SON YANG \n 90 80 75
print(score['YANG']) # 2
```

**벡터의 사칙연산**  
길이(요소의 갯수)가 같은 벡터는 사칙연산이 가능하며, 각 인덱스에 위치한 요소와 연산을 수행한다.

**벡터의 연장**  
`v <- v1 + v2`연산은 `벡터의 사칙연산`정의로 인해 두 벡터의 연결이 아닌 각 인덱스 요소 합 벡터를 반환한다. 두 벡터의 연장은 다음과 같다.
`v <- c(v1, v2) | v <- c(v1, v2[idx_start:idx_end])`

----


#### if 문
```
if (expression) {
	statement
} else if (expression) {
	statement
} else {
	statement
}
```

logical expression에서 and, or 기호를 한개만 사용한다.  
and : `if (a > 5 & b < 3)` or : `if (a > 3 || b < 3)`


#### 반복문
```
# like python3 "for i in range(1, 11)"
for (i in 1:10) {
	print(i)
}
```

```
i <- 23
while (i <= 10)
{
	print(i)
	i <- i + 1
}
```

#### 사용자 정의 함수 작성
```
myfunc <- function(a, b) {
	q <- a + b
	return(q)
}

print(myfunc(1, 2)) # 3
```

### 기타 함수
#### 데이터 처리
`sort(vector, decreasing=TRUE/FALSE)` 벡터 정렬. 벡터의 값이 재배치되지 않고 새로운 벡터를 반환함.

#### 연산
`log(x(targ)=, base=)` 로그  
`sqrt(val)` 제곱   
`max(arg0, arg1, ... | vector0, ...)` 최대값 (min - 최소값)  
`abs(vec | val)` 절댓값

#### 소숫점 정리하기
`ceiling(val, digits=0)` 올림  
`round(val, digits=0)` 반올림  
`floor(val, digits=0)` 	 내림

#### 난수 생성
`runif`
