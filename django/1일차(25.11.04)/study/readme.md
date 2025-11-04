# django ORM

### 1) poetry add ipython
- ipython : shell 이쁘게 보이는거
- 사용법 : python manage.py 
### 2) poetry add django-extensions
- 쉘에 기본적으로 모든 요소 import 해 옴
- settings.py에 추가 : THIRD_PARTY_APPS 에 "django_extensions" 의존성 추가
### 3) python manage.py shell_plus 
- 파이썬에서 요소르 import를 한 상태로 python 인터프리터 실행
### 4) ORM 사용법
- <TABLE_객체>.objects.all()
- <TABLE_객체>.objects.filter(name="이름")
- <TABLE_객체>.objects.filter(name__icontains="이")
- <TABLE_객체>.objects.filter(id__lte=<숫자>) : 이하
- <TABLE_객체>.objects.filter(id__gte=<숫자>) : 이상
- <TABLE_객체>.objects.first() : 처음
- <TABLE_객체>.objects.last() : 마지막
- <TABLE_객체>.objects.filter(name=<이름>).delete() : 삭제
- <TABLE_객체>.objects.create(name=<이름>, age=<나이>) : 추가
- A = <TABLE_객체>(name=<이름>, age=<나이>)
  - A.save() : 추가2
- <TABLE_객체>.objects.count() : 객체 수
- <TABLE_객체>.objects.bulk_create(<리스트>) : 리스트 전부를 필드로 넣음
- 