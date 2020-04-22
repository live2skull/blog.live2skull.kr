---
layout: post
title:  "Spring Boot 개발환경 구성하기"
date:   2020-04-19 00:00:00 +0900
categories: java spring-boot
---

Jetbrains Intelij 에서 Spring Boot 개발환경을 구성하고 테스트해 봅니다.


## Intelij 플러그인 설치

`File -> Settings -> Plugins` 플러그인에서 `Spring Assistant` 설치 후 IDE를 재시작합니다.

## 프로젝트 만들기

### 기본 정보 입력

`File -> New... -> Project` 프로젝트 종류 `Spring Initializr` 

**Project SDK** : Java 11 버전 이상의  설정한다. Intelij 내장 SDK 사용도 가능하지만, 가급적이면 별도로 설치한 `JAVA_HOME`등 설정이 완료된 SDK를 사용한다.  
**Initializr Service URL** : default [start.spring.io](https://start.spring.io) 선택

### 프로젝트 메타데이터 설정(환경설정)

|Name|Option|
|---|-----|
|Group|프로젝트 고유 도메인
|Artifact|프로젝트 고유 이름
|Type|빌드 도구 - Gradle Project
|Language|언어 - Java
|Packging|패키징 옵션 - Jar
|Java Version|자바 SDK 버전 - 11

단일 Jar 파일로 컴파일하고자 할 경우 `Jar`, 배포하여 `Tomcat`에서 실행할 경우 `War` 파일로 패키징한다.

### 의존성 패키지 설치

**Spring Initializr** 는 주로 사용하는 패키지를 프로젝트 생성이세 자동으로 설치해 준다. 사용자 환경에 맞게 원하는 패키지를 선택한다.


## 빌드, 실행 및 디버깅

⚠ 프로젝트를 처음 실행하고 Intelij에서 캐싱, configure build가 완료되기 까지 Run/Debug, 빌드 설정이 잡히지 않습니다. 환경에 따라 수 분이 소요될 수 있으니 여유를 가지고 기다립니다.

**빌드** : gradle-wrapper (/gradlew)로 빌드하고 /gradle/wrapper/graddle-wrapper.properties 설정을 따릅니다.   
배포 전 빌드된 `class`파일은 `/build` 디렉터리에 저장된다.

**실행 / 디버깅** : 빌드된 파일의 메인 클래스 파일을 자바 인터프리터로 직접 실행한다. (gradle bootRun으로 실행되지 않음)

## 배포
실행 환경에 따라 `jar`또는 `war`파일로 배포한다.

⚠ 작성 예정