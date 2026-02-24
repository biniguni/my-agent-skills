# Machine Learning / Deep Learning Project Structure

When scaffolding a `ml_dl` project, the following directory structure and file layout is recommended.
The scaffold script only creates the directories. The files listed below are suggestions for how to organize your code.

```text
project_name/
├── data/
├── experiments/       # 실험 결과 저장소 (Logs, Tensorboard, Checkpoints)
│   ├── exp_001/       # 실험 번호나 날짜별로 폴더 생성
│   └── exp_002/
├── notebooks/         # 아이디어 스케치용 (scratchpad)
├── papers/            # 관련 논문 PDF, LaTeX 소스, 참고자료
├── src/
│   ├── models/        # 커스텀 레이어, 손실 함수 등 연구 코드
│   │   ├── __init__.py        # 패키지 인식용 (필수)
│   │   ├── baseline.py        # 기본 모델 (예: 간단한 CNN/LSTM)
│   │   ├── transformer.py     # 새로 실험할 복잡한 모델
│   │   ├── components.py      # 재사용할 레이어 모음 (Custom Layer, Attention Block 등)
│   │   └── loss.py            # 직접 만든 손실 함수 (Custom Loss)
│   └── trainer.py     # 학습 실행기
├── configs/           # 실험별 하이퍼파라미터, 경로, 환경변수 등
│   ├── model/
│   ├── dataset/
│   └── experiment/
├── train.py           # 학습 실행 엔트리 포인트
├── eval.py            # 평가 스크립트
└── README.md          # 프로젝트 개요 및 실행 방법
```
