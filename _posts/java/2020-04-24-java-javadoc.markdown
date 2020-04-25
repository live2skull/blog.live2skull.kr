---
layout: post
title:  "Javadoc 작성하기"
date:   2020-04-24 15:00:00 +0900
categories: java
---

자바로 작성한 코드의 문서 작성을 해 봅니다.

## Javadoc 이란?

코드를 작성하다 보면 유지보수, 배포 등 다양한 상황으로 인해 코드의 문서 작성이 필요한 경우가 있습니다. 하지만 작성한 코드의 클래스, 필드, 메서드에 대해 개발이 완료된 후 일일이 작성하는 것은 번거로울 뿐더러, 코드의 규모가 크다면 더 복잡한 일이 될 것입니다. 

이를 지원하기 위해서 자바에서는 `Javadoc` 을 사용할 수 있으며, 문서화할 클래스, 필드, 메서드, 어노테이터, 인터페이스 등에 주석 및 어노테이션으로 문서를 작성하고, HTML등 다양한 포맷으로 export 하는 기능을 제공합니다.

`Javadoc`의 장점은 다음과 같습니다.
- 표준에 맞춘 주석 작성으로, 구독자 간의 혼동을 최소화 할 수 있습니다.
- 코드에 문서를 포함시킬 수 있어 개발과 동시에 쉬운 문서화가 가능합니다.
- 다양한 지원 도구로 원하는 디자인 / 타입의 문서를 쉽게 만들 수 있습니다.

