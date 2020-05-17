---
title:  "django drf 앱 패키징 가이드 - 00"
date:   2020-03-23 02:00:00 +0900

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
---

django, djangorestframework을 사용한 앱 패키지의 작성 규칙 및 요령해 대해 기술합니다.

{% include important.html content="본 문서는 작성자의 상황에 맞게 적용된 규칙입니다." %}

### 프로젝트 설정

환경변수 설정 및 변수에 따른 디버깅, 로깅(`sentry_sdk`) 적용 파일입니다.

📝 project_name/settings.py

**django, djangorestframework 적용**
<details markdown="1">
<summary>접기/펼치기</summary>
{% include gist.html gist="live2skull/12e8b9ae6b4dff21c7de5a25c33193aa" %}
</details>
</br>

**django, djangorestframework, celery 적용**

****

### 작업 환경 구축

#### application 패키지 개발 환경

💡 jenkins 서버에서 패키지를 별도로 관리하기 위해 폴더를 분리합니다.
- branch에 따른 패키지 빌드 (master/release 등)
- private reposity에 설치 파일 자동 업로드

📂 project directory
```
C:\Users\live2skull\Desktop\web_openapi 디렉터리

2020-03-27  오후 01:26    <DIR>          .
2020-03-27  오후 01:26    <DIR>          ..
2020-03-27  오후 12:29                75 .env
2020-03-27  오후 01:21               921 .gitignore
2020-03-27  오후 01:25    <DIR>          .idea
2020-03-27  오후 01:24    <DIR>          .venv
2020-03-27  오후 01:21               669 manage.py
2020-03-27  오후 12:13    <SYMLINKD>     openapi_jenan_disaster_notify [..\openapi_jenan_disaster_notify\..]
2020-03-27  오후 12:14    <SYMLINKD>     openapi_maps [..\openapi_maps\openapi_maps]
2020-03-27  오후 01:21    <DIR>          web_openapi
```
개발 환경에 사용될 프로젝트 폴더와 실제 배포(제작)할 앱 폴더를 분리하여 관리합니다. 이렇게 하면 `git` 버전 관리 및 `pip` 배포를 좀 더 편리하게 할 수 있습니다.

윈도우 심볼릭 링크 생성 (권한 오류시 관리자 권한으로 실행합니다)
```
D:\...> mklink /d ".\app_name" "app_folder"
```

📂 root directory
```
2020-03-27  오후 01:24    <DIR>          web_openapi
2020-03-27  오후 12:13    <DIR>          openapi_jenan_disaster_notify
2020-03-27  오후 12:14    <DIR>          openapi_maps
```

각 패키지 폴더는 같은 최상위 폴더가 아닌 다른 폴더에 위치하여도 무관합니다.

`ln -s` 명령어 - application 패키지의 src폴더로 심볼릭 링크를 생성합니다.  
패키지는 실제 폴더에서 버전 관리 및 빌드가 가능합니다.


`aws lambda (serverless)` 환경 업로드시에는 `zappa`를 이용하여 업로드합니다.    
[파이썬 django 프로젝트를 aws lambda로 서비스하기](https://blog.live2skull.kr/posts/django-serverless/)
