---
title:  "파이썬 django 프로젝트를 aws lambda 로 서비스하기"
date:   2019-09-01 00:59:09 +0900

toc: true
toc_label: "둘러보기"
toc_icon: "columns"

categories:
    - django
    - aws

tags:
    - django
    - serverless
    - aws
    - aws-lambda
    - zappa
    - python
---

python 기반의 웹 프레임워크인 `django`, `drf (djangorestframework)` 를  


{% include important.html content="Ubuntu 16.04, django 2.2.11 버전에서 테스트하였습니다.<br>
django 상위 버전(3.x) 에서는 로컬 환경에서 문제가 없으나 aws 환경에서 제대로 동작하지 않을 수 도 있습니다.
" %}


## AWS 계정 설정

aws lambda 서비스를 사용할 aws 계정이 필요하다. 계정이 없다면, 생성합니다.  [AWS 계정 생성하기](https://portal.aws.amazon.com/billing/signup#/start)


로컬 환경에서 aws 서비스에 액세스하기 위한 IAM 키를 발급합니다.


## 로컬 환경 준비

zappa 패키지를 프로젝트의 가상환경에 설치합니다.
```
pip install zappa
```

프로젝트의 zappa 설정 파일을 만듭니다. django 프로젝트의 최상위 디렉터리 (manage.py 이 존재하는 디렉터리) 에서 다음 명령을 실행합니다.
```
zappa init
```




## AWS Lambda로 프로젝트 업로드

프로젝트 파일을 aws lambda와 aws api gateway 환경에 업로드합니다.
```
zappa deploy
```


프로젝트에 변경사항이 발생하면, 업데이트하거나 이전 버전으로 되돌릴 수 있습니다.


## 동작 확인 및 트러블슈팅
```
zappa tail
```
