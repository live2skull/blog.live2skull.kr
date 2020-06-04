---
title:  "django - ORM 기본"
date:   2020-05-28 00:30:00 +0900

toc: true
toc_label: "둘러보기"
toc_icon: "columns"

categories: 
    - django

tags:
    - django
    - python
---

django ORM 개념 및 예제 모음입니다.

# django ORM

## QuerySet
인스턴스 검색 시, `get()` 메서드를 제외한 대부분의 메서드는 검색 결과가 아닌, `QuerySet`의 인스턴스를 반환합니다.

`QuerySet`은 객체의 값에 접근 (print로 읽거나, for 문이나 `list()` 로  iteration을 수행) 하는 시점에 쿼리를 실행하고 결과를 반환합니다.

```
# 이 때는 실제 데이터베이스에 쿼리가 실행되지 않습니다.
query = Article.objects.all() # type: QuerySet

# 전체 데이터에 대한 쿼리를 실행합니다.
for obj in query:
    print(obj.name)
```

### 검색 데이터 갯수(limit), 위치(offset) 지정
갯수와 위치를 지정하는 `QuerySet` 인스턴스를 반환합니다.

마지막 데이터부터 추출하는 음수 지정은 지원하지 않습니다.
이 경우 양수값을 사용하면서, 역순부터 탐색할 필드를 `order_by()` 메서드로 지정하여 사용할 수 있습니다.
```
# "LIMIT 1 OFFSET 5" 쿼리가 추가됩니다.
Article.objects.all()[5]

# "LIMIT 5 OFFSET 5" 쿼리가 추가됩니다.
Article.objects.all()[5:10]

# "LIMIT 1000" 쿼리가 추가됩니다.
Article.objects.all()[:1000]
```

----

## 인스턴스 검색
### lookup_expr 개념
`django`는 객체의 검색을 쉽게 하기 위해 필드 이름에 '__`lookup_expr`' 를 붙여 검색할  수 있는 기능을 제공합니다.

#### 필드 값에 대한 옵션
값이 정확이 일치하는 형태 `=` 가 아닌 다양한 비교 연산자, NULL, 문자열 검색을 지원합니다.

**일반 값 타입입니다.**
|이름|속성|
|-----|-------|
gt|지정 값보다 큰 경우
gte|지정 값보다 크거나 같은 경우
lt|지정 값보다 작은 경우
lte|지정 값보다 작거나 같은 경우
isnull|지정 값이 NULL인 경우

**문자열 타입입니다.**
|이름|속성|
|-----|-------|
contains|문자열 - 값을 포함하는 경우
exact|문자열 - 값이 정확히 일치하는 경우
startswith|문자열 - 값으로 시작하는 경우
endswith|문자열 - 값으로 끝나는 경우

```
# 조회수가 30보다 크거나 같은 인스턴스를 조회합니다.
Article.objects.filter(view_count__gte=30)
```


#### 연관된 객체에 대한 옵션
`ManyToManyField`, `ForeignKey`, `OneToOneField` 로 연관된 객체에서, 자신의 객체와 연관된 객체의 필드값에 바로 접근하거나, 쿼리 연산할 수 있습니다.

```
class User():
    id = BigAutoField(primary_key=True)
    name = CharField(null=False)

class Article():
    id = BigAutoField(primary_key=True)    
    user = ForeignKey(User, related_name="articles", on_delete=DO_NOTHING)

# 작성자가 "live2skull" 인 Article을 필터링
Article.objects.filter(user__name="live2skull")
```

*참고: 이 때, `User` 를 참조하는 `Article` 에서 `user_id` 로 외래키 값을 저장하며, 코드에서 값을 할당하거나 읽을 수 있습니다.

`ManyToMany` 관계에 있는 경우 다음 검색을 사용할 수 있습니다.

**__in** : A객체가 연관된 B객체 필드가 해당 값을 가지고 있는 경우. `iterable` 자료형으로 primary_key 또는 instance 형 데이터를 넘겨줍니다.  

*참고: 자료형에 저장된 모든 객체를 가진 자료가 아닌, 객체 각각을 가지고 있는 모든 결과를 필터링합니다. 각각에 대해 확인하려면 하나씩 필터링해야 합니다.

```
q = Advertise.objects.filter(...)
for _id in ids:
    q = q.filter(datas__in(_id,)) # tuple 형으로 하나씩 필터링
```

