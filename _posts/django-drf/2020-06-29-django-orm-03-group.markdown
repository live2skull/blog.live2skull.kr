---
title:  "django - ORM 집계 함수와 그룹핑"
date:   2020-06-29 12:00:00 +0900

toc: true
toc_label: "둘러보기"
toc_icon: "columns"

categories: 
    - django

tags:
    - django
    - python
---

django ORM 에서 집계 함수와 그룹핑 (`aggregate`, `group by`) 를 사용하는 방법에 대해 기술합니다.

## 시작하기 전 - 집계 함수

|이름|설명|
|---|------|
count|NULL이 아닌 레코드의 수
sum|필드명의 값들의 합계
avg|필드명의 값들의 평균
min|필드명의 값 중 가장 작은 값
max|필드명의 값 중 가장 큰 값

`count`를 제외한 수치를 계산하는 집계 함수는 `NULL` 값을 가진 행의 데이터는 무시하고 계산합니다.

## 시작하기 전 -  `group by`, `having`

### group by
데이터를 특정 열의 값을 가진 데이터들로 하나로 묶습니다. 이 때, 묶임으로써 합쳐진 다른 컬럼의 데이터는 집계 함수를 통해 추출할 수 있습니다. (여러 컬럼에 group by를 사용할 수 있음)

예) 년도, 수업, 수강한 학생, 성적 데이터를 가진 테이블

```
select year, class, avg(score) as average from student_grade where year=2020 group by class having count(student_id) >= 30;

# year, class, average
    2020,    ABCD0001,      80
    2020,    ABCD0002,      75
```
**SQL 작성**

#1. 먼저 2020년도의 데이터에서 추출하고자 합니다. `where` 절에 `year=2020`으로 필터링합니다.

이 때, `where`절에서 필터링 가능한 (집계와 상관없는 조건)은 `where`절에 작성합니다.  
`having`절에서 작성하게 되면 전체 데이터를 처리한 후 필터링하므로 응답 시간이 길어집니다.

#2. 각 수업별로 학생들의 성적 평균을 추출하고자 합니다. `group by class`과 `select class, avg(score)` 으로 학기별 학생들의 점수 평균을 가져옵니다.

#3. 수업 중 수강한 학생이 30명 이상인 수업의 점수만 가져오고자 합니다. 학생 수 1명별로 한개의 row를 가지고 있으므로, 각 수업별로 집계된 데이터의 학생 수를 확인합니다.  
이 데이터는 `where`절에서는 확인할 수 없는 집계된 데이터이므로,
`having` 절에서 필터링합니다.

### having

위 예제와 같이 `group by` 로 생성된 데이터에서 묶인 열 또는 나머지 데이터의 집계 값을 필터링하는 데 사용됩니다. `where` 절로 먼저 필터링 된 데이터에 대해 집계가 실시되고,   
집계된 데이터에서 필터링하게 됩니다.

----

## 사용하기
```>>> from django.db import Sum, Count, Max, Min, Avg```

`django.db` 모듈에 내장된 집계 함수와 `QuerySet`의 `aggregate`, `annotate` 함수로 `group by`, `having` 절 및 집계 기능을 구현할 수 있습니다.

### aggregate()

지정한 쿼리셋에서 지정한 열의 집계 함수를 실행하고 반환합니다.   
일반적인 `QuerySet`의 메서드와 다르게, 실행하면 바로 결과를 반환합니다.

```
Article.objects.filter(title__contains="야식").aggregate(like_avg=Avg("like_cnt"))

# SQL : select AVG("like_cnt") from Article where title LIKE %"야식"%;
# 반환 값 : {"like_cnt": 123}
```

|이름|타입|속성|
|-----|----|------|
재지정할 열이름|집계 함수|해당 열을 집계할 집계함수

`as` 구분으로 지정하는 열 이름을 별도로 지정하지 않으면, `aggregate`로 생성하는 집계 데이터의 열 이름은 **집계대상열이름__집계함수이름** 으로 생성됩니다.  
예) ```queryset.aggregate(Count(price))```  : price__count

**참고**  
#1. `QuerySet` 이 아닌 실행 결과를 반환하므로, 쿼리셋의 맨 마지막에 작성합니다.  
#2. `values` 메서드를 이용한 `group by` 쿼리를 실행하지 않습니다. `group by` 절을 사용하려면 `annotate` 메서드를 사용합니다.


----

### annotate

`annotate` 메서드는 다음 기능을 구현합니다.

#1. SELECT 대상의 필드 명을 변경  
#2. `values` 메서드와 함께 사용하여 `group by`, `having` 절을 구현

#### 열 이름을 변경하거나, select 대상의 열을 지정

```
from django.db import F

# like_cnt 열의 이름을 cnt로 변경합니다.
Article.objects.all().annotate(cnt=F("like_cnt"))
```

#### `group by`, `having` 절을 구현

위 `group by` 예제와 같이 `where` 절과 `having` 절에 지정할 필터를 구분하고, 작성합니다.

`values` 메서드로 `group by` 대상의 열을 지정하고, `annotate` 함수로 집계된 데이터에서 집계 함수를 실행할 수 있습니다.

```
select year, class, avg(score) as average from student_grade where year=2020 group by class having count(student_id) >= 30;
```

```
StudentGrade.objects
    .filter(year=2020) #1
    .values("class") #2
    .annotate(student_count=Count("student_id"), score_average=Avg("score")) #3
    .filter(student_count__gte=30) #4
    .values("score_average") #5
```

**각 메서드의 설명**  

#1. `group by`절 사용 전 `where`절의 필터링을 지정합니다.  이 때, 외래키를 가진 모델의 `INNER JOIN`을 사용할 수 있습니다.  
#2.  `group by` 의 대상이 되는 컬럼을 지정합니다.  
#3. 집계 함수로 계산할 열을 지정합니다. 이 때, `지정할 열 명` = `집계함수(집계될 열 명)` 으로 지정합니다.  
#4. `group by`가 지정된 `QuerySet` 에서 다시 필터링을 지정합니다. 이 때는 `having` 절로 필터링됩니다.  
집계 된 데이터에서 필터링시에는 `lookup_expr` 을 사용할 수 있습니다.    
#5. 마지막으로 `select` 할 데이터를 선택합니다. (선택사항 - score_average 만 추출할 경우)

**참고**

#1. `group by` 가 사용된 SQL문에서는 `where` 또는 `having` 절에 일치하는 데이터가 없다면 집계 함수를 사용하였더라도 반환되는 행의 갯수가 0 입니다.  
#2. `group by` 가 사용되지 않은 SQL문에서는 `where` 절에 일치하는 데이터가 없더라도, 명시적으로 `NULL` 값을 포함한 한 개의 행이 반환됩니다.