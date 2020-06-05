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
- Iteration
- Slicing (배열 인덱스 접근)
- Pickling / Caching
- `repr()`, `len()`, `list()`, `bool()`

[django db 최적화 - peoplefund](https://tech.peoplefund.co.kr/2017/11/03/django-db-optimization.html)

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

[django db - Caching and QuerySets](https://docs.djangoproject.com/en/1.8/topics/db/queries/#caching-and-querysets)

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
```>>> from django.db.models import Q```

`Q` 클래스로 쿼리문을 런타임 중 유동적으로 작성하고, AND, OR 연산을 할 수 있습니다.

`Q` 인스턴스에 쿼리할 조건을 입력해 AND, OR, NOT 조건으로 묶고, 최종적으로 `QuerySet` 인스턴스에 적용하여 쿼리를 실행하게 됩니다.

예) 이름에 "책" 은 포함하지만 "책상"은 포함하지 않는 데이터를 검색하고자 합니다.
```
q = Q()

q.add(Q(name__contains="책) | Q(name__contains="책상"), q.AND)
Article.objects.filter(q) # QuerySet 인스턴스에 적용하여 쿼리
```

### F(): 필드 참조
```>>> from django.db.models import F```

`F` 클래스로 쿼리문에서 필드 값을 상수값이 아닌 다른 필드 값으로 지정해서 비교 / 연산할 수 있습니다.

```
# 필드의 자기 자신의 값을 더합니다.
Article.objects.update(view_cnt=F('view_cnt') + 1)

# 다른 필드 값을 참조해 SELECT 쿼리를 실행합니다.
Article.objects.filter(title=F('body'))
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

### select_for_update() : 검색 데이터 LOCK
SELECT 결과로 선택되는 데이터를 ROW LOCK 하는 새로운 `QuerySet`을 생성합니다.  

ROW LOCK 이 적용된 데이터는 DML(UPDATE, DELETE)문을 호출할 시 실행되지 않고, LOCK 이 풀릴 때까지 대기하게 됩니다.

여러개의 서버를 운영하는 환경에서 동시성 문제를 제어하고자 할 때 사용합니다.

```
from django.db import transaction

with transaction.atomic():
    # 이미 잠금되어 있다면, 잠금이 끝날 때 까지 기다리게 됩니다.
    obj = Article.objects.select_for_update()
    obj.memo = "확인"
    obj.save()
    # with 문이 종료되며 LOCK이 풀립니다.

print("done!")
```

|이름|타입|속성|
|-----|----|------|
no_wait|bool(False)|LOCK이 걸려 있다면, 대기하지 않고 바로 시도합니다.
skip_locked|bool(False)|LOCK 상태와 상관없이 SELECT 합니다.
of|tuple(model:str, field:str)(())|LOCK 대상 모델과 필드. 기본값은 SELECT 모델의 primary_key 입니다.

*참고: `no_wait`, `skip_locked` 는 MySQL에서는 지원하지 않으며, backend에서 지원해야 사용 가능합니다.

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
### 빈 인스턴스 작성
빈 인스턴스를 생성합니다. 메모리에만 존재하며, `save()` 를 호출하기 전까지 데이터베이스에 저장되지 않습니다.
```
article = Article()
article.title = "게시물 내용"
article.body = "게시물 제목"

# 데이터베이스에 저장
# primary_key=True 필드가 자동 생성이 아니며, 값이 설정되지 않으면 오류 발생.
article.save()
```

### Model.objects.create() : 새로운 인스턴스 생성
인자값으로 객체를 데이터베이스에 생성하고, 해당 인스턴스를 반환합니다.
```
# return - instance: Model

obj = Article.objects.create(
    name="article 1", body="body 1"
)
```

### get_or_create() : 새로운 인스턴스 생성 또는 탐색
`defaults` 값을 제외한 인자값으로 `get()`을 시도합니다. 객체를 찾으면 반환하며, 그렇지 않으면 인자값과 `**defaults` 로 인스턴스를 만들고 반환합니다.
```
# return - tuple(instance: Model, created: bool)

obj, created = Article.objects.get_or_create(
    name="article 1",  defaults={"body":"1234}   
)
```

### bluk_create(): 빈 인스턴스 다중 생성

생략 - MySQL 에서 사용하기에 적합하지 않습니다.  
#1.  `save()` 메서드가 실행되지 않음.    
#2. `AutoField()` 를 primary_key로 가지고 있을 경우, backend 가 지원하지 않는 경우 값 설정이 불가능함.


----

## 인스턴스 수정

### save() : 인스턴스
인스턴스의 필드 값을 저장합니다.   
빈 인스턴스이고, primary_key 필드값을 지정하지 않고 Auto 필드이면 값이 자동 설정됩니다.

```
# return - None

obj = Article.objects.get(id=1)
obj.body = F("body") + "내용 추가"
obj.save()
```

|이름|타입|속성|
|-----|----|------|
force_insert|bool(False)|강제로 INSERT 문을 사용합니다. 일반적으로 사용하지 않습니다.
force_update|bool(False)|강제로 UPDATE 문을 사용합니다. 일반적으로 사용하지 않습니다.
using|db_dialect(None)|저장할 데이터베이스 dialect
update_fields|iterable(None)|저장할 필드를 지정합니다. 비어있다면 저장되지 않습니다.

**지금부터 서술하는 메서드는 Model.objects: Manager 또는 QuerySet 에서 사용할 수 있습니다.**

### update() : 쿼리된 인스턴스 업데이트
`QuerySet` 에 일치하는 인스턴스의 값을 인자값으로 업데이트 후, 변경된 데이터 갯수를 반환합니다.

*참고: 인스턴스의 값은 SQL UPDATE로 일괄적으로 변경되며, `save()` 메서드가 호출되지 않습니다. 따라서, 변경된 각 인스턴스의 `pre_save`. `post_save` 시그널이 실행되지 않게 됩니다.

```
# return - int

cnt_affected = Article.objects.filter(title__contains="nodejs").update(view_count=10)
```

### update_or_create() : 쿼리된 단일 인스턴스 변경 또는 생성
`defaults` 값을 제외한 인자값으로 `get()`을 시도합니다. 객체를 찾으면 `**defaults` 값으로 `update()`를 호출합니다.  
그렇지 않으면 인자값과 `**defaults` 로 새로운 인스턴스를 만들고 반환합니다.

`QuerySet`에 사용하면 인자값과 필터를 합쳐 확인하고, 위와 동일하게 실행됩니다. 이 때 `QuerySet` 필터 값은 새로운 객체에는 반영되지 않습니다.

*참고: `get`이 사용되므로 2개 이상의 객체가 발견되면 `Model.MultipleObjectReturned` 오류가 발생합니다.

```
# return - tuple(instance: Model, created: bool)

obj, created = Article.objects.update_or_create(
    id=123,  defaults={"view_count": 30}   
)
```

### bulk_update() : 지정한 인스턴스 변경사항 업데이트
전달된 각 인스턴스의 지정한 필드를 하나씩 `save()` 메서드와 동일히 업데이트합니다.  
`update()` 와 다르게, 이미 인스턴스로 불러온 객체를 하나씩, 지정한 필드만 업데이트하게 됩니다.

*참고: bluk_save() 의 역할로 생각하면 이해하기 쉽습니다.  
*참고: 지정하지 않은 필드는 무시되므로, 대상 객체의 변경 필드를 명확히 하지 않으면 데이터 누락이 발생할 수 있습니다.

```
# return - None

# Article() 인스턴스가 생성됩니다.
objs = [
    Article.objects.create(id=1),
    Article.objects.create(id=2)  
] 

objs[0].title = "제목1"
objs[1].title = "제목2"

Article.objects.bulk_update(objs, ['title']])
```

|이름|타입|속성|
|-----|----|------|
objs|iterable|업데이트를 수행할 객체의 집합입니다.
fields|iterable|업데이트를 수행할 필드 집합입니다. 비어있다면, 실행되지 않습니다.
batch_size|int(None)|한 쿼리당 업데이트될 인스턴스의 갯수입니다. 지정하지 않으면 django 가 결정합니다.

----

## 인스턴스 삭제

### save() : 인스턴스, QuerySet 결과 객체 삭제
인스턴스 또는 QueryuSet 결과를 데이터베이스에서 삭제합니다. DELETE 쿼리가 실행됩니다.  
반환값으로 삭제된 데이터의 행 갯수가 반환됩니다.

```
# return - int

# 단일 객체 인스턴스 삭제
obj = Article.objects.get(id=1)
deleted_cnt = obj.delete()

# 쿼리와 일치하는 객체 일괄 삭제
queryset = Article.objects.filter(name__contains="django")
deleted_cnt = queryset.delete(0)
```

|이름|타입|속성|
|-----|----|------|
using|db_dialect(None)|저장할 데이터베이스 dialect
keep_parents|bool(False)|True이며 모델이 타 모델의 외래키 연결을 가지고 있으면 자신은 삭제하지 않고 연결된 자식 모델만 삭제합니다.

*참고: `keep_parents` - 삭제되는 대상은 자신을 가리키는 모델을 지정합니다.