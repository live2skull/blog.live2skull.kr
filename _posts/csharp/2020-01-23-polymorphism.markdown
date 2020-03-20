---
layout: post
title:  "C# Polymorphism"
date:   2020-01-22 22:34:09 +0900
categories: csharp abstract interface
---

# 다형성
파생 클래스를 부모 클래스 형태로 사용하는 경우입니다.


### virtual
매서드의 본문을 작성하여야 함.  
상속된 파생 클래스에서 override 키워드로 재작성하며, 파생 클래스를 부모 클래스 형태(다형성)으로 사용할 때  
부모 클래스에서 virtual 선언 후 자식 클래스에서 override하여 재작성한 경우 자식 클래스의 매소드가 실행됩니다.  


### abstract
매서드의 본문을 작성할 수 없으며, 시그니쳐만 생성할 수 있음. 상속된 파생 클래스에서 반드시 재정의하여야 합니다.  
재정의하는 매서드는 반드시 override 되어야 함.


### new
부모 클래스에서 정의된 일반 메소드를 재정의하려면 `new` 메소드가 필요. 그렇지 않으면 경고가 발생합니다.  


### override
`virtual`, `abstract`로 정의된 매서드는 파생 클래스에서 재정의시 반드시 override 키워드가 사용되어야 합니다.


# 추상 클래스와 인터페이스
## 추상 클래스 (abstract class)
C#은 다중 클래스 상속을 지원하지 않습니다. 특정 기능을 구현하나, 파생 클래스로 반드시 확장하여야 하고,
공통된 구현이 필요한 개체에서 적합합니다.  
이는 다형성 특성도 구현할 수 있습니다.
```
public abstract class Parser
{
   public abstract List<string, object> Serialize();

}

public class NaverParser: Parser
{
   public override List<string, object> Serialize()
   {
      // virtual 선언인 경우 base method 접근. abstract 선언이라면 코드 자체가 존재하지 않는다.
      base.Serialize();
   }
}
```


## 인터페이스 (interface)
#### 특정 동작 구현이 필요한 경우 (ex: IEnumerable, IQueryable)
C#은 다중 클래스 상속을 지원하지 않으나, 인터페이스는 다중 상속이 가능합니다. 특정 기능을 지원하는 클래스를 작성할 경우, 공통된 메소드를 인터페이스를 이용해 관리합니다.
`ex) IEnumerable, IQueryable`

#### 특정 형식으로 다양한 다른 형식의 인스턴스에 접근할 경우
특정한 클래스에서 파생되지 않았으나, 동일한 형태로 액세스가 필요한 경우에 적용합니다.
```
public class IDBDriver
{
  public QueryResult query();
  public bool Fetch(); ..
}

public class MySQLClient: IDBDriver;
public class MongodbClient: IDBDriver;
```
