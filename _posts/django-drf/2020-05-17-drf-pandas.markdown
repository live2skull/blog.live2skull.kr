---
title:  "djangorestframework - pandas 로 csv, xlsx 생성하기"
date:   2020-05-17 15:00:00 +0900

toc: true
toc_label: "둘러보기"
toc_icon: "columns"

categories: 
    - django
    - djangorestframework

tags:
    - django
    - djangorestframework
    - python
    - pandas
---

django, djangorestframework에서 ORM으로 데이터베이스에 저장된 데이터를 `csv`, `xlsx` 파일 등으로 저장하는 방법에 대해 알아봅니다.

##  사용할 패키지 선택하기

[drf-renderer documentation](https://www.django-rest-framework.org/api-guide/renderers/)

djangorestframework 에서는 `Renderer` 개념의 객체를 제공하며,   
이를 통해 `Serializer`로 데이터베이스의 데이터를 직렬화 한 값을 json, csv, xlsx 등의 원하는 형식으로 출력할 수 있게 합니다.

drf 공식 문서에서는 json 랜더러를 기본적으로 제공하며 추가적인 포맷으로 사용할 수 있는 패키지를 제공하고 있으며, 그중 사용자가 많고,
파이썬 데이터 분석 프레임워크인 `pandas` 를 이용해 데이터 변환을 제공하는 `django-rest-pandas` 패키지를 사용하기로 결정했습니다.

[pandas github](https://github.com/pandas-dev/pandas)
[django-rest-pandas](https://github.com/wq/django-rest-pandas)

본 글에서는 `django-rest-pandas` 에서 제공하는 랜더러 중 csv, xlsx 데이터를 출력하는 두 랜더러 (`PandasCSVRenderer`, `PandasExcelRenderer`) 를 간단하게 사용하는 방법을 다루겠습니다.

... 추가예정

## 패키지 설치

## 구조 살펴보기

## 커스텀 `ViewSet` 만들기

## 정리