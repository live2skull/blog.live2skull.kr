---
layout: post
title:  "R언어 데이터구조 - matrix, dataframe"
date:   2020-04-10 20:00:00 +0900
categories: rlang
---

R언어의 matrix와 dataframe, 논리 벡터를 다루어 봅니다.

### matrix

vector가 1차원 배열을 다룬다면, matrix에서는 2차원 배열을 다루며, 저장된 데이터 타입은 모두 동일하다. (주로 실수, 정수형 데이터를 다룬다.)

**생성**
```
z <- matrix(1:10, nrow=4, ncol=5) # data, 행(가로), 열(세로)

[,1] [,2] [,3] [,4] [,5]
[1,]    1    5    9    3    7
[2,]    2    6   10    4    8
[3,]    3    7    1    5    9
[4,]    4    8    2    6   10
```

`rbind`, `cbind` 결합을 위해서는 각각 행, 열의 갯수가 맞아야 한다. (빈 구간을 채워주지 않는다)

**생성 - 1차원 벡터의 결합**
```
x <- 1:4
y <- 5:8

## 각 1차원의 데이터를 순서대로 N번째 열로 합쳐 matrix를 반환합니다.
m1 <- cbind(x,y) # column bind

## 각 1차원의 데이터를 순서대로 N번째 행으로 합쳐 matrix를 반환합니다.
m2 <- rbind(x,y) # row bind
```

**생성 - matrix와 1차원 벡터 / matrix 의 결합**
````
m1 <- cbind(x,y) # column bind
m3 <- rbind(m1, m1)
m4 <- rbind(m1, x)
````

**값 접근**
```
z[1,2] # 1행 2열에 있는 값
z[3,] # 3행에 있는 모든 값(벡터)
z[,5] # 5월에 있는 모든 값(벡터)
```


**행, 열에 이름 할당 및 접근**  
행, 열에 이름을 할당하여 matrix를 시각화하는데 유용하게 사용합니다.
```
d <- matrix(1:8, nrow=4, ncol=2)
rownames(m) # 설정되어 있다면 vector, 없다면 NULL 반환
rownames(m) <- c('Student1', 'Student2')
colnames(m) <- c('국어', '영어', '수학', '탐구')

d # d 출력
국어 영어 수학 탐구
Student1    1    3    5    7
Student2    2    4    6    8
```

각 행과 열에 이름이 설정되었다면 인덱스처럼 접근할 수 있습니다.

```
d['Student1',]

d # d 출력
국어 영어 수학 탐구
   1    3    5    7
```

----

### dataframe

2차원 배열인 점에서는 matrix와 동일하나, 저장된 데이터 타입이 여러개인 점에서 다르다. 단, 저장된 데이터들은 컬렴별로는 동일한 데이터 타입을 가져야 한다.  
해당 특성을 제외하고는 matrix와 동일하게 다룰 수 있다.

**생성**  
벡터와 데이터 벡터를 결합하여 dataframe을 생성한다.
```
food <- c("pizza", "chicken", "ramen")
rank <- c(1, 2, 3)

information <- data.frame(food, rank)
rownames(information) # [1] '1' '2' '3'
colnames(information) # [1] 'pizza' 'chicken' 'ramen'

food rank
1   pizza    1
2 chicken    2
3   ramen    3
```
`data.frame` 함수를 이용해 입력한 순서대로 각 열을 구성하는 matrix가 생성되었으며, 각 변수의 이름이 matrix의 `colnames`가 된다.


**dataframe 체크** `is.data.frame(information) # TRUE or FALSE`  

**행 / 열 별 데이터 접근**  
dataframe에만 적용되고, matrix에서는 적용되지 얺거나 다르게 동작합니다.
```
information[, 'food'] # vector 'pizza', 'chicken', 'ramen'
information['food'] # dataframe 1xn - vector에서는 다르게 동작함
information$food # vector
```

접근하고자 하는 행 / 열의 상세 정의
```
iris[,c(1:3)] # 1번째부터 3번째까지의 열 데이터
iris[,c(1,3,5)] # 1, 3, 5번째의 열 데이터
iris[c(5,6,7),] # 5, 6, 7번째의 행 데이터
iris[c(5,6,7), c(1,2)] 5, 6, 7번째의 행 데이터 에서 1, 2번째의 열 데이터
```

컴마로 구성되는 범위 선택이 아닌 인덱스 선택의 경우 여러개를 선택하려면 `c(idx1, idx2, ...)`를 이용하여 선택한다. 이 때, 범위 선택과 인덱스 선택을 동시에 사용 할 수 있다.

----

### matrix, dataframe 다루기

💡 `head`, `tail` 은 데이터셋의 일부분을 잘라서 새로운 `list`를 생성한다.

#### 테이블 정보 확인

|함수|반환 형식|설명|
|---|----|-----|
|`dim(df)`|vector|행과 열의 수|
|`nrow(df)`|integer|행의 수|
|`ncol(df)`|integer|열의 수|
|`names(df)`|vector|컬럼이름 보이기 (==colnames) ret: vector  
|`head(df)`|list|데이터셋의 앞부분 일부
|`tail(df)`|list|데이터셋의 뒷부분 일부 ret: list (data.frame == list?)
|`str(df)`|NULL|데이터셋 요약 보기 - 요약정보는 콘솔에 출력하고, 반환하지 아니함|
|`unique(df[,'col1'])`|integer **?**|중복된 값을 제외한 데이터 리스트
|`table(df[, 'col1'])`|integer **?**|중복된 값을 제외한 데이터 리스트와 갯수

⚠️ `colSums(iris)` **?** : 'x'는 반드시 수치형이여야 합니다.

#### 산술연산

|함수|반환 형식|설명|
|---|----|-----|
|`colSums(df[,-5])`|double **?**|열별 합계
|`colMeans(df[,-5])`|double **?**|열별 평균
|`rowSums(df[,-5])`|double **?**|행별 합계
|`rowMeans(df[,-5])`|double **?**|행별 평균


#### 조건에 맞는 행 추출
`subset(df, [expression])` 조건에 맞는 행(row) 추출

소스 matrix, dataframe의 rownames, colnames는 보존된다.

```
RES.1 <- subset(iris, Petal.Width > 2 & Sepal.Width < 5)
RES.1

Sepal.Length Sepal.Width Petal.Length Petal.Width   Species
101          6.3         3.3          6.0         2.5 virginica
103          7.1         3.0          5.9         2.1 virginica
105          6.5         3.0          5.8         2.2 virginica
106          7.6         3.0          6.6         2.1 virginica
110          7.2         3.6          6.1         2.5 virginica
113          6.8         3.0          5.5         2.1 virginica
115          5.8         2.8          5.1         2.4 virginica
116          6.4         3.2          5.3         2.3 virginica
118          7.7         3.8          6.7         2.2 virginica
...
```
