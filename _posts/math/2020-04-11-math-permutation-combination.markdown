---
title:  "순열과 조합 파이썬 구현"
date:   2020-04-11 12:00:00 +0900

toc: true
toc_label: "둘러보기"
toc_icon: "columns"

categories: algorithm
tags: math algorithm python
---

순열과 조합에 대해 알아보고, 이를 구하는 알고리즘을 작성해 보자.

💡참고 - 작성한 예제 코드는 **입력 데이터에 중복이 없음을 가정** 하고 작성하였다. 중복된 데이터가 있다면 중복된 결과가 출력되며, 이 경우 `list(set(data))` 등으로 적절히 처리한다.

[↪️출처 - SUNGHWAN PARK 님의 블로그](https://shoark7.github.io/programming/algorithm/Permutations-and-Combinations) 코드 일부를 참고하였습니다.


### 순열
**경우의 수 : nPr = n! / (n-r)!**

n개의 원소가 있는 배열에서 r개의 원소를 순서를 구분하여 선택한다. 따라서 **[1, 2]** 와 **[2, 1]** 는 서로 다른 선택이 된다.

📝 python 순열 구하기 (제네레이터)
```
def select_permutation(arr: list, r: int, use_sort:bool=False, use_new_instance:bool=True):
    # use_new_instance: False인 경우 새 인스턴스를 만들지 않음. 단, chosen객체가 수정되면 안된다.
    # =True -> list()로 사용 할 수 없음.

    n = len(arr)
    assert n >= r
    # nPr = n! / (n-r)!
    # expected_count = math.factorial(n) // math.factorial(n - r)

    if use_sort: arr = sorted(arr)

    used = [False for _ in range(n)] # 전체 n을 제귀하면서 중복된 값을 추출한다.
    chosen = list() # 이곳에다가 데이터를 순차적으로 담는다.

    def generate():
        if len(chosen) == r:
            yield list(chosen) if use_new_instance else chosen
            return

        for i in range(n): # 전체 객체에 대하여 반복적으로 스캔함 (재귀)
            if not used[i]: # 아직 선택되지 않음
                chosen.append(arr[i])
                used[i] = True # arr 데이터가 중복 가능하므로 각 자리에 대한 사용 여부를 파악
                yield from generate()
                chosen.pop() # 이곳으로 돌아왔다면 append한 데이터가 마지막 데이터임
                used[i] = False

    yield from generate()
```

----

### 조합
**경우의 수 : nCr = n! / r!(n-r)! = nCn-r**

n개의 원소가 있는 배열에서 r개의 원소를 순서 구분없이 선택한다. 따라서 **[1, 2]** 와 **[2, 1]** 는 서로 같은 선택이 된다.

📝 python 조합 구하기 (제네레이터)
```
def select_combination(arr: list, r: int, use_sort:bool=False, use_new_instance:bool=True):
    # use_new_instance: False인 경우 새 인스턴스를 만들지 않음. 단, 객체가 수정되면 안된다.

    n = len(arr)
    assert n >= r
    # nCr = n! / r!(n-r)!
    # expected_count = math.factorial(n) // r!(n-r)!

    if use_sort: arr = sorted(arr)

    chosen = list() # 이곳에다가 데이터를 순차적으로 담는다.

    def generate(start: int):
        if len(chosen) == r:
            yield list(chosen) if use_new_instance else chosen
            return

        for _next in range(start, n): # 중첩 for문을 재귀함수로 구현하였다고 보면 된다.
            chosen.append(arr[_next])
            yield from generate(_next + 1) # 현재 수를 선택했으므로 그 다음 수를 선택합니다.
            chosen.pop()

    yield from generate(0)
```

----

#### 코드를 작성하며...
반복문으로 배열에서 N개의 원소를 순서대로 골라 구현하려고 했는데, 문제는 N이 **상수가 아닌 변수** 가 될 때였다. 이렇게 동일한 코드를 반복하는 방법 중 하나로 재귀함수를 이용해 구현할 수 있음을 알게 되었다.
