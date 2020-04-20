---
layout: post
title:  "자바 살펴보기 - 1 : 버전, 배포판, JDK"
date:   2020-04-11 20:00:00 +0900
categories: java
---

자바를 잘 모르는 사람이 자바에 대해서 알아보았습니다. 1편.

## Java란?

> 자바는 썬 마이크로시스템즈의 제임스 고슬링(James Gosling)과 다른 연구원들이 개발한 객체 지향적 프로그래밍 언어이다.  
출처 :  [위키백과 - 자바(프로그래밍 언어)](https://ko.wikipedia.org/wiki/%EC%9E%90%EB%B0%94_(%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D_%EC%96%B8%EC%96%B4))


## 버전별 정보와 주요 특징

자바 1.0 - 1.0.2 의 정식 stable 버전은 1996년에 출시되어, 지속적인 개발이 이루어지고 있다.  
자바 버전(클래스 파일 버전) 과 자바 플랫폼 버전은 다음과 같다.

|자바 플랫폼 버전 (major)|minor|클래스 버전|주요사항|
|---|---|-----|-----|
|1.0 - 1.1|3|45|
|1.2|3|46|
|1.3|0|47|
|1.4|0|48|
|5|0|49|
|6|0|50|
|7|0|51|
|8|0|52|
|9|0|53|
|10|0|54|
|11|0|55|
|12|0|56|
|13|0|57|
|14|0|58|

**major version** : 새로운 플랫폼의 출시, 이전 버전과의 호환성 단절 (예: Java 10으로 컴파일한 바이너리는 Java9 에서 실행 불가)  
**minor version** : 

💡 10 미만의 자바 플랫폼은 `1.x` 로 표기하기도 한다.  
💡 클래스 버전은 자바 파일을 컴파일하는 과정에서 지정할 수 있으며, 클래스 버전보다 더 낮은 자바 플랫폼은 해당 클래스 파일을 실행할 수 없다. `unsupported class file major version` 이 발생하며, 이와 관련한 내용은 추후 다룬다.

[Java API to find out the JDK Version a class file is compiled for?](https://stackoverflow.com/questions/1293308/java-api-to-find-out-the-jdk-version-a-class-file-is-compiled-for)

설치된 자바의 버전은 다음 방법으로 확인한다.

```
java --version
```

## 배포판

`OracleJDK` - 오라클 자바의 배포판은 다음과 같다.

|이름|-|-|
|---|-----|-----|
|Java SE|Standard Edition|일반 제품
|Java EE|Enterprise Edition|기업용 서버 제품
|Java ME|Mobile Edition|임베디드 모바일 제품
|Jave FX||그래픽, 멀티미디어 기능을 지원하는 리치 클라이언트 제작용

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

자바는 무료이지만, 애플리케이션을 제작하고, 배포(판매) 및 서비스 운영을 하기 위해서는 자신의 사용하고 있는 JDK의 배포판 결정에 주의가 필요하다. `OracleJDK` 는 유료이므로,  사용하기 전 반드시 약관을 확인할 필요가 있다.

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

자바의 스펙을 재정하고, 이를 토대로 구현하여 오픈소스 형태로 배포하는 자바가 바로 `OpenJDK` 이다. 추가적인 기능 없이 스펙 그대로의 자바를 만든 것이며, 이는 전적으로 오라클이 담당하고 있다. (엄밀히 말하면, 자바 스펙을 검토, 재정하는 기관이 있지만 결정권에 오라클이 큰 영향을 미친다고 한다)

이 `OpenJDK`에 오라클이 배포판 별로 추가적인 기능을 더하여 유로 라이센스로 사용하도록 하고, 기술 지원 등을 추가한 것이 바로 `OracleJDK` 이다. 

따라서 `OracleJDK`에서 운영중인 응용 프로그램이나 프레임워크를 `OpenJDK` 환경으로 전환하고자 한다면 구현되지 않은 기능이 있을 수 있으니, 사전에 호환영 문제를 필이 확인해보아야 한다.

오라클사가 기능을 추가하여 `OracleJDK` 를 만든 것처럼, 특정 환경에서의 실행을 지원하거나 다양한 기능이 추가된 자바 스펙을 준수한 JVM과 JDK가 존재한다.  
[무료 / 상용 자바 JVM 리스트](https://en.wikipedia.org/wiki/List_of_Java_virtual_machines)  

OpenJDK 자바와 OracleJDK 자바는 각각 이곳에서 확인할 수 있다.
|이름|-|
|---|-----|
|OpenJDK|https://openjdk.java.net/
|OracleJVM|https://java.com/ko/download/
|OracleJDK|https://www.oracle.com/java/technologies/javase-downloads.html
