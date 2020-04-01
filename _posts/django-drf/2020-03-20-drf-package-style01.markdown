---
layout: post
title:  "django drf 앱 패키징 가이드 - 01"
date:   2020-03-23 00:59:09 +0000
categories: django drf python package guide
---

django, djangorestframework을 사용한 앱 패키지의 작성 규칙 및 요령해 대해 기술합니다.

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

설치를 위한 설정값은 `setup.cfg` 또는 `setup.py` 에 `setup(**kwargs...)` 인자값에 가술하여도 무관합니다.  
단, `setup.cfg`에 기술할 경우

### migrations
데이터베이스 스키마의 변경사항으로, django utility로 자동 생성되며, 패키지 및 `.gitignore` 에 포함함을 원칙으로 합니다.


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
사용자의 요청이 잘못되었을 경우, 다른 fall-back 실행 요소가 없으므로 `is_valid(raise_exception=True)`를 기본 사용하여 예외를 발생시킵니다.

client side - 400 Bad Request 반환합니다.  
server side - `sentry_sdk` 사용자 정보를 포함한 오류를 보고합니다.

#### 데이터 크롤링
⚡ 수정 중 : 수집된 데이터의 전처리 과정 구현을 `Model.staticmethod`, `interactions`, `Serializer.to_representation` 어느 곳에 작성하는가?   

\- serializer: custom field를 작성하여 to_representation 전처리 (regex 구현 등)  
\- to_representation, to_internal_value 테스트 및 parser 작성 시도

[Python 데이터 분석 실무 - 데이터 전처리](https://wikidocs.net/16574)

****

### validators - 데이터 검증

```

```

****

### filters - 검색 필드 작성
