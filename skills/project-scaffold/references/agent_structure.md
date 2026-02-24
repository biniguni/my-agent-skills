# AI Agent Project Structure

When scaffolding an `agent` project, the following directory structure and file layout is recommended.
The scaffold script only creates the directories. The files listed below are suggestions for how to organize your code.

```text
project_name/
├── agents/            # 에이전트 핵심 로직, 프롬프트, 상태 관리 등
│   ├── __init__.py
│   └── core_agent.py
├── tools/             # 에이전트가 사용할 도구(Tools) 모음
│   ├── __init__.py
│   └── calculator.py
├── memory/            # 단기/장기 메모리 및 Vector DB 연동 등
├── config/            # API 키, 환경변수, 설정 등
├── tests/             # 에이전트/툴 단위 테스트 (매우 중요)
├── main.py            # 에이전트 실행 진입점
├── requirements.txt
└── README.md          # 프로젝트 개요 및 실행 방법
```
