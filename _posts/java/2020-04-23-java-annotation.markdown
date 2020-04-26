---
title:  "자바  - 어노테이션(annotation)"
date:   2020-04-23 16:00:00 +0900

toc: true
toc_label: "둘러보기"
toc_icon: "columns"

categories: java
tags: java
---

자바의 어노테이션(@ - annotation)에 대해서 알아봅니다.

## 자바에서 어노테이션 이란?

자바 개발을 하다 클래스, 메서드 선언자에 `@Entity`, `@Deprecated` 등의 '@' 이 들어간 코드를 볼 수 있습니다.  이는 자바5 버전부터 추가된 어노테이션으로, 데이터의 유효성 검사,  메타 데이터 추가 등의 기능을 합니다.

**메타 데이터** : 데이터를 위한 데이터를 의미하며, 한 데이터를 위한 설명을 추가합니다.(자신의 정보를 담고 있음)  
예를 들어, JPA로 엔티티를 선언할 때 규격에 맞는 클래스를 선언하고 `java.persistence` 의 `@Entity` 어노테이션을 클래스에 붙임으로써 해당 클래스가 엔티티임을 작성할 수 있습니다.

## 기본 어노테이션

#### 1. @Override
선언한 메서드가 부모 클래스의 메서드를 오버라이딩 했음을 지정한다.  
컴파일 시에 부모 클래스의 해당 메서드의 시그니쳐가 존재하지 않으면 오류가 발생한다.

#### 2. @Deprecated
선언한 메서드 또는 클래스가 더 이상 사용되지 않거나, 미래에 사용되지 않을 것임을 지정한다.  
컴파일 시에 경고를 발생합니다.

#### 3. @SuppressWarnings
선언한 곳에 발생한 컴파일 경고를 무시합니다.

#### 4. @SafeVarargs
제네릭 같은 가변인자의 매개변수를 사용할 때 나타나는 컴파일 경고를 무시합니다.

#### 5. @FunctionalInterface
함수형 인터페이스를 지정합니다.

----

## 어노테이션의 구현

다음은 구현된 어노테이션의 예제입니다.

```
@Target({METHOD, FIELD}) 
@Retention(RUNTIME)
public @interface Column {

    /**
     * (Optional) The name of the column. Defaults to 
     * the property or field name.
     */
    String name() default "";

    ...
}
```

각각 1, 2번째 줄에 쓰인 `@Target` `@Retention` 을 **메타 어노테이션**이라 하며, 이를 이용해 커스텀 어노테이션의 종류를 작성할 수 있습니다.

### 종류

메타 어노테이션의 종류는 다음과 같습니다.

#### @Target

어노테이션이 적용되는 범위를 선언합니다. 예를 들어, `ElementTyped.METHOD`로 선언된 어노테이션은 메서드에만 적용 가능하며 클래스, 필드 등에는 적용할 수 없습니다.  
`@Target` 이 지정되지 않았다면 **throw, instance 생성, casting, 제네릭 표현** 을 제외한 거의 모든 경우에 사용이 가능합니다.

|이름|옵션|
|---|-----|
ElementTyped.PACKAGE|패키지
ElementTyped.TYPE|class, interface, enumeration 지정
ElementTyped.METHOD|method
ElementTyped.CONSTRUCTOR|constructor
ElementTyped.ANNOTATION_TYPE|annotation type
ElementTyped.PARAMETER|parameter
ElementTyped.TYPE_USE|모든 type (throw, instance생성, castring, 제네릭 표현 제외)
ElementTyped.PARAMETER|type variable interface

#### @Retention

자바 컴파일러가 어노테이션을 다루는 방법을 기술합니다.

|이름|옵션|
|---|-----|
RetentionPolicy.SOURCE|컴파일 전까지만 유효하며, 이후에는 사라집니다. 컴파일 시에 경고 및 오류를 확인할 수 있으며, 컴파일 결과에는 영향을 미치지 않습니다. (예: `@Override @Deprecated`)
RetentionPolicy.CLASS|컴파일러가 클래스를 참조할 때까지 유효합니다.
RetentionPolicy.RUNTIME|컴파일되는 자바 파일에 실제 반영됩니다. 대부분의 어노테이션이 여기에 해당됩니다.
----

추가적인 어노테이션의 종류는 다음과 같습니다.

**@Documented** : 해당 어노테이션을 JavaDoc에 포함시킵니다.

**@Inherited** : 상위 어노테이션의 상속을 받을 수 있습니다.

**@Repetable** : 연속적으로 어노테이션을 선언할 수 있게 합니다. 동일한 어노테이션을 여러 번 사용할 경우 array형태로 작성하지 않고 하나씩 각각 작성할 수 있습니다.