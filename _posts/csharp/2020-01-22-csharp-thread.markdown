---
title:  "C# Thread"
date:   2020-01-22 22:34:09 +0900

categories: csharp
tags: csharp thread

toc: true
toc_label: "둘러보기"
toc_icon: "columns"
---

# 스레드
`System.Threading.Thread`  
추가적인 스레드에서 사용자 코드를 실행할 수 있도록 합니다.

## 기본 사항
.NET Framework에서의 스레드는 sealed 클래스로 구현되어, 다른 클래스에서 상속하여 사용할 수 없습니다.  
임의적으로 상속하여 구현하고자 할 경우, [Object Composition](https://stackoverflow.com/questions/8123461/unable-to-inherit-from-a-thread-class-in-c-sharp) 기법을 이용하여 구현할 수 있습니다.

```
using System.Threading;

abstract class BaseThread
{
    private Thread _thread;
}

```

----

## 생성
```
public Thread(ThreadStart start, [int maxStackSize: 0]);
public Thread(ParameterizedThreadStart start, [int maxStackSize: 0]);
```

**ThreadStart (메소드의 실행 인자가 없는 경우)**  
인자값을 받지 않는 시작 함수 대리자
```
public delegate void ThreadStart();
```


**ParameterizedThreadStart (메소드에 실행 인자를 전달하는 경우)**  
인자값을 받는 시작 함수 대리자
```
public delegate void ParameterizedThreadStart(object obj);

public sealed class Thread : ...
{
  public void Start();
  public void Start(object parameter); // ParameterizedThreadStart 대응
}

Thread myThread = new Thread(new ParameterizedThreadStart(MyThreadMethod))

List<object> parameter = new List<object>();
parameter.Add("message");
parameter.Add(1234);
myThread.Start(parameter);

public void MyThreadMethod(object obj)
{
    List<object> parameter = (List<object>)obj;
    string message = (string)parameter[0];
    int uid = (int)parameter[1];
}


```



**maxStackSize**  
응용 프로그램의 기본 스택 크기를 사용할 경우 0, 그렇지 않은 경우 사용자 정의 크기를 입력. 신뢰할 수 있는 코드에서 기본 스택 코드보다 큰 경우 무시됩니다.

----

## 관리
