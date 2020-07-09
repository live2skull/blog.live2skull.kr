---
title:  "머신러닝 - 준비"
date:   2020-07-07 12:50:00 +0900

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

## 개발환경 셋팅 - Tensorflow v1.x 설치

처음 학습하고자 하는 강의가 텐서플로우 1 버전을 바탕으로 구성되었으므로, 1 버전의 마지막인 `1.15.3` GPU 버전을 설치합니다.

설치환경 : 윈도우 10, python 3.7

### [1. NVIDIA 소프트웨어 설치](https://www.tensorflow.org/install/gpu?hl=ko)

CUDA Toolkit 설치후 해당 버전에 맞는 cuDNN을 적당한 폴더에 풀고 PATH에 추가한다.

[CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit) : 고성능 GPU 가속 애플리케이션을 개발할 수 있는 개발 환경을 제공  
[cuDNN SDK](https://developer.nvidia.com/cudnn) : 딥러닝(딥 뉴럴 네트워크)를 위한 CPU 가속 기본 라이브러리.

```
# CUDA Toolkit
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\bin
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\extras\CUPTI\libx64
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\include

# cuDNN SDK
C:\tools\cuda\bin
```

**tensorflow-gpu==1.15.3 버전은 CUDA 10.0 / cuDNN SDK 7.6.3 설치**

### 2. tensorflow 라이브러리 설치
pip 19 이상 버전이 필요하며, python 3.6 ~ 3.7을 지원한다. 설치 도중 일치하는 라이브러리가 없으면 지원되지 않는 파이썬 / pip 버전을 사용했을 가능성이 높음.

```
pip install tensorflow-gpu==1.15.3
```


### 설치 후 확인
tensorflow 모듈을 로드하고 테스트 코드를 실행해 봅니다.
```
(.venv) D:\development\mllab>python
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
2020-07-07 15:35:28.964137: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cudart64_100.dll
>>> hello = tf.constant("hello, tensorflow!")
>>> sess = tf.Session()
2020-07-07 15:35:48.211295: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library nvcuda.dll
2020-07-07 15:35:48.378750: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1639] Found device 0 with properties:
name: GeForce GTX 670MX major: 3 minor: 0 memoryClockRate(GHz): 0.601
pciBusID: 0000:01:00.0
2020-07-07 15:35:48.390468: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cudart64_100.dll
2020-07-07 15:35:48.409731: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cublas64_100.dll
2020-07-07 15:35:48.430540: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cufft64_100.dll
2020-07-07 15:35:48.443181: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library curand64_100.dll
2020-07-07 15:35:48.462556: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cusolver64_100.dll
2020-07-07 15:35:48.479516: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cusparse64_100.dll
2020-07-07 15:35:48.511730: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cudnn64_7.dll
2020-07-07 15:35:48.520179: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1721] Ignoring visible gpu device (device: 0, name: GeForce GTX 670MX, pci bus id: 0000:01:00.0, compute capability: 3.0) with Cuda compute capability 3.0. The minimum required Cuda capability is 3.5.
2020-07-07 15:35:48.536480: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1180] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-07-07 15:35:48.546524: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1186]
>>> print(sess.run(hello))
b'hello, tensorflow!'
>>>
```

