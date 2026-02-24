# Data Analysis Project Structure

When scaffolding a `data_analysis` project, the following directory structure and file layout is recommended.
The scaffold script only creates the directories. The files listed below are suggestions for how to organize your code.

```text
project_name/
├── main.py                # 전체 파이프라인(엔드투엔드) 실행 스크립트
├── config/                # 설정 파일 (DB 접속 정보, 하이퍼파라미터 등)
│   └── config.yaml        
├── data/
│   ├── raw/               # 원본 데이터 (Immutable)
│   └── processed/         # 최종 분석용 데이터
├── notebooks/             # 탐색적 분석(EDA) 및 실험
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda_visualization.ipynb
│   └── 03_modeling_test.ipynb
├── src/                   # 재사용 가능한 모듈화된 코드
│   ├── __init__.py
│   ├── analysis/          # 주요 분석 로직, 통계 모델링
│   │   ├── __init__.py
│   │   └── statistics.py
│   ├── utils/             # 공통 유틸리티
│   │   ├── __init__.py
│   │   ├── db_loader.py   # DB 연결 및 쿼리 실행
│   │   ├── logger.py      # 로그 기록 설정
│   │   └── helpers.py     # 공통 함수 (날짜 계산 등)
│   └── visualization/     # 시각화 전용 함수
│       ├── __init__.py
│       └── plotting.py
├── output/                # 결과물
│   ├── models/            # 학습된 모델 파일 (.pkl, .h5 등)
│   ├── figures/           # 저장된 그래프 (png, pdf)
│   └── reports/           # 최종 리포트 (csv, xlsx)
├── tests/                 # (선택) src 코드 테스트용 스크립트
├── .gitignore             # Git 제외 목록 (데이터, 설정값 등)
├── requirements.txt       # 의존성 패키지 목록
└── README.md              # 프로젝트 개요 및 실행 방법
```
