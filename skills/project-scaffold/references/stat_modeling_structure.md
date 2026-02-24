# Statistical Modeling Project Structure

When scaffolding a `stat_modeling` project, the following directory structure and file layout is recommended.
The scaffold script only creates the directories. The files listed below are suggestions for how to organize your code.

```text
project_name/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/         # 데이터 탐색 및 통계 분석 결과 
├── src/
│   ├── __init__.py
│   └── inference.py   # 가설 검정, A/B 테스트 추론 등 주요 통계 로직
├── reports/           # 통계 결과, Markdown/PDF 리포트
├── main.py            # 실행 파이프라인
├── requirements.txt
└── README.md          # 프로젝트 개요 및 실행 방법
```
