---
layout: post
title:  "자바 살펴보기"
date:   2020-04-11 20:00:00 +0900
categories: java
---

자바를 잘 모르는 사람이 자바에 대해서 알아보았습니다.

## Java란?

> 자바는 썬 마이크로시스템즈의 제임스 고슬링(James Gosling)과 다른 연구원들이 개발한 객체 지향적 프로그래밍 언어이다.  
출처 :  [위키백과 - 자바(프로그래밍 언어)](https://ko.wikipedia.org/wiki/%EC%9E%90%EB%B0%94_(%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D_%EC%96%B8%EC%96%B4))



## 버전별 비교와 주요 특징


## 배포판

|이름|-|
|---|-----|
|Java SE|
|Java EE
|Java ME
|Jave FX

`JVM, JDK` 는 실행 환경, 개발 환경으로 나뉘며, 배포판은 기능별로 정리한 것으로 보면 된다.

## Java 구성 요소

|이름|-|
|---|-----|
|JVM|컴파일된 자바 바이트코드를 실행 (Hotspot 이라도고 함)
|JDK|.java 파일을 컴파일하기 위한 SDK. (javac 로 실행하는 컴파일러)

`JVM`은 `JRE - Java Runtime Environment`로 일반적인 자바 설치시 설치되는 `java` 프로그램이 바로 이것이다.  
 `JRE`로는 컴파일된 자바 프로그램의 실행만 가능하고, 자바 소스코드 `.java` 를 `.class, .jar` 등의 자바 바이트코드로 컴파일하기 위해서는 `JDK - Java Development Kit`가 필요하다.

## OracleJDK와 OpenJDK

[Oracle JDK와 OpenJDK의 차이 정리 - 지단로보트 님 블로그](https://jsonobject.tistory.com/395)

`Java` 언어는 무료이며, 

자바로 애플리케이션을 제작하고, 배포(판매) 및 서비스 운영을 하기 위해서는 자신의 사용하고 있는 JDK의 배포판을 신중히 결정해야 한다. `OracleJDK` 는 유료이기 때문에, 사용하기 전 반드시 약관을 검토하여야 한다.

[오라클사의 Java 라이센스 관련 정리](https://www.oracle.com/technetwork/java/javase/overview/oracle-jdk-faqs.html)

자신이 사용하고 있는 자바의 JDK 종류를 확인하려면 다음과 같이 실행한다.
```
java --version
```

`OracleJDK` 배포판
```
java 13.0.2 2020-01-14
Java(TM) SE Runtime Environment (build 13.0.2+8)
Java HotSpot(TM) 64-Bit Server VM (build 13.0.2+8, mixed mode, sharing)
```

`OpenJDK` 배포판
```
openjdk version "13" 2019-09-17
OpenJDK Runtime Environment (build 13+33)
OpenJDK 64-Bit Server VM (build 13+33, mixed mode, sharing)
```
