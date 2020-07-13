---
title:  "C# - 엑셀 파일 저장하기"
date:   2020-07-09 11:50:00 +0900

toc: true
toc_label: "둘러보기"
toc_icon: "columns"

categories:
    - csharp
    - excel

tags:
    - csharp
    - excel
    - data-mining
---

# C# 에서 엑셀파일 저장하기

`EPPlus` nuget 패키지의 `OfficeOpenXml` 라이브러리로 C#에서 엑셀 파일을 저장할 수 있습니다.

## 파일 유무 체크 및 열기

파일에 이어서 작성하는 경우가 아니라면, 기존의 파일이 존재하는지 확인하고 있다면 제거합니다.

```
FileInfo excelFile = new FileInfo(fileName);
// 지정된 파일이 이미 있을경우 삭제한다.
if (excelFile.Exists) excelFile.Delete();
```

## 엑셀 파일 생성

라이센스 모드를 설정하고, 새로운 파일을 엽니다.

```
ExcelPackage.LicenseContext = OfficeOpenXml.LicenseContext.NonCommercial;

using (ExcelPackage excel = new ExcelPackage())
{
    // 이곳에 작성 코드를 입력합니다.
}
```

## 작업지(Worksheet) 생성

새로운 시트를 만들고, `ExcelWorksheet` 인스턴스를 생성합니다.  
시트 인스턴스에서 데이터 추가 및 컬럼, 열에 대한 서식 지정 등을 할 수 있습니다.

```
string sheetName = "시트명"

// 시트를 생성하면 해당 시트의 인스턴스를 받습니다.
ExcelWorksheet sheet = excel.Workbook.Worksheets.Add(sheetName]);

// 이미 작성되어 있는 경우, 불러옵니다.
ExcelWorksheet sheet = excel.Workbook.Worksheets[sheetName];
```

----

## 입력할 데이터 지정

데이터를 입력하기 위한 자료를 생성합니다.  
다음은 각 행과 열의 데이터를 한꺼번에 입력하는 예제입니다.

\> 행과 열을 동시에 입력하는 예제입니다.

```
List<object[]> dataRows = new List<object[]>();

int itemCnt = 3;

// 출력할 데이터 객체
foreach (Item in items)
{
    // 각 행 정보를 담고 있는 객체
    object[] dataRow = new object[3];
    dataRow[0] = item.Name;
    dataRow[1] = item.Price; // int, decimal 데이터도 그대로 입력
    dataRow[2] = item.URL;

    // 각 열 정보를 행에 입력
    dataRows.Add(dataRow);
}
```

문자열이 아닌, 숫자(`int`. `decimal`) 데이터도 그대로 입력합니다. `string`형으로 변환하면 엑셀은 문자열 데이터로 인식합니다.  
각 행의 `dataRow`가 `object[]` 타입이므로 라이브러리에서 타입 언박싱하여 자동으로 처리합니다.

### 입력 데이터 구간 지정

엑셀에서 행 / 열 구간 선택 시 사용하는 `A13:F13` 형태의 구간입니다.  
\> 예: 3개의 데이터를 2번째 행의 A부터 C까지의 열에 입력하고자 할 경우

```
// LoadFromArrays는 전체 범위가 아닌 시작 행 번호와 각 데이터의 열 크기만 맞추면 됩니다.
// itemCnt 가 3이므로, A ~ C 까지 입력. 시작 행은 2 일 때,

string headerRange = String.Format("A2:{0}2", Char.ConvertFromUtf32(itemCnt + 64));
// "A1:C1"
// 대문자 A의 바이트 코드 = 64 에 데이터 갯수를 더함으로써 해당 열을 나타냅니다.
//! Z가 넘을경우 AA로 변환되므로 추가적인 작업이 필요합니다.
```

### 데이터 입력 메서드

`sheet.Cells[headerRange]` 의 각 메소드를 상황에 맞게 사용합니다.

|메서드|데이터 형식|설명|
|---|------|------------|
LoadFromArrays|IEnumerable<object[]>|각 열의 데이터 - object[] 의 객체, 각 행의 데이터 - object 객체
LoadFromCollection|IEnumerable<T>|한 열을 대상으로 각 행의 데이터

### 데이터 입력 

작성된 데이터와 데이터 구간을 이용하여 데이터를 시트에 입력합니다.  
데이터가  입력되면 해당 구간의 `Row`와 `Column`은 자동으로 생성됩니다.

