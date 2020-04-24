---
layout: post
title:  "자바 - Lombok"
date:   2020-04-24 09:00:00 +0900
categories: java lombok
---

Lombok 프레임워크로 소스코드 경량화하기.

## Lombok 이란?
자바에서 일반 클래스나 엔티티 오브젝트(DTO, VO, Domain)를 작성할 때, 멤버필드에 대한 접근자, toString, 빌더 등 필드나 클래스에 작성하는 내용을 어노테이터로 간편하게 생성할 수 있게끔 하는 프레임워크입니다.

단. 편리한 만큼 잘못 사용하면 예상치 못한 동작을 할 수 있는 경우가 있습니다. `Lombok`에서 지원하는 어노테이션과, 개인적으로 생각하는 사용 규칙, 주의사항에 대해 알아보겠습니다.

💡 프레임워크의 기능이 굉장히 많습니다. 다루지 못한 부분은 틈틈히 추가할 예정입니다.


## 지원하는 어노테이터

### 생성자

지정한 클래스의 생성자를 작성해 줍니다. 모든 생성자 어노테이터에는 접근 제한자를 설정할 수 있습니다.

|이름|설명|
|---|-----|
AccessLevel.MODULE|모듈 단위의 접근이 가능합니다.
AccessLevel.PACKAGE|package 한정자
AccessLevel.PUBLIC|public 한정자
AccessLevel.PRIVATE|private 한정자
AccessLevel.PROTECTED|protected 한정자
AccessLevel.NONE|기본값 사용

**@NoArgsConstructor**  
매개변수가 없는 생성자를 만듭니다. 가장 기본적인 사용입니다.

**@AllArgsConstructor**  
모든 필드를 매개변수로 받는 생성자를 만듭니다.

**@RequiredArgsConstructor**  
지정한 필드만 매개변수로 받는 생성자를 만듭니다. 생성자에 필요한 필드를 **@NonNull** 어노테이션으로 지정합니다.

```
@RequiredArgsConstructor(access=AccessLevel.PUBLIC)
package com.live2skull.demo;
import lombok.*;

public class Songs {
    private Long id;
    @NonNull private String title;
}
```

----

### 빌드 패턴
앞서 **@AllArgsConstructor**는 매개변수의 순서 할당 문제로 사용하지 않는 것을 권장했습니다. 이에 대응하여 생성자 매개변수를 지정할 수 있는 빌드 패턴을 사용할 수 있습니다.

빌드 메소드로 사용될 메소드를 작성하고, `@Builder` 어노테이터를 적용합니다.

```
package com.live2skull.demo;
import lombok.*;

// new() 생성자로 인스턴스를 사용하지 못하게 합니다. 필수사항은 아닙니다.
@NoArgsConstructor(access=AccessLevel.PROTECTED)
public class Songs {
    private Long id;
    private String title;

    @Builder
    public Songs(String title)
    {
        // 생성자처럼 작성하고 새로운 객체의 return 이 필요 없음
        // 아래 코드를 실행한 새로운 객체가 반환됩니다.
        this.title = title;
    }
}
...
// 사용 예시
Songs s = Songs.builder()
                .title("안녕하시죠?")
                .build();
```

----

### 접근자 및 기타

**@Getter**   
필드의 읽기 접근자를 작성합니다. 클래스에 선언하면 모든 필드에 대해 생성자를 만들며, 필드에 생성하면 해당 필드에만 생성됩니다.

**@Setter**  
필드의 쓰기 접근자를 작성하며, 읽기 접근자와 동일합니다.

**@ToString**  
`toString()` 메서드를 작성합니다. 각 필드 자료형의 `toString()` 메서드로 변환된 값을 가져오며, 생성자 형태로 만듭니다. `exclude` 옵션으로 제외할 필드를 지정할 수 있습니다.

부모 클래스의 `toString()`을 사용 - ```@ToString(callSuper=true)```  
하나의 필드만을 `toString()` 에서 제외 - ```@ToString(exclude="id")```   
여러개의 필드를 `toString()` 에서 제외 - ```@ToString(exclude={"id", "title"})```

```
package com.live2skull.demo;
import lombok.*;

@ToString
public class Songs {
    private Long id;
    private String title;
}

// 다음과 같이 출력
// Songs(id=1234, title="안녕하시죠?")
```

**@EqualsAndHashCode**  
`equals()` 와 `hashcode()` 메서드를 생성합니다. 



## 사용 규칙 (또는 주의하거나 금지하는 규칙)

### 1. @AllArgsConstructor, @RequiredArgsConstructor를 가급적 사용하지 않습니다.

생성자 매개변수의 순서가 필드의 작성 순서가 아닌 컴파일러의 특정 규칙에 따라 결정되기 때문에, 사용자가 생성자를 사용하며 실수하기 쉽습니다. 특히, 같은 자료형인 필드를 두가지 이상 사용한다면 값의 순서가 바뀌어도 컴파일 / 런타임 중에 문제를 바로 파악할 수 없어 버그 발생의 위험이 있습니다.

- 실수를 하기 쉬운 `@AllArgsConstructor, @RequiredArgsConstructor` 대신 `@Builder` 어노테이션을 사용합니다.
- 가급적이면 생성자를 직접 작성하므로써 매개변수 등에 의한 코드의 오류를 최소화합니다.


### 2. @EqualsAndHashCode를 함부로 사용하지 않습니다.
`@EqualsAndHashCode` 어노테이터를 사용하면 복잡한 절차 없이 `equals()` `hashcode()`메서드를 사용할 수 있지만, 기본값으로 모든 필드에 대해 메서드를 작성하므로, 다음과 같은 문제가 발생할 수 있습니다.

다음은 한 객체의 예제입니다.

```
@Entity
@Getter
@EqualsAndHashCode
public class Users {
    
    private Long id;
    private String name;
    
    @Setter
    private Long accountBalance;

    // 생성자 생략 ...
}

```

객체의 통장 잔고(accountBalance)는 접근자를 주어 변경이 가능한 **Mutable** 필드이고, 이름과 고유 아이디는 접근만 가능하므로써 수정 불가능한 **Immutable** 필드입니다. 만약 **Mutable** 필드가 `equals()`, `hashcode()` 에 사용한다면 다음과 같이 동작할 수 있습니다.

```
Users user = new Users(1, "live2skull", 500);
 
Set<Users> users = new HashSet<>();
orders.add(user);

System.out.println("before change balance : " + users.contains(user)); // true 

user.setAccountBalance(1000);

System.out.println("after change balace : " + users.contains(user)); // false
```
객체를 구분하기 위해 사용한 불변 필드는 id, name 뿐이었지만, 모든 필드가 참조되어 accountBalance가 변경된 객체가 서로 다른 객체로 인식되었습니다. (hashcode 값이 달라짐)

따라서 본 어노테이션을 사용할 때는 다음 규칙을 지키는 것이 좋습니다.
- 필드의 가변, 불변 여부 명확히 합니다.
- 사용한다면, `exclude` (해당 필드를 제외한 나머지 필드만을 사용) 또는 `of` (지정한 필드만을 사용)로 가변 필드를 지정합니다. 문법은 `ToString`의 `exclude` 필드 지정과 동일합니다.





## 유용한 글 
게시물로 잘 정리하신 분들의 링크입니다. 생각을 정리하는 데 많은 도움이 되었습니다.

[권남 - Lombok 사용시 주의점(Pitfall)](https://kwonnam.pe.kr/wiki/java/lombok/pitfall)  
[권남 - Java equals & hashCode](https://kwonnam.pe.kr/wiki/java/equals_hashcode)