### Q() : 쿼리 확장
`Q` 클래스를 이용하여 쿼리문을 런타임 중 유동적으로 작성하고, AND, OR 연산을 할 수 있습니다.

`Q` 인스턴스에 쿼리할 조건을 입력해 AND, OR, NOT 조건으로 묶고, 최종적으로 `QuerySet` 인스턴스에 적용하여 쿼리를 실행하게 됩니다.

예) 이름에 "책" 은 포함하지만 "책상"은 포함하지 않는 데이터를 검색하고자 합니다.
```
q = Q()

q.add(Q(name__contains="책) | Q(name__contains="책상"), q.AND)
Article.objects.filter(q) # QuerySet 인스턴스에 적용하여 쿼리
```

----

**지금부터 서술하는 메서드는 Model.objects: Manager 또는 QuerySet 에서 사용할 수 있습니다.**

### get() : 단일 인스턴스 검색
인자값과 일치하는 객체를 검색해 인스턴스를 반환합니다. 다음 경우에는 해당 오류가 발생합니다.  
`Model.DoesNotExist` : 인자값과 일치하는 객체가 존재하지 않음  
`Model.MultpleObjectReturned` : 인자값과 일치하는 객체가 한 개 이상임

```
# return - instance: Model

try:
    obj = Article.objects.get(name="article 1")
except Article.DoesNotExist:
    pass
except Article.MultipleObjectReturned:
    pass
```

### all() : QuerySet 작성
전체 객체를 가져오는 QuerySet을 생성합니다.
```
queryset = Article.objects.all()
```

### filter() : QuerySet 작성
인자값 또는 QuerySet을 필터링하는 새로운 QuerySet을 생성합니다.
```
queryset = Article.objects.filter(name__contains="책")
```

### values() : 검색 최적화 - 원하는 필드만 검색
지정한 열의 데이터만을 쿼리하는 새로운 `QuerySet`을 생성합니다.  
`django`  는 기본적으로 모델 인스턴스의 모든 열의 데이터를 가져옵니다. 필요한 데이터의 열이 정해져 있을 경우, 쿼리 시간을 단축할 수 있습니다.   

`QuerySet`이 실행되면, 각 데이터의 model instance 가 아닌 지정한 열이 포함된 `dict` 데이터를 반환합니다.

```
# {"name" : "안녕하시죠?", user_id : 123}
result = Article.object.values("name", "user_id").get(id=1) 
```

### values_list() : 검색 최적화 - 원하는 필드만 검색
지정한 열의 데이터만을 쿼리하는 새로운 `QuerySet`을 생성합니다.   
`values()` 메서드와 동일한 역할을 하며, 반환 데이터는 지정한 열 순서의 `tuple` 데이터를 반환합니다.

```
# ("안녕하시죠?", 123)
result = Article.object.values("name", "user_id").get(id=1) 
```

### order_by() : 정렬
정렬할 필드명을 순서대로 정의하는 새로운 `QuerySet`을 생성합니다.   
기본값은 ASC(오름차순) 이며, DESC(내림차순) 정의시 필드명 앞 '-' 을 사용합니다.

```
queryset = Article.objects.all().order_by('-id') # id 값으로 내림차순 정렬
```

### exists(): 존재 여부 확인
`QuerySet` 의 결과가 존재하는지 쿼리한 결과를 반환합니다.
```
# return - bool
is_exist = queryset.exists()
```

### count(): 쿼리 결과 확인
`QuerySet` 의 결과 갯수를 쿼리한 결과를 반환합니다.
```
# return - int
row_count = queryset.count()
```

----

## 인스턴스 생성
### Model.objects.create() : 새로운 인스턴스 생성
인자값으로 객체를 데이터베이스에 생성하고, 해당 인스턴스를 반환합니다.
```
# return - instance: Model

obj = Article.objects.create(
    name="article 1", body="body 1"
)
```

### get_or_create() : 새로운 인스턴스 생성 또는 탐색
`defaults` 값을 제외한 인자값으로 `get()`을 시도합니다. 객체를 찾으면 반환하며, 그렇지 않으면 인자값과 `**defaults` 로 인스턴스를 만듭니다.
```
# return - tuple(instance: Model, created: bool)

obj, created = Article.objects.get_or_create(
    name="article 1",  defaults={"body":"1234}   
)
```
----

## 인스턴스 수정

----

## 인스턴스 삭제
