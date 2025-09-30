# Python Print Examples — Quick Guide
이 저장소는 Python의 다양한 `print()` 사용법을 담은 예제들을 보여주고, VS Code와 Jupyter 환경에서 실행하는 간단한 안내를 제공합니다.

---

## 파일 목록
### 1) `main_print_v1.py`
- **설명**: 기본적인 print() 함수와 다양한 출력 방식을 연습하는 스크립트입니다.

- **주요 기능**:

    - 기본 출력, 여러 값 출력 (sep, end 옵션)

    - f-string / .format() / % 스타일 출력

    - 딕셔너리, 리스트 등 복합 자료형 출력

    - 간단한 계산/함수 호출을 포함한 f-string

- **실행 방법**:
    - VS Code 터미널에서 다음 명령어를 실행하세요.

    - Windows: python main_print_v1.py

    - macOS/Linux: python3 main_print_v1.py

### 2) `main_print_v2.py`
- **설명**: rich 라이브러리를 사용하여 더 풍부하고 가독성 높은 출력을 만드는 예제입니다.

- **주요 기능**:

    - 컬러/스타일이 적용된 f-string 출력 (rprint)

    - Panel을 이용한 멀티라인 박스 출력

    - Table을 이용한 데이터 테이블 출력

- **사전 설치**:
이 파일을 실행하기 전에 가상환경을 활성화하고 pip로 rich를 설치해야 합니다.

>Bash
>
>pip install rich
### 3) `main_print_v1.ipynb`
- **설명**: main_print_v1.py와 동일한 내용의 Jupyter Notebook 파일입니다.

- **주요 특징**:

    - 셀 단위로 코드를 실행하고 결과를 바로 확인할 수 있는 환경입니다.

    - 코드 설명과 결과를 함께 문서로 만들기에 적합합니다.

    - 실행 방법:
VS Code에서 이 파일을 열고 각 셀을 실행하거나, 상단의 'Run All' 버튼을 사용해 전체 코드를 실행할 수 있습니다.

### 4) `requirements.txt`
- **설명**: 이 프로젝트에 필요한 파이썬 패키지 목록과 버전을 기록한 파일입니다.

- **주요 용도**:

    - 이 파일을 사용하면 다른 환경에서도 동일한 패키지를 쉽게 설치할 수 있습니다.

- **사용 방법**:

    - 모든 패키지 설치: pip install -r requirements.txt

    - 현재 환경의 패키지 목록 생성: pip freeze > requirements.txt