---
layout: post
title:  "django drf 앱 패키징 가이드"
date:   2019-09-01 00:59:09 +0000
categories: django drf python package guide
---

{% include important.html content="본 문서는 작성자의 상황에 맞게 적용된 규칙입니다." %}

**django 재사용(배포 및 설치) 가능 패키지의 디렉터리 구조 예시**

```
├── LICENSE
├── MANIFEST.in
├── README.rst
├── openapi_maps
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── coordinate.py
│   │   ├── region.py
│   │   └── street.py
│   ├── serializers
│   │   └── __init__.py
│   ├── tests.py
│   └── views.py
├── setup.cfg
└── setup.py
```


### migrations
데이터베이스 스키마의 변경사항. django utility로 자동 생성된다. 패키지에 포함을 원칙으로 합니다.


### models - 데이터베이스 모델

#### 모델 필드명 작성 요령

다음 가이드를 최대한 준수하되, 예외 상황이 발생할 경우 해당 사유를 주석으로 필히 기록합니다.



#### models.py 파일을 패키지로 작성할 경우

데이터베이스 모델을 정의. 별도의 모듈로 정의할 경우 models/\_\_init\_\_.py 파일에 하위 `django.db.models.Model` 클래스를 상속한 구현 모델을 모두 import 합니다.

📝 models/\_\_init\_\_.py
```
from .region import Region
# 이렇게 해야 cli 인터페이스의 makemigrations, migrate등 데이터베이스 명령이 정상 동작합니다.
```

📝 models/region.py
```
from django.db.models import Model
from django.db.models import BigAutoField, IntegerField, BigIntegerField, CharField, ForeignKey, DecimalField, OneToOneField
from django.db.models import CASCADE

__all__ = ['Region']
# export 옵션을 적용하여 불필요한 타 모듈이 노출되지 않게 합니다.

class Region(Model):

    id = BigIntegerField(primary_key=True)
    name = CharField(null=False, max_length=MAX_REGION_NAME)
    parent = ForeignKey('Region', related_name='children',
                        null=True, on_delete=CASCADE)
```

****

### serializers - 직렬화, 역직렬화

#### 클라이언트 요청 검증

#### 데이터 크롤링 -

****

### validators - 데이터 검증

****

### filters - 검색 필드 작성
