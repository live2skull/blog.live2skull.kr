---
title:  "python pytest 유닛테스트 작성하기"
date:   2021-01-03 22:00:00 +0900

toc: true
toc_label: "둘러보기"
toc_icon: "columns"

categories: python testing
tags: python testing pytest
---

pytest를 이용한 유닛 테스트 방법에 대해 살펴봅니다.

## 1. 테스트 코드 작성 및 테스트 실행

### 유닛 테스트의 작성

유닛 테스트는 전체 기능이 올바르게 동작하는지보다, 각 세부적인 구현 (예: 각각의 메서드)가 올바르게 동작하는지 검증합니다.

### 설치 및 테스트 실행

pytest를 현재 가상 환경에 설치합니다.
```
pip install pytest
```

pytest로 단일 파일 또는 특정 모듈에 대해 테스트를 진행하는 경우는 다음과 같습니다.
```
pytest "단일 파일 또는 특정 모듈 이름"
```

pytest로 현재 디렉터리에서 모든 테스트 파일에 대한 테스트를 진행하는 경우는 다음과 같습니다.
```
pytest
```

### 테스트 코드의 작성

테스트 코드 파일(모듈) 은 `test_*.py`의 형태로 "test"를 파일 명의 접두사로 가져야 하며, 테스트 메서드 마찬가지로 "test"역시 마찬가지로 메서드 명의 접두사로 가져야 합니다.

test_calc.py
```
def test_add_value():
	assert 3 + 4 == 7
```

간단한 테스트 예시입니다. 테스트 코드는 특정 값 또는 실행 결과에 대해 검증을 `assert`문을 통해 검증하게 됩니다.

또는 테스트를 원하는 메서드의 실행 후 지정한 오류가 발생하는지 여부를 검증할 수 있습니다.

```
def test_zero_division():
	with pytest.raises(ZeroDivisionError):
		q = 1 / 0
```

본 테스트 예시와 같이 `pytest.raises(Exception)` 을 `with`문과 함께 지정하여 지정한 오류가 발생하는지 여부를 확인할 수 있습니다. 이 때 오류 클래스는 복수 입력이 가능합니다.

---

## 2. 테스트 값 전달 및 fixture 활용

### 테스트 시작 setup, teardown 코드 작성

다음 예제는 pytest.fixture 데코레이터를 이용해 setup 및 teardown 함수를 작성한 예시입니다. 

```
import pytest

@pytest.fixture
def build_file(request):
	### 임시 파일 생성 코드
	f = open('/tmp/testfile', 'wb')

	def finalize():
		f.close()
		os.remove('/tmp/testfile')	

	### 사용이 종료되고 실행할 finalize 함수 작성
	request.addfinalizer(finalize)
	return f

def test_file_write(build_file):
	build_file.write(b'\x00\x00')
```

테스트 메서드 `test_file_write` 를 작성하며, `build_file`를 인자로 받았습니다.  
이 때, `build_file` 인자는 pytest.fixture 데코레이터로 정의되어 함수명이 동일한 함수명을 실행하고, 해당 결과를 반환하여 테스트 코드에 주입합니다.

### 테스트 변수로 입력

다음과 같이 여러 테스트 코드에 대해 테스트 인자값으로 전달할 수 있습니다.

```
import pytest
@pytest.fixture
def build_argument(request):
	return [(1,2), (3,4)]


def test_add(build_argument):
	# 테스트 코드 작성...

def test_mul(build_argument):
	# 테스트 코드 작성...
```

### 테스트 값(파라메터) 를 테스트 코드에 전달

다음은 `pytest.mark.parametrize` 데코레터를 이용하여 테스트 코드에 여러개의 값을 순차적으로 전달하여 모두 실행하는 예제입니다.

```
@pytest.mark.parametrize("test_input", "expected", [("1+2", 3), ("3+4", 7)])
def test_eval_result(test_input: str, exptected: int):
	assert eval(test_input) == expected
```

`pytest.mark.parametrize` 인자값으로 각각 테스트 코드로 입력될 인자값의 이름과,  
마지막 인자값으로는 `List` 에 각각의 테스트 값을 순서대로 입력함으로써 여러 입력값을 테스트 코드에 실행할 수 있습니다.


-----

## 3. django 프로젝트에서 `pytest-django` 패키지를 사용한 테스트 코드 작성

`pytest-django` 패키지를 사용하여 pytest 유닛 테스트 코드를 작성할 수 있습니다.

다음은 테스트를 위해 테스트 데이터베이스를 초기화하는 예제입니다.

```
import pytest
from .models import User

@pytest.mark.django_db
def test_my_user(client: Client):
	User.objects.create(name="test")
```

다음은 클라이언트 request 목업 요청이 가능한 `django.test.Client` 클래스를 이용하여 특정 URL 기능에 대한 테스트를 진행하는 예제입니다.

```
from django.test import Client
from json import loads

def test_create_user(client: Client):
	response = loads(
		client.post('/api/users/create',
		 data={'id' : 'test', 'password' : 'pw'}).body
	)

	assert response['result'] == True
```