---
layout: post
title:  "gradle 사용하기 - 1"
date:   2020-04-19 00:00:00 +0900
categories: java gradle
---

Gradle에 대해서 알아봅니다.

## Gradle 이란?

`Marven`을 대체한 빌드 도구.  `Grovvy` 기반의 DSL(Domain Specific Language)를 사용한다.

> 참고 :  Android Studio 의 빌드 환경. 코드 작성은 IDE를 이용하지만 빌드 환경은 전적으로 Gradle 에서 처리한다.


## 설치하기

### OS X 

`Homebrew` 에서 설치할 수 있다. 의존성 패키지인 `openjdk` 가 함께 설치된다. (작성일 기준 openjdk 13)

```
brew install gradle
```
설치가 완료되면 다음으로 `gradle` 설치 디렉터리를 확인할 수 있다. IDE에 따라 `GRADLE_HOME` 환경변수를 참조하는 경로가 있으니 추가해준다.

```
 whereis gradle
```

사용하는 쉘의 profile에 다음 줄을 추가한다. `설치 경로.../bin/gradle` 에서 설치 경로를 입력한다.

```
export GRADLE_HOME="GRADLE이 설치된 경로"
```

`gradle` 명령어를 실행하여 `BUILD SUCCESSFUL` 이 출력되면 정상적으로 설치된 것이다.


## 