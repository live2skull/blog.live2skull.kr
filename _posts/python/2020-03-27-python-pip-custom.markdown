---
title:  "private pip(pypi) 서버 구축 및 테스트"
date:   2019-09-01 00:59:09 +0900

toc: true
toc_label: "둘러보기"
toc_icon: "columns"

categories: python pip
tags: python pip
---

Pypi(Python package index)는 파이썬을 위한 공식적인 패키지(third-party) 소프트웨어 배포 서버이며, 다양한 패키지를 설치하기 위해 사용하는 `pip`는 pypi 공식 서버 [pypi index](https://pypi.org/simple/) 에서 패키지를 검색 및 다운로드한다.

패키지 사용이 편리하도록 공개적으로 배포하고 프로젝트에 적용할 수 있지만, 경우에 따라 내부에서 공개할 수 없는 패키지를 관리하는 상황이 생길 수 있습니다.

본 글에서는 private pypi 서버를 구축하고, 개발 환경에서 해당 서버의 패키지를 다운로드 및 업로드 할 수 있게 구성하는 방법을 설명합니다.

## pypi 서버 설치

💡 `pip`는 보안 연결을 사용하지 않을 경우에 호스트 추가 설정이 필요하므로 https 사용을 권장합니다.

## 클라이언트 설정
pypi 서버 설치가 완료되었으면, 패키지 배포 및 설치를 위해 클라이언트 설정 파일을 작성합니다.

### pip
패키지 서버를 추가함으로서 사용자 서버에서 패키지 사용이 가능하도록 합니다.

📝 pip.conf
```
```

### twine
패키지 서버를 추가함으로서 사용자 서버에 패키지 업데이트를 가능하게 합니다.

📝 .pypirc
```
[distutils]
index-servers=
	api
	pypi

[api]
repository:https://custom.pypi.com
username:username
password:password

[pypi]
# pypi.org에 등록된 본인의 계정이 있을 경우 추가합니다.
username:undefined
password:undefined
```
