---
title:  "머신러닝 - tensorflow 의 기본적인 연산"
date:   2020-07-07 16:20:00 +0900

toc: true
toc_label: "둘러보기"
toc_icon: "columns"

categories:
    - machine-learning
    - tensorflow

tags:
    - machine-learning
    - tensorflow
    - python
---

수정 중

# tensorflow의 기본적인 연산

**tensorflow 1.x 버전 기준입니다.**  

[Tensorflow 공식 문서](https://www.tensorflow.org/guide/tensor?hl=ko)

## 텐서(Tensor) 의 정의

tensorflow에서 노드로 다루는 모든 것. 벡터와 행렬을 일반화한 것으로, 고차원으로 확장 가능합니다.  

먼저 텐서로 이루어진 그래프를 작성하고, `tf.Session` 세션을 생성하여 지정된 연산을 수행함으로써  `sess.run([op1, op2, ...])` 텐터플로우 라이브러리를 이용한 머신러닝을 수행하게 됩니다.

|이름|설명|
|----|---------|
tf.Variable|변수 값을 갖는 텐서입니다. 생성 시 기본값이 필요합니다. 값의 변경이 가능합니다.
tf.constant|상수 값을 갖는 텐서입니다. 값의 변경이 불가능합니다.
tf.placeholder|2.x 버전에서 Variable 등으로 대체되었으며, 사용자 입력이 가능한 텐서입니다.
tf.SparseTensor|희소 텐서

## 텐서(Tensor) 의 속성

`Tensor`가 가지는 속성은 크게 3가지로 구분됩니다.

|이름|설명|
|----|---------|
rank|Tensor의 차원
shape|Tensor가 차원별로 가진 객체수의 집합
dtype|Tensor가 가진 데이터의 자료형

### rank

Tensor가 가지고 있는 데이터의 차원입니다.

|데이터|값|
|----|---------|
3|0 (단일 값)
[1, 2, ...]|1
[[1, 2], [3, 4], ...]|2

### shape

Tensor가 가지고 있는 각 데이터의 갯수입니다. 외부 차원의 데이터 갯수부터 측정됩니다.  
`placeholder` 노드에서 shape을 정의할 경우, 해당 데이터의 갯수에 제한을 두지 않는다면 `None`으로 정의할 수 있습니다.

|데이터|값|
|----|---------|
3|0 (단일 값)
[1, 2, ...]|1
[[1, 2], [3, 4], ...]|2


### dtype

Tensor가 가진 데이터의 자료형이며, 배열의 모든 데이터는 하나의 자료형을 가집니다.



## 텐서(Tensor) 의 연산

### 상수 텐서의 연산으로 새로운 값을 가진 텐서 생성
```
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0) # tf.flost32 implicitly (기본형 적용)
node3 = tf.add(node1, node2)

# 1.x 의 버전은 세션에서 노드의 연산을 수행합니다.
sess = tf.Session()

# 단일 연산 또는 다중 연산 (list) 가능.
print("node1, node3", sess.run([node1, node3]))
# node1, node3 [3.0, 7.0]
```

### placeholder 텐서로 런타임에 지정한 값을 연산한 텐서 생성
```
# 그래프를 실행시키는 단계에서 값 설정
a = tf.placeholder(tf.float32) # type
b = tf.placeholder(tf.float32)
adder_node = a + b

# 단일 연산. placeholder 노드의 이름으로 값을 제공해서 업데이트함
print(sess.run(adder_node, feed_dict={a: 3, b: 4.5}))
# 다중 연산 결과는 [3, 7] 형태로 여러 연산 결과가 반환된다.
print(sess.run(adder_node, feed_dict={a: [1,3], b: [2,4]}))
```