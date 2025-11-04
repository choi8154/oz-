# Django의 기능들

1. Object relational Mapping -> ORM이라고 부르는 DB 구조와 쿼리를 할 수 있는 기능
2. Authentication & Authorization -> 인증 허가 즉 로그인 관련 기능
3. Admin Interface -< 관리자 인터페이스
4. Internationalization -> 국제화, 번역 기능
5. URL Routing -> URL을 이용한 페이지 처리
6. Template Engine

MVT 구조

# 장점
- 개발 속도가 빠름
- 코드 재사용 및 모듈화 : 유연
- 안전한 웹 애플리케이션 구축 : 보안
- 패키지가 모두 준비가 되어 있음
- 개발 시간을 줄여주느느 관리자 페이지의 마법
- 개발 시간 및 코드를 줄여주는 모듈화의 마법 : 코드 재사용 효율성이 좋음
- 획일화도니 구조로 누가 코드를 봐도 적응 시간이 빠름
- 수 많은 패키지와 잘 구축된 커뮤니티

#  단점
- 잘 쓰려면 숙련 및 개념 탑재 필요

# 설계 아키텍쳐
브라우저 -> webserver -> urls.py -> views.py -> models.py -> db -> models.py
 -> views.py -> template -> views.py -> web server -> 브라우저