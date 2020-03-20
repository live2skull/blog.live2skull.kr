---
layout: post
title:  "파이썬 패키지 생성 및 배포 가이드"
date:   2019-09-01 00:59:09 +0000
categories: python package pip distuil
---


git branch 관리
jenkins 를 이용하여 master branch 로 push (commit) 이 발생하였을때만
자동화하여 빌드를 하도록 한다.

# http://amazingguni.github.io/blog/2016/03/git-branch-%EA%B7%9C%EC%B9%99

# https://docs.djangoproject.com/ko/3.0/intro/reusable-apps/
# http://blog.naver.com/PostView.nhn?blogId=lingua&logNo=221537606241&parentCategoryNo=43&categoryNo=&viewDate=&isShowPopularPosts=false&from=postView
# https://rampart81.github.io/post/python_package_publish/

# 레퍼런스보다는 hack에 가까우므로 setup() 코드를 이용합니다.
# https://stackoverflow.com/questions/14399534/reference-requirements-txt-for-the-install-requires-kwarg-in-setuptools-setup-py
# from pip._internal.req import parse_requirements
# install_reqs = parse_requirements('requirements.txt')

# https://truveris.github.io/articles/configuring-pypirc/
# 최종 패키지 작성이 완료되면
# 해당 셋팅을 한 후, twine upload --repository api dist/.... (빌드된 파일)
# python setup.py bdist_egg
