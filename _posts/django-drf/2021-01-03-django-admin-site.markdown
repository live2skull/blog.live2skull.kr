---
title:  "django admin site 만들기"
date:   2021-01-03 22:00:00 +0900

toc: true
toc_label: "둘러보기"
toc_icon: "columns"

categories: 
    - django

tags:
    - django
    - python
---

django에서 지원하는 admin site를 이용해 관리 페이지를 작성합니다.

# django admin site

## 소개

`django`는 django model로 정의한 모델의 데이터를 손쉽게 관리할 수 있도록 admin site 기능을 제공하며, django에서 기본적으로 제공하는 `User`, `Group`과 사용자가 지정한 
모델을 관리할 수 있습니다.

이러한 기능들은 `django.contrib.admin` 모듈에 구현되어

admin site 기능들에 대한 구현을 담고 있는 모델이며, 기본적으로 제공하는 `User`, `Group` 모델을 관리하는 admin site는 다음과 같이 구성되어 있습니다.

```
site = DefaultAdminSite()
```

기본 admin site 객체는 django에서 import하여 사용하는 다른 모듈에서 model의 관리가 필요한 경우 등록하는 기본 site 객체로,  
사용자는 해당 site 객체를 확장하거나, 별도의 admin site를 만들어 사용할 수 있습니다.

세부적인 설정은 문서 하단의 `AdminSite` 문단에서 다룹니다.
```
from django.contrib.admin import site, AdminSite

# 1. 기본 site 객체의 활용
my_site = site
my_site.site_title = "테스트" # title
my_site.site_header = "테스트 헤더" # 제목 헤더
my_site.site_url = "http://test" # 서비스 메인 페이지 url

#2. 새로운 AdminSite 클래스 작성
class MyAdminSite(admin.AdminSite):
    site_title = "테스트" # title
    site_header = "테스트 헤더" ## 제목 헤더
    site_url = "http://test" # 서비스 메인 페이지 url
```

### admin site를 프로젝트 url에 등록
admin site 객체 (AdminSite)를 다음과 같이 프로젝트 url에 등록합니다.

```
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    # ...
]
```

### admin site 접근 사용자 권한 설정

admin site 에 접근 가능한 사용자는 superuser 권한을 가져야 하며, 다음 명령어로 해당 권한을 가진 사용자를 생성할 수 있습니다.
```
python manage.py createsuperuser
```
---

## AdminSite

관리 페이지를 구성하는 `AdminSite` 클래스 구성에 대해 설명합니다.

### 관리 모델 추가

`AdminSite`는 각각의 모델 객체에 대한 관리 기능 (인스턴스 추가, 삭제, 수정 및 일괄 작업) 을 제공하며, 이를 위해 `AdminSite`에 클래스를 등록합니다.

관리 기능 정의 `ModelAdmin` 하단의 문단에서 상세히 다룹니다.

```
from django.contrib,admin import AdminSite, ModelAdmin
from myapp.model import Movie

class MyAdminSite(AdminSite):
    pass

my_site = MyAdminSite()

# 1. 관리 대상 Model 클래스 등록 (기본 옵션으로 관리)
my_site.register(Movie)

# 2. 관리 대상 Model 클래스와 관리 기능 정의 ModelAdmin 클래스 등록.
class MovieModelAdmin(MovieModelAdmin):
    pass

my_site.register(Movie, MovieModelAdmin)
```

### 페이지 커스텀화

admin site는 django 패키지 `templates/admin` 풀더에 사전 작성된 `html` 템플릿을 통해 렌더링됩니다.  
해당 파일을 커스터마이징하여 원하는 클라이언트 기능을 추가 구현할 수 있습니다.  

각 페이지에 대한 템플릿 파일 지정 속성은 다음과 같습니다.

|속성|설명|
|---|----|
|index_template|메인 페이지|
|app_index_template|앱 인덱스 페이지 (앱 model 리스트)|
|login_template|로그인 페이지|
|logout_template|로그아웃 페이지|
|password_change_template|비밀번호 변경 페이지|
|password_change_done_template|비밀번호 변경 완료 페이지|

다음 예시와 같이 경로를 작성할 경우, `현재 패키지 루트 + /templates/` 에서 템플릿 파일을 검색합니다. (`/myapp/templates/admin_page/inde.html`)

>⚠️ 기본 페이지가 표시될 경우, 기본 페이지와 경로 및 파일명이 동일한지 확인합니다.

```
class MyAdminSite(AdminSite):
    index_template = 'admin_page/index.html'
```

---

## ModelAdmin

admin site에 모델 등록 및 관리 기능을 정의하는 클래스입니다.  
각 모델에 관한 페이지는 크게 "객체 생성", "객체 수정", "객체 리스팅 및 탐색" 으로 구성되어 있습니다.

다음 예시를 통해 각 속성과 구성 방법에 대해 설명합니다.

