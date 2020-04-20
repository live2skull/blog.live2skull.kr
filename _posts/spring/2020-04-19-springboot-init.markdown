---
layout: post
title:  "Spring Boot 개발환경 구성하기"
date:   2020-04-19 00:00:00 +0900
categories: java spring-boot
---

Jetbrains Intelij 에서 Spring Boot 개발환경을 구성합니다.


## Intelij 설정

`File -> Settings -> Plugins` 플러그인에서 `Spring Assistant` 설치 후 IDE를 재시작합니다.

## 프로젝트 만들기

`File -> New... -> Project` 플러그인에서 `Spring Assistant` 선택

Project SDK  - 13 이상 버전의 java sdk 선택  
Initializr Service URL - default [start.spring.io](https://start.spring.io) 선택


**프로젝트 메타데이터 설정(환경설정)**

|Name|Option|
|---|-----|
|Group|프로젝트 고유 도메인
|Artifact|프로젝트 고유 이름
|Type|빌드 도구 - Gradle Project
|Language|언어 - Java
|Packging|패키징 옵션 - Jar
|Java Version|자바 SDK 버전 - 11

단일 Jar 파일로 컴파일하고자 할 경우 `Jar`, 배포하여 `Tomcat`에서 실행할 경우 `War` 파일로 패키징한다.