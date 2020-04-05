---
layout: post
title:  "C# Invoke"
date:   2020-01-22 22:34:09 +0900
categories: csharp invoke
---

# Invoke
System.Windows.Forms 객체에서 한정.

## 기본 사항

컨트롤의 핸들이 있는 스레드가 아닌 다른 스레드에서   
컨트롤의 데이터에 접근하게 될 경우, 크로스 스레드 오류가 발생한다.

따라사 원하는 메소드(델리케이트) 및 인자를 컨트롤 핸들의 스레드에서 실행(Invoke) 함으로써  
컨트롤의 데이터에 접근 및 수정이 가능하다.  

**Invoke - 컨트롤의 핸들을 가진 스레드에서 사용자 코드를 대신 실행합니다.**

```
public void StartBtn_Click(object sender, EventArgs e)
{
   Thread myThread = new Thread(new ThreadStart(AccessToControl))
   myThread.Start();
}

public void AccessToControl()
{
   myTxt1.Text = "Set Unsafety."
}
```

이 경우 `InvalidOperationException (컨트롤이 안전하지 않은 스레드에서 액세스 되었습니다)` 오류가 발생한다.

특정 컨트롤에 대해 Invoke가 필요한지의 여부를 판별하고, 필요한 경우 Invoke하여 실행한다.

```
public void MyThreadMethod()
{
    // Invoke가 필요한 상황인지 판별한다.
    if (myTxt1.InvokeRequired)
    {
        // 무명 메서드와 MethodInvoker :: public delegate void MethodInvoker()
        // 이용하여 원하는 함수 호출 / 해당 함수 재호출
        myTxt1.Invoke((MethodInvoker) delegate() { MyThreadMethod(); });
        return;
    }
    // 필요 없는 상황일 경우, 기존 스레드에서 코드를 실행.
    else AccessToControl();
}

public void AccessToControl()
{
    myTxt1.Text = "Set Text."
}
```