```
from django.contrib import admin, messages

class ModelAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('id', 'name', 'score')
    list_display_links = ('id', 'name')
    list_filter = ('score',)
    ordering = ('name', )

    fieldsets = [
        ('일반정보', {'fields' : ('name', 'opened_at', 'genres', 'score')}),
        ('상세정보', {
            'fields' : ('actors', 'thumb_url', 'img_url', 'description')
        })
    ]

    autocomplete_fields = ('actors', )
    filter_horizontal = ('genres', )

    def make_published(self, request, queryset: QuerySet):
        count = queryset.count()

        if count == 0:
            self.message_user(
                request, "아무 객체도 선택되지 않았습니다.", messages.WARNING
            )
        else:
            self.message_user(
                request, "%d개의 객체가 선택되었습니다." % count, messages.INFO
            )

    make_published.short_description = "추가된 액션" ## 클라이언트 액션 리스트에 표시
    actions = [make_published]

```

### 리스트 페이지 구성

#### search_fields
리스트 페이지에서 객체를 검색하기 위한 필드를 지정합니다. 필드는 `CharField`, `IntegerField`, `DecimalField` 와 같이 문자열로 변환할 수 있는 비참조형 필드에 대해 사용 가능하며, 리스트 페이지의 검색 기능을 이용하여 객체를 검색할 수 있도록 합니다.

#### list_display
리스트 페이지에서 표시할 객체의 필드를 지정합니다. 지정하지 않으면 객치의 `__str__` 값만을 표시합니다.

#### list_display_links
리스트 페이지에서 객체 수정(상세정보 페이지) 하이퍼링크가 표시되는 필드를 지정합니다.  
해당 필드는 `list_display`에도 선언되어야 합니다.

#### list_filter
리스트 페이지에서 객체 필터링 검색에 사용될 필드를 지정합니다.  
모든 비참조형 필드에 사용 가능하나, `choices=` 속성이 지정되어 입력 값이 제한된 필드나 입력 가능한 값의 범위가 크지 않은 정수형 필드에 적합합니다.


### 리스트 페이지 - Action 정의

Action은 단일 또는 선택한 여러개의 객체에 대해 일괄적으로 작성한 특정 작업을 실행할 수 있는 기능으로써, 본 예제에서는 `make_published` 메서드에 특정 작업을 정의하였습니다.

#### actions 
대상 클래스에 대해 사용할 Action 메서드를 추가합니다.

#### Action 정의
위 예제의 `make_published` 을 참고합니다.  

클라이언트 요청 컨텍스트 `request`, 클라이언트가 선택한 객체에 대한 `queryset (QuerySet)` 을 받아 지정한 역할을 수행합니다.

작업 후 `self.message_user(request, message:str, level:int)` 메서드를 통해 실행 결과를 클라이언트에게 반환할 수 있으며, 이는 클라이언트의 요청 결과에 렌더링되어 반환됩니다. 


### 객체 수정 페이지

#### fieldsets
객체 수정 및 데이터 열람을 위한 필드를 데이터 형식에 맞추어 지정합니다. 본 속성에 정의되어 있지 않은 필드는 관리 페이지에서 접근할 수 없습니다.

>⚠️ 상황에 따라 필드를 제한할 수 있도록 `get_fieldsets` 메서드를 재정의할 수 있습니다.

#### filter_horizontal
`ForeignKey` 및 `ManyToMany` 필드를 위한 속성으로, 해당 속성에 정의된 필드는 M2M 참조 지정을 위한 그래픽 탐색기가 제공됩니다.

>⚠️ 대상 객체의 인스턴스가 많은 경우, `autocomplete_fields`를 사용하는 것이 권장됩니다.

#### autocomplete_fields
`ForeignKey` 및 `ManyToMany` 필드를 위한 속성으로, 해당 속성에 정의된 필드는 M2M 참조 지정을 위한 그래픽 탐색기가 제공됩니다.

`filter_horizontal, filter_vertical` 필드와는 달리 선택 가능한 객체가 많은 경우에 입력(참조) 할 객체를 서버 사이드에서 검색해 선택할 수 있습니다.

이 때 대상 객체의 검색을 위해, 해당 모델 클래스에 대해서도 검색이 가능하도록 admin site 인스턴스에 등록되어야 합니다.

```
# ... (본 예제)

# Actor 클래스를 검색 가능하도록 search_fields 필드를 지정한다.
class ActorModelAdmin(admin.ModelAdmin):
    search_fields = ('name', )

my_site.register(Movie, MovieModelAdmin)
my_site.register(Actor, ActorModelAdmin)
```


### 페이지 커스텀화

admin site와 동일하게, 각 페이지별로 지정된 템플릿 파일을 커스터마이징하여 원하는 클라이언트 기능을 추가 구현할 수 있습니다.

각 페이지에 대한 템플릿 파일 지정 속성은 다음과 같습니다.

|속성|설명|
|---|----|
|add_form_template|객체 추가 페이지|
|change_form_template|객체 세부 정보 (수정) 페이지|
|change_list_template|리스트 페이지|
|delete_confirmation_template|삭제 확인 페이지|
|delete_selected_confirmation_template|벌크 삭제 확인 페이지|
|object_history_template|객체 히스토리 페이지 (⚠️ 확인 필요)|
|popup_response_template|Action 실행 결과 팝업 템플릿|