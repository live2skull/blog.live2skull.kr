---
layout: post
title:  "C# Delegate"
date:   2020-01-22 22:34:09 +0900
categories: csharp delegate
---

# 대리자

## 정의
특정 메소드(반환 형식 및 매개변수 목록)에 대한 메소드를 나타낼 수 있는 형식입니다.  
C++ 등의 저수준 언어에서, 함수 포인터와 같은 개념으로 이해할 수 있습니다.

## 사용
특정 이름(대리자 타입 이름)의 변수를 만들 때 다음고 같이 사용할 수 있다.  
인스턴스화된 대리자에 `+=` , `-=` 연산자를 사용함으로써 연속된 대리자 생성이 가능합니다.  

----

#### 대리자 타입의 생성
```
public delegate int MyDelegateType(int var1, string var2)
public int MyMethod(int var1, string var2);
```

#### 함수를 직접 지정
```
MyDelegateType myDel1 = MyMethod;
```

#### 클래스 생성과 유사한 방법으로 지정 (생성자에 대항 함수 지정으로 스레드 생성 - ThreadStart)
```
MyDelegateType myDel2 = new MyDelegateType(myMethod);
```

#### 익명 함수
```
MethodInvoker method = (MethodInvoker) delegate(int arg1, int arg2) { ...; };
```

----

## 대리자 사용 예시

### 프레임워크 기본 개체
`MethodInvoker` : System.Windows.Forms   
`public delegate void MethodInvoker()`    
인자가 없는 단일 함수 대리자.

### 인자값 전달
#### System.Windows.Forms.Control을 상속한 GUI 클래스에서의 Invoke  
```
public object Invoke(Delegate method, params object[] args);
```



#### ParameterizedStart으로 생성된 스레드의 인자값 전달.
ParameterizedStart가 사전 정의된 대리자로써, object 형 하나만을 받는다.
자료형이 동일 또는 서로 다른 변수들을 받을 경우 object[] 또는 List\<object\>로 대응한다.

----

## MulticastDelegate (연결된 대리자 체인)

...