```
sheet.Cells[headerRange].LoadFromArrays(dataRows);
```

---

## 서식 지정

각 열 번호에 해당하는 `sheet.Column(n)`에 서식을 지정할 수 있습니다. 행 `sheet.Row(n)`에도 동일하게 적용됩니다.

### 열 크기 

```
sheet.Column(3).Width = 20;
````

### 출력 포맷

```
sheet.Column(3).Style.Numberformat.Format = @"₩#,##0_);(₩#,##0)"; // 원표시, 3단위별 단위표시
```

## 엑셀 파일로 출력

`FileInfo` 또는 `Stream` 으로 저장할 수 있으며, 비밀번호 설정도 가능합니다.

```
excel.SaveAs(excelFile);
```
----

## 전체 코드

```
FileInfo excelFile = new FileInfo(fileName);
// 지정된 파일이 이미 있을경우 삭제한다.
if (excelFile.Exists) excelFile.Delete();

// #1. 시트 지정
string[] sheets = new string[] { "데이터" };

ExcelPackage.LicenseContext = OfficeOpenXml.LicenseContext.NonCommercial;

using (ExcelPackage excel = new ExcelPackage())
{
    // 시트가 하나이므로 추가적인 작업은 없음.
    excel.Workbook.Worksheets.Add(sheets[0]);


    // dataRow로 데이터를 지정해서 저장합니다.


    // #1. 시트 지정
    ExcelWorksheet sheet = excel.Workbook.Worksheets[sheets[0]];

    // #2. 지정한 데이터 저장하기
    // 헤더 저장

    // 각 아이템에 대한 데이터 저장 - 범위에 의해 가로에 순차적으로 저장된다.
    // 제품ID, 이름, 최저가, 최저가 쇼핑몰, URL

    int idx = 1;

    /// *****************************
    /// 출력 데이터 열이 변경될 경우 수정
    int itemCnt = 5;


    // 각 list 객체가 한 열이며, 각 obj는 해당 행에 대한 데이터를 가지고 있다.
    List<Object[]> dataRows = new List<Object[]>();
    string[] dataRow = new string[itemCnt];
    /// *****************************
    /// 출력 데이터 열이 변경될 경우 수정
    dataRow[0] = "제품ID"; dataRow[1] = "이름"; dataRow[2] = "최저가";
    dataRow[3] = "최저가 쇼핑몰"; dataRow[4] = "URL";
    dataRows.Add(dataRow);

    foreach (Item item in objects)
    {
        // 가로 범위 지정이 알파벳 문자임으로 데이터 길이에서 이를 변환합니다.
        object[] _dataRow = new object[itemCnt];
        _dataRow[0] = item.ProductId;
        _dataRow[1] = item.Name;
        _dataRow[2] = item.LowPrice; // 숫자 데이터는 문자로 변환할 필요 없이 그대로 입력합니다.
        _dataRow[3] = item.LowPriceMallName;
        _dataRow[4] = item.LowPriceLink;
        dataRows.Add(_dataRow);
        
        idx++;
    }

    // 열 번호는 0부터 시작이므로 0으로 고정. 데이터 갯수에 따라 행 번호만 설정한다.
    string headerRange = String.Format("A1:{0}1", Char.ConvertFromUtf32(itemCnt + 64));
    sheet.Cells[headerRange].LoadFromArrays(dataRows);


    // #3. 컬럼 스타일 지정하기
    // 데이터를 추가하면 컬럼은 자동으로 생성되며, 시작 인덱스는 1 입니다.

    // 각 열의 width 를 지정
    sheet.Column(1).Width = 20;
    sheet.Column(2).Width = 120;
    sheet.Column(3).Width = 20;
    sheet.Column(4).Width = 20;
    sheet.Column(5).Width = 50;


    // 각 열 별로 서식을 지정
    sheet.Column(1).Style.Numberformat.Format = "@";
    sheet.Column(2).Style.Numberformat.Format = "@";
    sheet.Column(3).Style.Numberformat.Format = @"₩#,##0_);(₩#,##0)"; // 원표시, 3단위별 단위표시
    sheet.Column(4).Style.Numberformat.Format = "@";
    sheet.Column(5).Style.Numberformat.Format = "@";

    excel.SaveAs(excelFile);
}
}
```