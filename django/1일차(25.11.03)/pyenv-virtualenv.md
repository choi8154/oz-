# pyenv

### 0) pyenv란?
- 파이썬 버전 관리자, 어떤 파이썬으로 돌릴지를 고름.(버전 스위치)

### 1) 설치방법은?
- brew install pyenv


### 2) 사용 방법은?
- 전역 : pyenv global 3.11.9
- 현재 프로젝트 기준 : pyenv local 3.11.9
- 현재 터미널 세션만 임시로 : pyenv shell 3.11.9


# pyenv-virtualenv

### 0) pyenv-virtualenv란?
- 프로젝트 격리 환경 그 파이썬 위에서 패키지를 분리함.(환경 격리)

### 1) 설치방법은?
1. pyenv먼저 설치 돼있어야함 : brew install pyenv-virtualenv
2. 다음 설정을 위해 셸 위치 확인 : which $SHELL
3. 쉘이 켜질 때 pyenv-virtualenv 기능을 자동으로 활성화(zsh가 위치일 시) : echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc 

### 2) 사용 방법은?
1. pyenv install 3.12.2 : 3.12.2 가 미리 설치되어 있어야함. 그래서 설치
2. pyenv virtualenv 3.12.2 myenv : 3.12.2 기반으로 이름이 myenv인 가상환경을 생성.
3. pyenv local myenv : 프로젝트 폴더에 자동으로 들어오면 자동 활성화되게하는 명령어.
4. pyenv activate myenv : 위 명령어를 수행한 시점에 지금 쉘에서 즉시 활성화.
5. python --version : 파이썬 버전 확인.
6. which python : 파이썬 가상환경 잡혔는지 확인.
7. 페키지 설치 : pip install <페키지>
8. 설치 확인 : pip list