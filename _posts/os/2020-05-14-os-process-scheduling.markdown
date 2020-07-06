---
layout: post
title:  "운영체제의 기본 개념 - 스케쥴링"
date:   2020-05-14 10:00:00 +0900
categories: os
---


preemptive & non-preempotive (선점, 비선점)
선점: 특정 프로세스를 실행 중 아직 끝나지 않았으나, 다른 프로세스로 전환하게됨

비선점: 프로세스가 끝나거나, IO를 만나기 전에는 실행이 전환되지 않음.

? disk utilization
I/O를 대기하는 시간 동안만 다른 프로세스에서 실행을 하면 그 범위를 disk utilization 이라고 한다.
따라서, 해당 utilization이 높아질수록 각 프로세스별로 효율적으로 작업을 할 수 있게 됩니다.

## waiting time

특정 프로세스의 waiting time 구하기  
전체 실행 시간에서 자신의 실행 시간을 제외한 시간

? average waiting time - 각각의 waiting time을 더합니다

## response time

특정 프로세스가  CPU에서 실행되어 처리, 결과를 반환하기까지 걸리는 시간.

## time quantom


** 각 스케쥴링 알고리즘 별로 겐트 차트로 평균 응답, response 시간, 전체 시간을 그려줍니다.


# 스케쥴링

프로세스 간 실행 시간을 공평하게 측정하려면 어떻게 해야 하는가?

작업에 따라 시간배율을 달리 해야할 수 도 있다. (예: IO에 따른 배치)

* 짧은 시간동안 몰아서 하는 작업 : CPU intensive - 작업이 이루어지는 구간: CPU burst
IO 작업을 하는 프로세스들은 또 IO Queue에서 대기하여 순차적으로 IO작업을 수행한다.


## FIFO (first in first out - FCFS)
큐에 입력된 순서대로 작업을 전체 실행하고 다음 작업으로 넘거삽니다.


## Round-Robin (RR)

순차적으로 프로세스를 실행하게 됩니다. FIFO와 동일하나 time slice / quantum 을 두고 해당 시간이 초과하면 큐의 끝으로 이동하고
context switch / 다음 프로세스를 실행합니다.

대부분의 현대 스케줄러에서 사용되는 알고리즘의 근간

작업 시간이 너무 크다면: response time 문제 발생
작업 시간이 너무 짧다면: 모든 작업이 매우 조금씩 실행되어 매우 늦게 결과가 출력될 것임.


## SJF (Shortest Job First)

짧게 실행되는 작업 여러개, 길게 실행되는 작업 한개.  
짧게 실행되는 작업들을 빠르게 먼저 처리한 후 나머지 긴 작업을 처리한다.

문제점: (starvation avoid) 프로세스 스케쥴링 중 짧은 시간의 작업들이 계속 추가된다면, 길게 실행되는 작업은 영원히 실행되지 못하고 기다리게 된다.

이것도 작업의 시간을 예측하는데 어려움이 있으므로 구현하기에 비현실적이게 된다.


## SRTF (Shortest Remaining Time First)

`SJF` 스케쥴링에 선점 정책을 도입한 알고리즘. (Fair utilization)
장점: 평균 대기 시간 최소화
단점: 프로세스 생성시 총 실행시간 추정 작업이 필요함. (시간이 가장 작게 걸리는 작업부터 실행해야 하므로), 
이에 따라 구현 및 사용이 현실적으로 비현실적이임.

실제 시간이 얼마나 걸릴지 판단하기 쉽지 않으므로, 구현하기에 비현실적이게 된다.


## CSF 
프로세스별로 자신의 CPU시간 및 IO시간을 측정하여 CPU, IO 시간의 비율이 모든 프로세스에서 동일하도록 스케쥴링합니다.

----

사용하는 환경에 따라 시스템이 요구하는 목표가 다르며, 이에 따라 알맞는 스케쥴링 알고리즘을 이용하여야 한다.

### Multi-user systems

### Batch systems
    
### Interactive systems

### Real-time systems
