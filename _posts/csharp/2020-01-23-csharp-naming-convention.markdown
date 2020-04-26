---
title:  "C# Naming convention"
date:   2020-01-22 22:34:09 +0900

toc: true
toc_label: "둘러보기"
toc_icon: "columns"


categories: csharp
tags: csharp naming-convention
---

### MSDN 공식 문서의 권고안을 이용하되, 일부 예외사항은 별도로 정해서 사용한다.

헝가리안 표기법은 사용하지 않는다. 변수, 각 객체의 "형식을 유추할 수 있는" 명칭도 사용하지 않는다.

> 헝가리안 표기법  
> 80년대 경 IDE가 부실한 환경에서, 변수 및 필드명에 데이터의 형식을 유추할 수 있도록 변수명에
접두어를 붙임. 멤머변수의 경우에도 별도의 접두어가 존재함.

> 카멜 표기법 (camelCase)  
> 각 단어의 첫문자를 대문자로 표기하고 붙여쓰되, 첫 문자는 소문자로 표기

> 파스칼 표기법 (PascalCase)  
> 각 단어의 첫문자를 대문자료 표기하고 붙여쓰며, 첫 문자도 대문자로 표기

----

 

[Microsoft Naming Guidelines](https://docs.microsoft.com/en-us/previous-versions/dotnet/netframework-1.1/xzf533w0\(v=vs.71\))

## 공통 사항
- 모든 이름에는 영숫자가 아닌 문제를 사용하지 않음.
- 기본 식별자 / 키워드와 충돌하는 명칭을 사용하지 않음.
- 약어나 축약어를 사용하지 않음. `ex) GetWin -> GetWindows`
- 서술어 + 명사 형태의 이름을 사용한다. `ex) TbxAmount -> AmountTbx`
- 되도록이면 형태를 유추할 수 있는 네이밍을 사용하지 않는다.
> 프레임워크 기본 정의객체인 MethodInvoker, ParameterizedStart 등이 Delegate 형임에도 불구하고, 이름에서 형식을 유추할 수 없다.

### 클래스, 구조체, 형식(custom type)
- 파스칼 표기법 사용 (PascalCase)

### 클래스, 구조체 내부
- 매서드, 속성: 파스칼 표기법 사용 (PascalCase)
- 필드: 카멜 표기법 사용 (camelCase)


### 인스턴스, 변수
- 카멜 표기법 사용 (camelCase)

### 열거형
- 열거형 자체는 파스칼 표기법 및 복수형 사용. 내부 필드는 파스칼 표기법 사용.

----

## 추가 네이밍 규칙


### 커스텀 라이브러리 네임스페이스 명


### Windows.Forms.Control 객체
다음 명칭을 접미사로 사용한다.

|컨트롤|접미사|비고|
|------|---|---|
|Form|Form|윈도우 폼에는 이름 그대로 사용 (예외)|
|Button|btn||
|Timer|tmr||
|Label|lbl||
|TextBox|tbx||
|ProgressBar|pgb||
|BackgroundWorker|bgw||
|ListView|lsv||
|DateTimePicker|dtp||

### Thread (ThreadStart, ParameterizedStart) 시작 함수 스레드


### 윈도우 폼 이벤트 Callback Method


### Event 객체의 Callback Method
`.net framework` 에서 사용되고 있는 명명에 따라,  
`On ...` 접두어를 파스칼 표기법을 이용하여 표기한다.

### EventArgs 를 상속한 클래스의 명칭
`... EvtArgs` 접미어를 사용하여 표기한다.

### 직렬화(Serialize), 역직렬화(Deserialize) 객체
**각 객체의 필드마다 규격화된 문법 (XPath 등)을 작성하여 삽입하기 어려움. (기능객체와 직렬화클래스를 분리작성)**  
**세부 스펙을 지정하지 않았으므로 보류**  
특정 구조체, 클래스 명이 다른 네임스페이스의 객체와 겹칠 수 있으나, 별도의 접두어는 기본적으로 붙이지
않고 명명하는 것을 원칙으로 한다.


... TODO -> 추가적인 라이브러리 작성 등의 소요가 발생한다면 별도로 표기한다.
