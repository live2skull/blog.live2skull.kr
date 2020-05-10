---
title:  "OS X에서 pip 문제 해결"
date:   2020-05-10 17:30:00 +0900

toc: true
toc_label: "둘러보기"
toc_icon: "columns"

categories: python pip
tags: python lxml html
---

개발 환경 설정 중 겪은 오류들과 문제 해결 방법을 적어두었습니다.

## clang / gcc 컴파일러 오류

### 1. `ld` 라이브러리 오류

```
ld: library not found for -lssl
```

오류가 발생할 수 있는 경우는 다음과 같습니다.

- -l `library` 에 해당하는 라이브러리가 설치되어 있지 않음.
- `LIBRARY_PATH` 환경변수가 설정되어 있지 않음.
- 라이브러리는 설치되어 있으나 환경변수에 등록되어 있지 않음.

라이브러리가 설치되어 있지 않은 경우, 해당 라이브러리를 설치합니다. (OS X의 경우 대부분의 라이브러리를 brew에서 설치할 수 있습니다.)

사용하는 쉘에 맞는 `.profile` 에 `export LIBRARY_PATH=...` 로 라이브러리 경로를 설정하고 적용 후 재시도합니다.
