## 0. Markdown(MD)
  - MD언어: 설명, 정리 언어
  - MD문법 존재(30분 공부)

## 1. 개발환경 구축
### 1-1. Anaconda
  - anaconda prompt 실행행
  - conda env list: 가상 환경 목록 보기
  - conda create -n llm prthon=3.11: llm 가상환경 생성
  - conda activate llm: 11m 가상환경 접속
  - pip list: 가상환경에 설치된 라이브러리 목록 보기
  - pip install [라이브러리]: 라이브러리 설치
  - cls: 화면 청소
  - 아나콘다는 편리하지만 매우 무거움
### 1-2. 로컬 가상환경
- 불편하지만, 매우 가벼움
- Python을 직접 설치 + 가상환경 직접 생성(venv)
- Pythin -m venv venv

### 1-3. Github
  - 버전관리도구
  - 코드를 관리해주는 웹 저장소
  #### Repository 연결
  - 깃허브는 프로젝트 단위로 Repository 생성
  - 팀장이 Repository를 생성하고 팀원들을 초대해서 협업
  - 깃허브는 git이라고 하는 버전관리도구를 손쉽게 사용할 수 있는 플랫폼(git설치) / git -v확인 가능
  - 로컬(컴퓨터, 노트북)-글로벌(website)
  - Repository가 로컬, 글로벌 존재
  - git status : git Repository 현재 상태
  - git init . : git Repository 생성(로컬)
  - git remote -v : 원격 Repository 연결 상태 확인(글로벌)
  - git romote add origin [URL] : 로컬과 글로벌 Repository 연결
  - git branch -M main : Master Branch -> Main branch 변경
  - git pull origin main : 글로벌의 Main 코드를 내려받기
  - git add [file] : 해당 파일을 버전관리 목록 추가
  - git add . : 현재 경로의 모든 파일을 버전관리 목록 추가
  - git commit -m "내용" : 버전 생성
  - git add와 commit 로컬에서 행위(글로벌 변화 X)
  - git push origin main : Local의 commit으로 생성한 버전을 글로벌에 업로드

## 2. Project Chatbot
### 2-1. 구조
- frontend: 사용자 화면 인터페이스
- backend: 서비스
  ㄴ ai(langchain)
  ㄴ database

### 2-2. frontend
- 웹 표준: HTML, CSS, Javascript
- -> 프론트엔드 프레임워크: React.js, Vue.js, ...

### 2-3. backend
- Python: Django(web), Flask, FastAPI(AI)
- -> FastAPI 점유율↑
- main(컨트롤타워) -> router(기능별 분류) -> service(실제 동작) -> crud(DB)

### 2-4. Chatbot(AI)
- Langchain(프레임워크) + OpenAI GPT(model)
- -> 고도화: LangChain + LangGraph + Model

### 2-5. Database
- PostgreSQL 사용 (Hybrid DB)
-   ㄴ RDB + NoSQL

### 2-5-1. rnwh
 - DBMS(데이터베이스 관리 시스템) -> MariaDB or PostgreSQL
 -    ㄴ Database -> kwu : 프로젝트 단위
 -           ㄴ Table -> chat_history: 대화기록 저장할 공간
 -                ㄴ Column 4개: session_id, type(H or AI), message, regdate