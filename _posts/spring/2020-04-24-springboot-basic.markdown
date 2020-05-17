---
title:  "Spring Boot 기본 - 1"
date:   2020-04-24 13:00:00 +0900

toc: true
toc_label: "둘러보기"
toc_icon: "columns"

categories: java spring-boot
tags: java spring-boot
---

Spring Boot를 이용한 간단한 웹 서비스 작성 - 기본 구성 알아보기

## Spring Boot 프레임워크 구성 요소


## Spring Boot 사용자 프로젝트 구성 요소

Spring Boot 프레임워크를 이용한 사용자 프로젝트에서 작성하는 구성 요소입니다 각 구성요소는 subpackage로 나누어 작성하게 됩니다.

|구성요소|설명|
|---------|-------|
|controller|URL요청 맵핑
|domain|JPA Entity 어노테이션 클래스. ORM 연동 객체
|dto|RestAPI에서 사용자 데이터를 Entity 로 변환합니다.
|repository|JPA Repository 인터페이스.  ORM CRUD 구현체.
|filter|
|service|interface와 impl 클래스 구현체. 도메인이 수행하는 기능을 지정한다. (컨트롤러에서 여러개의 서비스 이용)
|util|
|enums|JPA등에 적용할 Enum 객체


### 서비스

사용자가 여러 도메인 등 다양하게 사용되는 작업을 통합해 작성합니다.

#### Service (interface)

#### ServiceImpl (Class)

서비스 인터페이스를 실제 구현합니다.