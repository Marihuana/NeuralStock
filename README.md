
# 🧠 NeuralStock 🚀  
**AI 기반 자동 주식 매매 시스템**  

NeuralStock은 **Python과 AI를 활용하여 주식 데이터를 분석하고 자동으로 매매하는 시스템**입니다.  
AI 모델을 이용한 주가 예측, 백테스트, 그리고 실시간 자동 매매 기능을 제공합니다.  

---

## 📌 주요 기능  
✅ **실시간 주식 데이터 가져오기** (`yfinance`, `requests`)  
✅ **주가 데이터 분석 & 시각화** (`pandas`, `matplotlib`)  
✅ **AI 기반 주가 예측 모델** (`scikit-learn`, `tensorflow`)  
✅ **자동 매매 알고리즘** (퀀트 전략 적용)  
✅ **증권사 API 연동 (매매 자동화)**  

---
## 📊 프로젝트 구조
``` 
NeuralStock/
│── data/                  # 📊 주식 데이터 저장
│── models/                # 🤖 훈련된 AI 모델 저장
│── notebooks/             # 📒 Jupyter Notebook 분석 파일
│── src/                   # 🏗️ 핵심 Python 코드
│   │── main.py            # 🏁 프로그램 실행 메인 파일
│   │── data_fetcher.py     # 📡 주식 데이터 수집
│   │── data_analyzer.py    # 📈 데이터 분석
│   │── strategy.py         # 📊 투자 전략
│   │── trader.py           # 💰 자동 매매
│   │── config.py           # ⚙️ 설정 파일
│── logs/                  # 📝 프로그램 실행 로그
│── requirements.txt       # 📦 필요한 라이브러리 목록
│── README.md              # 📃 프로젝트 설명 문서
```

## 🚀 Git 브랜치 전략

NeuralStock 프로젝트는 **GitHub Flow**와 **Git Flow**를 조합한 전략을 사용합니다.  
각 브랜치의 역할은 다음과 같습니다:

- `main` → **배포용 브랜치** (Stable)  
  - 안정적인 버전만 포함되며, 직접 커밋하지 않음.  
  - `develop` 브랜치에서 충분히 테스트된 후 병합됨.  

- `develop` → **최신 개발 브랜치**  
  - 새로운 기능이 추가될 때 기본적으로 이 브랜치에서 작업함.  
  - 모든 `feature/xxx` 브랜치는 `develop`에서 분기되고, 완료되면 `develop`으로 병합됨.  

- `feature/xxx` → **새로운 기능 개발 브랜치**  
  - 특정 기능을 개발할 때 `develop`에서 분기하여 작업.  
  - 완료되면 `develop`으로 병합 후 삭제.  
  - 브랜치 이름 예시: `feature/data-fetching`, `feature/ai-model`  

- `hotfix/xxx` → **긴급 버그 수정 브랜치**  
  - `main`에서 직접 분기하여 긴급한 버그 수정 진행.  
  - 수정 완료 후 `main`과 `develop`에 병합.  
  - 브랜치 이름 예시: `hotfix/api-fix`, `hotfix/data-bug`  

📌 **브랜치 생성 & 병합 예시**
```sh
# 새로운 기능 개발
git checkout develop
git checkout -b feature/data-fetching
# 작업 후
git commit -m "✨ 주식 데이터 수집 기능 추가"
git push origin feature/data-fetching
# PR 생성 후 develop에 병합
```

## 💡 사용 기술
- 언어: Python
- 라이브러리: pandas, numpy, matplotlib, seaborn
- 머신러닝: scikit-learn, tensorflow, torch
- API: yfinance, requests, FastAPI
- 자동 매매: 증권사 OpenAPI

## 📌 TODO 리스트 (진행 상황)
- 프로젝트 기본 구조 설정
- GitHub 연동
- 실시간 주식 데이터 가져오기
- AI 기반 주가 예측 모델 개발
- 자동 매매 알고리즘 구현
- 증권사 API 연동

## 🤝 기여 방법 (Collaborate)
1. NeuralStock 저장소를 Fork
2.	새로운 기능 개발 후 Pull Request 생성
3.	리뷰 후 Merge 진행

## 📞 문의 & 연락처
📩 이메일 : bracket0723@gmail.com
📌 GitHub Issue 탭을 이용해주세요!