`Javadoc`은 자바 문서 작성의 표준으로 문서화 된 코드 대부분에서 사용하고 있으며, `Javadoc`으로 작성된 대표적인 문서는 [오라클사의 JavaSE  documentation](https://docs.oracle.com/javase/8/docs/api/) 이 있습니다.

## 주석으로 문서 작성하기

`Javadoc` 은 multi-line 주석으로 작성하며, 간단한 예시는 다음과 같습니다.  
대부분의 IDE에서는 주석의 양식을 자동으로 만들어 줍니다. Javadoc 시작 문자열 /** 을 작성후 줄바꿈하면 주석의 양식이 생성됩니다. (intelij IDEA, eclipse 등 지원)



```
package kr.live2skull.demo;

/**
 * 원격 서버와 HTTP 통신 기능을 제공하는 구현체입니다.
 *
 * @author live2skull
 * @since 1.1
 */
public class HttpClient {

    // 코드 구현 ...

}
```

- **/\*\*** 문자열로 시작합니다. (multi-line 주석 **/\*** 과는 다릅니다!)
- 각 클래스, 메서드, 필드, 어노테이션 등 설명하고자 하는 구현체 위에 작성합니다.
- 해당 구현체의 설명 작성과, 각 특성 지정을 위해 '@'로 시작하는 **태그** 로 구성되어 있습니다.
- 설명 작성은 HTML문서로 작성할 수 도 있습니다. 
 
공통적으로 사용되는 태그는 다음과 같습니다.

|이름|설명|
|-----|-------|
|@version|패키지 등 구현제 버전
|@author|코드 작성자
|@deprecated|해당 구현체의 삭제, 지원 중단을 예고함
|@since|해당 구현체가 추가된 버전
|@see|문서가 참조할 다른 클래스 / 메서드 / 외부 링크
|@link|**@see** 와 동일
|@exception|\[ExceptionClass Description\] throw 할 수 있는 예외 정의. **ExceptionClass** 알파벳 순으로 작성.
|@throws|**@exception** 과 동일
|@param|\[ParamName Description\] 메서드, 생성자 인자값 설명
|@return|반환값 설명
|@serial|**Serializeable** 인터페이스에 사용
|@serialData|**writeObject writeExternal** 메소드로 작성된 추가적 데이터를 설명
|@serialField|**serialPersistnetFields** 배열의 모든 필드에 사용

다른 객체를 참조하는 태그(@see, @link)등 의 지정 문법은 다음과 같습니다.

|문법|설명|
|-----|------|
package.Class#field|패키지의 클래스 - 필드 지정
package.Class#member(Type type, ...)|패키지의 클래스 - 메서드 지정 
package.Class#constructor(Type type, ...)|패키지의 클래스 - 생성자 지정
\<a href="URL"\>label\<\/a\>|외부 링크와 라벨 지정

패키지 명은 작성하는 코드가 대상 클래스를 import 했다면 생략할 수 있습니다.  
대상 작성 후 표시할 문자열(라벨) 을 다음과 같이 작성할 수 있습니다. 
```
@link kr.live2skull.demo.HttpClient "HttpClient 참고하기"
```

문서 설명에서 **@link @see** 태그를 중괄호로 표기하여  참조할 다른 객체를 지정할 수 있습니다. 
```
/**
* ... 문서 설명
* @deprecated 이 클래스는 1.3 버전 이후로 지원되지 않을 예정입니다. {@link WebParser} 를 사용하세요.
*/
```

----

## 작성 예시

구현체별로 `Javadoc`을 작성한 예제를 살펴보겠습니다.

### 패키지

패키지의 `Javadoc` 작성은 패키지 디렉터리 루트에 `package-info.java` 파일에 작성합니다. 이 파일은 문서만 작성하며, 다른 기능은 구현하지 않습니다.

```
/**
* clms 서버와의 인증, 컨텐츠 관리, 다운로드 기능을 제공하는 클라이언트입니다.
* @author live2skull
* @version 1.2
* @since 1.0
*/
// package-info.java 에도 마찬가지로 패키지를 명시합니다.
package kr.live2skull.clms;
// 다른 기능은 구현하지 않습니다.
```

### 클래스
```
package kr.live2skull.demo;

/**
 * 음악 엔티티입니다.  
 *
 * @author live2skull
 * @since 1.0
 */
@Entity
@Getter
public class Songs {
    // 코드 구현 ...
}
```

### 필드
```
package kr.live2skull.demo;

@Entity
@Getter
public class Songs {
    /**
    * 고유 ID 값입니다. [PK]
    */
    @Id
    @GeneratedValue
    private Long id; 

    /**
    * 음악 제목입니다. 값은 null 일 수 없습니다.
    */
    @Column(nullable=false)
    private String title;
}
```

### 메서드
```
public class ClmsClient {
    /**
    *
    * @throws AuthorizationException authKey가 contentId와 일치하지 않습니다.
    * @throws ContentNotExistException contentId에 해당하는 컨텐츠가 존재하지 않습니다.
    *
    * @param contentId 컨텐츠 ID입니다.
    * @param authKey 컨텐츠 비밀번호입니다. 지정하지 않을 경우 null 입니다.
    * @return 컨텐츠가 위치한 URL입니다.
    */
    public URL resolveDownloadURL(Long contentId, String authKey) {
        // ... 
        return new URL(response.strip());
    }
}
```

### 어노테이션

```
/**
* 인증에 사용할 필드를 지정합니다.
*/
@Target({FIELD}) 
@Retention(RUNTIME)
public @interface AuthorizeData {
    /**
     * 데이터의 키 값입니다.
     */
    String name();
}
```

## HTML문서 생성하기

`Javadoc`을 소개하며 오라클사의 JavaSE documentation을 소개하였습니다. 이와 같이 코드상의 문서 뿐 아니라, HTML문서를 생성하여 documentation 페이지를 제작할 수 있습니다.

자바 설치 시 (`openjdk oraclejdk` 기준) 포함된 `javadoc`  명령어로 HTML문서를 생성할 수 있습니다. 

#### 패키지 문서 생성
문서를 생성하고자 하는 패키지를 지정합니다. 이때 작업 디렉터리 또는 `-sourcepath` 로 패키지 디렉터리가 있는 부모 디렉터리를 지정합니다.
```
javadoc com.live2skull.demo -sourcepath %userprofile%\IdeaProjects\demo\src\main\java
```

#### 단일 java 파일 문서 생성
마찬가지로 코드의 경로를 지정하거나, 작업 디렉터리를 대상 코드로 옮겨야 합니다.
```
javadoc MyFirstCode.java
```

----

## 유용한 글
게시물로 잘 정리하신 분들의 링크입니다. 생각을 정리하는데 많은 도움이 되었습니다.

[araikuma님- \[Javadoc\] @see 태그](https://araikuma.tistory.com/658  )  
[lesstif님 - 자바독 치트 시트](https://www.lesstif.com/java/javadoc-cheat-sheet-26083721.html)