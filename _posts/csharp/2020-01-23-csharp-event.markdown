---
title:  "C# Event"
date:   2020-01-22 22:34:09 +0900

toc: true
toc_label: "둘러보기"
toc_icon: "columns"


categories: csharp
categories: csharp event
---

# 이벤트
게시자 클래스에서 이벤트를 선언하는 데 사용됩니다.

### 프레임워크에서의 기본 정의
이벤트 정의를 위해 사용되는 대리자  

```
using System.Runtime.InteropServices;

public delegate void EventHandler(object sender, EventArgs e);
public delegate void EventHandler<TEventArgs>(object sender, TEventArgs e);

public class EventArgs
{
    // 빈 EventArgs 생성자
    public static readonly EventArgs Empty;

    public EventArgs();
}
```

### 기본 사용
프레임워크 기준 - EventHandler, EventHandler\<TEventArgs\>를 제외한 다른 대리자를 사용하지 않음.
```
// 이벤트 발행자 정의
//           대리자         이벤트 명
public event EventHandler MyEvent;

// 이벤트 발행
MyEvent(this, new EventArgs()); // EventArgs: null로 발행해도 무관함

// 이벤트 구독
public class Test
{
    public void OnEventRaised(object sender, EventArgs e)
    {
        ...
    }

    public void Test()
    {
        // 구독하고자 하는 이벤트의 메소드 시그니쳐와 콜백이 일차하여야 한다.
        // 메소드가 아닌 대리자를 연결할 경우, 해당 대리자는 이벤트의 대리자와 동일한 객체여야 한다.
        // 대리자의 경우 시그니쳐만 동일한 경우 사용할 수 없다.
        MyEvent += this.OnEventRaised;
    }
}
```
