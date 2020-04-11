---
layout: post
title:  "순열과 조합"
date:   2020-04-11 12:00:00 +0900
categories: math python algorithm
---

순열과 조합에 대해 알아보고, 이를 구하는 알고리즘을 작성해 보자.

### 순열
**전체 갯수: nPr = n! / (n-r)!**

n개의 원소가 있는 배열에서 r개의

📝 python 순열 구하기 (제네레이터)
```
## TODO: 제네레이터 버전 함수 작성
def select_permutation(arr: list, r: int, use_sort:bool=False) -> list:
    n = len(arr)
    assert n >= r
    # nPr = n! / (n-r)!
    # expected_count = math.factorial(n) // math.factorial(n - r)

    if use_sort: arr = sorted(arr)

    used = [False for _ in range(n)] # 전체 n을 제귀하면서 중복된 값을 추출한다.
    chosen = list() # 이곳에다가 데이터를 순차적으로 담는다.
    results = list()

    def generate():
        if len(chosen) == r:
            results.append(list(chosen)) # new instance
            return

        for i in range(n): # 전체 객체에 대하여 반복적으로 스캔함 (재귀)
            if not used[i]: # 아직 선택되지 않음
                chosen.append(arr[i])
                used[i] = True # arr 데이터가 중복 가능하므로 각 자리에 대한 사용 여부를 파악
                generate()
                chosen.pop() # 이곳으로 돌아왔다면 append한 데이터가 마지막 데이터임
                used[i] = False

    generate()
    return results
```


### 조합

...
