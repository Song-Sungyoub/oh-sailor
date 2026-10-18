# 오!수병 (오늘은 내가 요리사 수병)
![오!수병](./pic/logo.png)

## 프로젝트 주소
[ohsailor.kr](http://20.194.39.12)

## 프로젝트 소개
- 오!수병은 크게 두 가지 주제를 갖고 있는 커뮤니트 플랫폼입니다. 장병들에게 크게 맞다아 있는 문제들을 해결하고자 만들게 되었습니다. 그 둘은 음식과 정보입니다. '오!늘은 내가 요리사'와 '오!신트'입니다. 먼저 음식의 주제를 담은 '오!늘은 내가 요리사'는 식단에 대한 의견을 조리병과 소통할 수 있는 커뮤니티입니다. 메뉴를 평가하고, 개선되어야 할 점에 대해 리뷰를 남길 수 있습니다. 조리병과 조리간부들과 장병들간에 소통이 이루어지면서, 개선할 점을 쉽게??? 알 수 있습니다.


## 기능 설명
### 오!늘은 내가 요리사
- 식단표 확인
- 메뉴 평가
- 식단 커뮤니티


### 오!신트 (Osint)
- 


## 컴퓨터 구성 / 필수 조건 안내 (Prerequisites)
* ECMAScript 6 지원 브라우저 사용
* 권장: Google Chrome 버젼 77 이상

## 기술 스택 (Technique Used) 
### Server(back-end)
 - PHP7.0, Python3.9 
 - laravel 프레임워크(PHP) 
 - MySQL (DBMS) 
 
### Front-end
 -  HTML5, CSS3, JavaScript를 이용한 개발
 -  UI framework
 -  Bootstrap, Jquary 등의 프레임워크

## 설치 안내 (Installation Process)
```bash
$ git clone git@github.com:osamhack2021/Web_OhSailor_1FleetCERT.git
$ yarn or npm install
$ yarn start or npm run start
```

## 프로젝트 사용법 (Getting Started)
**마크다운 문법을 이용하여 자유롭게 기재**

잘 모를 경우
구글 검색 - 마크다운 문법
[https://post.naver.com/viewer/postView.nhn?volumeNo=24627214&memberNo=42458017](https://post.naver.com/viewer/postView.nhn?volumeNo=24627214&memberNo=42458017)

 편한 마크다운 에디터를 찾아서 사용
 샘플 에디터 [https://stackedit.io/app#](https://stackedit.io/app#)
 
## 팀 정보 (Team Information)
- song sung youb (ssyoub0327@daum.net), Github Id: Song-Sungyoub

## 저작권 및 사용권 정보 (Copyleft / End User License)
 * [MIT](https://github.com/osamhack2021/Web_OhSailor_1FleetCERT/blob/master/license.md)

This project is licensed under the terms of the MIT license.

※ [라이선스 비교표(클릭)](https://olis.or.kr/license/compareGuide.do)

※ [Github 내 라이선스 키워드(클릭)](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/licensing-a-repository)

※ [\[참조\] Github license의 종류와 나에게 맞는 라이선스 선택하기(클릭)](https://flyingsquirrel.medium.com/github-license%EC%9D%98-%EC%A2%85%EB%A5%98%EC%99%80-%EB%82%98%EC%97%90%EA%B2%8C-%EB%A7%9E%EB%8A%94-%EB%9D%BC%EC%9D%B4%EC%84%A0%EC%8A%A4-%EC%84%A0%ED%83%9D%ED%95%98%EA%B8%B0-ae29925e8ff4)


## 비공개 실행 설정

DB 접속은 `web/database.php`에서 서버 환경변수 `OHSAILOR_DB_HOST`(기본 localhost), `OHSAILOR_DB_USER`, `OHSAILOR_DB_PASSWORD`, `OHSAILOR_DB_NAME`을 읽습니다. 필수 값이 없으면 연결을 시도하지 않고 일반 오류를 반환합니다. PHP 워커(Apache/PHP-FPM 등)에 환경변수가 전달되도록 설정하세요. `.env.example`은 이름 안내용이며 PHP가 `.env`를 자동으로 읽지는 않습니다. 실제 비밀번호는 저장소 밖에서 설정합니다.

phpMyAdmin 쿠키 인증은 별도의 `PMA_BLOWFISH_SECRET` 환경변수에 정확히 32자의 무작위 ASCII 값을 설정해야 합니다. 예: `python -c "import secrets; print(secrets.token_hex(16))"`. 생성된 값은 커밋하지 마세요.

이전에 커밋된 접속정보는 사용 중인 서버에서 교체해야 합니다. 코드 변경만으로 DB 비밀번호가 바뀌지는 않습니다. 운영 DB와 README의 공개 연락용 이메일은 유지합니다. 과거 Git 이력 정리는 별도이며, 설정을 복구할 때도 비밀번호를 소스에 다시 넣지 마세요.

이번 정리 커밋은 `[skip ci]`로 업로드해 자동 배포를 건너뜁니다. 이후 배포 전 서버 환경변수와 실제 DB 연결을 별도로 확인하세요.

검증: PHP CLI가 있는 환경에서 `python -m unittest discover -s tests -v`. `PHP_BINARY`로 PHP 실행파일을 지정할 수 있습니다. 테스트는 DB 연결 함수를 대체하므로 운영 DB에 접속하지 않습니다.
