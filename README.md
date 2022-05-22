# tasty2b9
### 선릉 주변(선릉역, 선정릉역, 삼성중앙역) 음식점 검색 어플리케이션입니다.
------------------------

## 기능기획
프로젝트 사전에 기획한 기능목록입니다.
수행한 기능들은 체크박스를 통하여 표시하였습니다. 

- [x] 모바일 UI
- [x] 카테고리별 음식점 리스트
- [x] 검색결과 음식점 리스트
- [x] 음식점 리스트 결과값에 대한 거리순 정렬
- [x] 음식점 리스트 결과값에 대한 별점순 정렬
- [ ] 음식점 리스트 결과값에 대한 좋아요순 정렬
- [x] 음식점 리스트 결과값에 대한 가격순 정렬
- [x] 음식점 리스트 결과값에 대한 페이지네이션
- [x] 음식점 상세페이지
- [x] 음식점 메뉴 및 가격 표시
- [ ] 음식점 별점 기능
- [ ] 음식점 좋아요 기능
- [x] 로그인
- [x] 회원가입
- [ ] 회원탈퇴
- [x] 네이버 지도API로 검색결과 음식점 위치 표시
- [ ] 네이버 지도API로 검색결과 음식점 네임태그 표시
- [ ] 네이버 지도API로 검색결과 지도 센터포인트 변경
------------------------

## 폴더구조
프로젝트 폴더구조는 아래와 같습니다.

```
.

├── README.md
├── Dockerfile
├── docker-compose.yml
├── node_modules
├── package.json
├── package-lock.json
├── tailwind.config.js
├── requirements
│   ├── deploy.txt
│   └── dev.txt
├── db.sqlite3
├── sample.env
├── manage.py
├── config
│   ├── __init__.py
│   ├── asgi.py
│   ├── nginx
│   │   └── nginx.conf
│   ├── settings
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── deploy.py
│   │   └── dev.py
│   ├── urls.py
│   └── wsgi.py
├── core
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── restaurants
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── accounts
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── utils
│   ├── bulk_db.py
│   ├── naver_api.py
│   ├── scraper.py
│   └── urls.py
├── templates
│   ├── accounts
│   │   ├── login.html
│   │   └── signup.html
│   ├── core
│   │   └── base.html
│   └── restaurants
│       ├── detail.html
│       └── home.html
└── static
   ├── admin
   ├── base
   ├── debug_toolbar
   └── imakewebthings-waypoints
```
------------------------

## 기술스택
프로젝트 결과물은 아마존 클라우드를 통해 배포하였으며,
기술사용 스택은 아래와 같습니다.

- AWS EC2
- AWS RDS(MySQL)
- NGINX
- GUNICORN
- DOCKER
- DJANGO
- BOOTSTRAP
- TAILWIND CSS
------------------------

## 환경설정
virtualenv를 사용하여 아래와 같은 버전으로 작업하였습니다.

- Python 3.8.2
- Django 3.2
- .env (sample.env참조) 
------------------------

## 설치
프로젝트에 필요한 서드파티들은 requirements.txt 파일을 통해 설치할 수 있습니다.
```
pip install -r tasty2b9/requirements/dev.txt

```
or
```
pip install -r tasty2b9/requirements/deploy.txt

```
------------------------

## KPT회고
- Keep:
    - 단독으로 fullstack프로젝트를 진행했던점도 있었지만, 디자인이 구체화될수록
    기능이 명확해지고 그에따른 데이터 구조와 데이터서빙 양상이 달라졌기 때문에,
    코드를 갈아엎는 과정을 통해 다시금 디자인 및 기능기획의 중요성을 깨닫게 되었습니다.
    - DRF사용에만 익숙해져 있어서 라이브러리에 대해 의존성이 높았는데, 장고의 MVT구조와 FBV의 사용을 통해
    코드작성에 대해 고려해볼 점들을 다시금 다지게 되는 기회였습니다.
- Problem:
    - 초기에 기획했던 기능들과 디자인에 대해 2주안에 다 구현하는것을 목표로 삼았었지만,
    미구현된 기능들의 부재와 특히 음식점 상세 페이지의 디자인이 미흡하였습니다.
    - 결과물에 대하여 살펴보니 오히려 음식점 상세 페이지보다 우선순위로 놓고 보아야 할 기능은
    음식점 리스트 결과에 대하여 센터포인트가 유동적으로 바뀌어야 하는 부분이었던것 같습니다.
    - mobile ui에 대하여 pagination시 infinite scroll을 구현하려고 하였지만,
    타 스크립트와 충돌이 일어나는 부분이 있어 적용되지 않은 부분입니다.
    - 음식점 이미지를 naver url로 보여주기 때문에 규격화되지 않았는데,
    s3작업이나 기타수정을 통해 사이즈 규격을 맞추어야할 부분입니다.
    - home view에서 template에 서빙해줄 context의 사용에서 반복되는 부분들이나
    template사용에 직접적으로 불필요한 부분들은 직관적인 set으로 변경할 필요가 있는것 같습니다.
    - 정렬시 발생되는 추가 쿼리셋에 대해 살펴보았을때, 중복되는 부분은 발견하지 못하였지만,
    pagination시 음식점 이름이 유니크한 값임에도 중복되는 음식점이 발견되었습니다.
- Try:
    - 중복되는 음식점에 대하여 가격순 정렬의 queryset에 문제가 있는것으로 생각되어
    질의되는 query들을 살펴보며 debugging중에 있습니다.
    → (해결) paginator에 인자로 들어가는 queryset에서 order_by사용시,
    paginator이후 각 페이지에서 질의하는 데이터들은
    정렬 기준이 되는 동일 데이터값에 의해 랜덤하게 사용되기 때문에
    order_by에 추가로 unique필드값을 넣어줘야 하는것으로 확인했습니다.
    ('queryset to become randomly ordered when using paginator',
    reference: https://github.com/encode/django-rest-framework/issues/6886)