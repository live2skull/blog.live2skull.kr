---
layout: post
title:  "django drf 앱 패키징 가이드 - 00"
date:   2020-03-23 02:00:00 +0000
categories: django drf python package guide
---

django, djangorestframework을 사용한 앱 패키지의 작성 규칙 및 요령해 대해 기술합니다.

{% include important.html content="본 문서는 작성자의 상황에 맞게 적용된 규칙입니다." %}

### 프로젝트 설정

환경변수 설정 및 변수에 따른 디버깅, 로깅(`sentry_sdk`) 적용 파일.

📝 project_name\/settings.py

**django, djangorestframework 적용**
{% include gist.html gist="live2skull/12e8b9ae6b4dff21c7de5a25c33193aa" %}


**django, djangorestframework, celery 적용**
