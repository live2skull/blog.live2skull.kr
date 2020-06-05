---
title:  "django - ORM 트랜젝션"
date:   2020-06-05 19:00:00 +0900

toc: true
toc_label: "둘러보기"
toc_icon: "columns"

categories: 
    - django

tags:
    - django
    - python
---

django ORM 에서 트랜젝션을 사용하는 방법에 대해 기술합니다.

## 시작하기 전 - django의 트랜젝션
django 에서는 데이터베이스의 `autocommit` 을 사용하고, 자체적인 transaction management를 사용합니다.

[django docs - autocommit](https://docs.djangoproject.com/en/3.0/topics/db/transactions/#autocommit)

django는 별도의 설정이 없으면 `autocommit` 을 기본적으로 사용하도록 데이터베이스를 구성합니다. 이는 트랜젝션이 필요 없는 코드에서는 작업 결과가 바로 데이터베이스에 적용 될 수 있게 합니다.

트랜젝션을 실행하게 되면 django는 `autocommit` 을 비활성화하여 트랜젝션의 본 기능을 사용할 수 있게 됩니다.

----

## 사용하기
``` >>> from django.db import transaction```

`django.db.transactions` 모듈에 내장된 메서드를 이용하여 트랜젝션 기능을 사용할 수 있습니다.  
내부적으로 `Atomic` 객체를 사용하며, `transaction` 모듈로 동작을 관리합니다.

### transaction.atomic() : 트랜젝션 시작
트랜젝션을 시작하려면, `atomic()` 을 `with` 문으로 컨텍스트 매니저를 사용합니다.  
상황에 따라 `transaction.atomic()`은 다음 작업을 수행합니다.  

#1. 현재 커넥션이 트랜젝션이 아닌 경우 - 실행 시점에서 새로운 트랜젝션을 시작합니다.  
#2. 현재 커넥션이 트랜젝션 내부인 경우 - 실행 시점에서 세이브포인트를 생성합니다.

```
with transactions.atomic():
    ... # 코드 실행
```

|이름|타입|속성|
|-----|----|------|
using|db_dialect(None)|저장할 데이터베이스 dialect
savepoint|bool(True)|False 이면, 이미 트랜젝션 내부인 경우 별도로 세이브포인트를 생성하지 않습니다.

컨텍스트 매니저 내부에서의 실행이 종료되면, `atomic()` 이 반환한 `django.db.transaction.Atomic()` 객체에 의해 다음 작업이 수행됩니다.  

#1. 컨텍스트가 정상적으로 종료된 경우  -  마지막 트랜젝션 / 세이브포인트를 커밋합니다.  
#2. 컨텍스트 코드에서 exception 이 발생한 경우  - 마지막 트랜젝션 / 세이브포인트를 롤백합니다.  

*참고: 컨텍스트 매니저 기능을 작성한 클래스는 마지막으로 코드 블럭 내부에서 발생한 exception을 전달받는 코드로 커밋 / 롤백 여부를 결정하게 됩니다.

----

### transaction.commit() : 트랜젝션 커밋
현재까지 이루어진 작업을 수동으로 커밋합니다. 이렇게 하면 코드블럭의 실행 결과와 관계없이 트랜젝션은 곧바로 종료됩니다.

### transaction.rollback() : 트랜젝션 롤백
현재까지 이루어진 작업을 수동으로 롤백합니다. 이렇게 하면 코드블럭의 실행 결과와 관계없이 트랜젝션은 곧바로 종료됩니다.

### 세이브포인트 수동 제어
다음 방법으로 세이브포인트를 수동으로 생성하고 커밋, 롤백할 수 있습니다.

`savepoint()` : 실행 시점의 세이브포인트를 생성하고, 고유 객체를 생성합니다.  
`savepoint_commit()` : 해당 시점의 세이브포인트를 커밋합니다.  
`savepoint_rollback()` : 해당 시점의 세이브포인트를 롤백합니다.

```
sid = transaction.savepoint() 
try:
    obj.save()
    transaction.savepoint_commit(sid)
except:
    transaction.savepoint_rollback(sid)

print("done!")
```
----

### 기타 사용 방법 : decorator 사용
함수 동작 결과에 따라 트랜젝션을 수행하도록 `decorator`를 사용할 수 있습니다.

```
@transaction.atomic
def do_some_stuff():
    ...

# atomic 컨텍스트 매니저와 동일하게 함수가 종료되면 오류 여부에 따라 커밋 / 롤백 됩니다.
```

### django 뷰에서 기본적으로 트랜젝션 사용

`ATOMIC_REQUESTS` 설정을 True 값으로 사용하면, `non_atomic_requests` 데코레이터를 사용하지 않은 모든 뷰 함수에서 기본적으로 트랜젝션이 사용됩니다.

[django docs - ATOMIC_REQUESTS](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-DATABASE-ATOMIC_REQUESTS)